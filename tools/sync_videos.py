"""把 B 站已公开的视频同步进官网教程：python3 tools/sync_videos.py。只用 Python 标准库，封面转换用 cwebp。

视频清单 content/videos.json 由人维护（slug、卡片文案、图文摘要放 content/tutorials/<slug>.html）。
本脚本只填每条的 auto 字段：从 ../video/publish/<source>/ 的投稿回执和计划里读 BV 号、时长、章节，
把 16:9 封面转成 img/tutorials/<slug>.webp。回执写明 publication=public 才上官网；
没公开、或这台机器上没有视频目录时保留原来的 auto，不清空，页面照旧生成。
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PUBLISH = ROOT.parent / 'video/publish'
VIDEOS = ROOT / 'content/videos.json'
CHAPTER = re.compile(r'^(\d{2}):(\d{2}) (.+)$')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cover(slug, plan, auto):
    """优先用 16:9 封面（和教程页卡片同比例）；源文件没变就不重新转换"""
    source = PUBLISH.parent / plan['cover']
    wide = source.with_name(source.name.replace('4比3', '16比9'))
    source = wide if wide.is_file() else source
    target = ROOT / 'img/tutorials' / f'{slug}.webp'
    sha = digest(source)
    if target.is_file() and auto.get('cover_source_sha256') in (sha, None):
        return f'/img/tutorials/{slug}.webp', sha  # 已有封面且来源没变（旧条目没记来源时沿用现有图）
    if not shutil.which('cwebp'):
        raise SystemExit('缺少 cwebp，先 brew install webp。')
    target.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['cwebp', '-quiet', '-q', '82', '-resize', '1200', '675', str(source), '-o', str(target)], check=True)
    return f'/img/tutorials/{slug}.webp', sha


def sync():
    videos = json.loads(VIDEOS.read_text())
    if not PUBLISH.is_dir():
        print(f'这台机器上没有 {PUBLISH}，保留 content/videos.json 里已有的视频信息。')
        return
    known = {v['source'] for v in videos}
    for video in videos:
        folder = PUBLISH / video['source']
        receipt, plan = folder / 'bilibili-receipt.json', folder / 'bilibili-plan.json'
        if not receipt.is_file():
            print(f"{video['slug']}：还没投稿，不上官网。")
            continue
        receipt, plan = json.loads(receipt.read_text()), json.loads(plan.read_text())
        if receipt.get('publication') != 'public':
            print(f"{video['slug']}：B 站还没公开（{receipt.get('platform_state_desc', '状态未知')}），暂不更新。")
            continue
        chapters = [[m[1] + ':' + m[2], int(m[1]) * 60 + int(m[2]), m[3]]
                    for m in map(CHAPTER.match, plan['description'].splitlines()) if m]
        auto = video.get('auto', {})
        image, sha = cover(video['slug'], plan, auto)
        video['auto'] = {'bvid': receipt['bvid'], 'url': f"https://www.bilibili.com/video/{receipt['bvid']}/",
                         'duration': round(plan['duration']), 'chapters': chapters, 'cover': image,
                         'cover_source_sha256': sha, 'bilibili_title': receipt['title']}
        print(f"{video['slug']}：{receipt['bvid']}，{len(chapters)} 个章节。")
    VIDEOS.write_text(json.dumps(videos, ensure_ascii=False, indent=2) + '\n')
    for folder in sorted(PUBLISH.iterdir()):
        receipt = folder / 'bilibili-receipt.json'
        if folder.name not in known and receipt.is_file() and json.loads(receipt.read_text()).get('publication') == 'public':
            print(f'新公开的视频还没上官网：{folder.name}。在 content/videos.json 加一条（slug、卡片文案），'
                  f'图文摘要写进 content/tutorials/<slug>.html，再运行本脚本。', file=sys.stderr)


if __name__ == '__main__':
    sync()
