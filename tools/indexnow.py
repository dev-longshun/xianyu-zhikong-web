#!/usr/bin/env python3
"""把改过的页面主动推给 IndexNow（必应、Yandex、Naver、Seznam 等共用；Google 不收）。

密钥文件是根目录的 <32 位十六进制>.txt，内容就是密钥本身，按协议必须公开放在网站根目录，
所以可以进公开仓库。由 deploy/deploy.sh 在新版本上线后调用，推送失败只提示、不让发布失败。

用法：
  python3 tools/indexnow.py --since <旧提交>   # 只推 旧提交..HEAD 之间改过的页面
  python3 tools/indexnow.py --all              # 推 sitemap 里全部页面（第一次接入、或想全量重推时）
  加 --dry-run 只打印要推的地址，不发请求。
"""
import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = 'https://xianyu.dongeai.com'
HOST = 'xianyu.dongeai.com'
ENDPOINT = 'https://api.indexnow.org/indexnow'


def find_key():
    keys = [p for p in ROOT.glob('*.txt') if re.fullmatch(r'[0-9a-f]{32}', p.stem)]
    if len(keys) != 1:
        sys.exit(f'根目录应当正好有一个 IndexNow 密钥文件（32 位十六进制.txt），现在有 {len(keys)} 个')
    key = keys[0].stem
    if keys[0].read_text().strip() != key:
        sys.exit(f'{keys[0].name} 的内容必须和文件名里的密钥一致')
    return key


def sitemap_urls():
    return re.findall(r'<url><loc>([^<]+)</loc>', (ROOT/'sitemap.xml').read_text())


def changed_urls(since, key, known):
    """旧提交..HEAD 之间改过的 index.html 对应的页面地址；只留 sitemap 里有的。
    旧提交里还没有密钥文件（第一次接入后发布）就推全部。"""
    if subprocess.run(['git', 'cat-file', '-e', f'{since}:{key}.txt'], cwd=ROOT,
                      capture_output=True).returncode != 0:
        print('上一版还没接 IndexNow（或本地没有那个提交），这次推送全部页面')
        return known
    try:
        out = subprocess.run(['git', 'diff', '--name-only', since, 'HEAD', '--', '*index.html'],
                             cwd=ROOT, check=True, capture_output=True, text=True).stdout
    except subprocess.CalledProcessError:
        print(f'本地找不到提交 {since}，改为推送全部页面')
        return known
    urls = []
    for path in out.split():
        url = ORIGIN + '/' + path[:-len('index.html')]
        if url in known:
            urls.append(url)
    return urls


def submit(key, urls):
    body = json.dumps({
        'host': HOST,
        'key': key,
        'keyLocation': f'{ORIGIN}/{key}.txt',
        'urlList': urls,
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method='POST',
                                 headers={'Content-Type': 'application/json; charset=utf-8'})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, ''
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(errors='replace')[:300]
    except OSError as e:
        return None, str(e)


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--since', help='旧提交（线上原来的 version.txt）')
    g.add_argument('--all', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    key = find_key()
    known = sitemap_urls()
    urls = known if args.all else changed_urls(args.since, key, known)
    if not urls:
        print('IndexNow：这次没有改到页面，不用推送')
        return
    print(f'IndexNow：推送 {len(urls)} 个页面')
    for u in urls:
        print('  ' + u)
    if args.dry_run:
        return
    status, detail = submit(key, urls)
    # 200 已收下；202 已收下、密钥还在验证（刚接入时常见）
    if status in (200, 202):
        print(f'IndexNow 已收下（HTTP {status}）')
    else:
        print(f'IndexNow 推送没成功（HTTP {status}）：{detail}。网站已正常上线，'
              f'可稍后手动重推：python3 tools/indexnow.py --all', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
