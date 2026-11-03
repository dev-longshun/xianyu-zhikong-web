"""生成静态教程、更新日志和下载页：python3 tools/build_pages.py。无需第三方依赖。"""
from pathlib import Path
import html
import json
import re
import struct

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://xianyu.dongeai.com'
RELEASES = json.loads((ROOT / 'content/releases.json').read_text())
LATEST = RELEASES[0]
# 视频教程清单：人维护文案，tools/sync_videos.py 从 B 站投稿回执填 auto（BV 号、时长、章节、封面）。
# 只有填过 auto（B 站已公开）的视频才生成页面。
VIDEOS = [v for v in json.loads((ROOT / 'content/videos.json').read_text()) if v.get('auto', {}).get('bvid')]


def esc(value):
    return html.escape(str(value), quote=True)


def nav(active):
    links = [('/', '产品介绍'), ('/pricing/', '价格'), ('/tutorials/', '使用教程'), ('/changelog/', '更新日志'), ('/download/', '下载客户端')]
    return '''<a class="skip-link" href="#content">跳到正文</a>
<nav class="nav site-nav" aria-label="主导航"><div class="nav-in">
<a class="brand" href="/"><img class="brand-mark" src="/img/logo.webp" width="26" height="26" alt="">闲鱼智控</a>
<div class="nav-links">''' + ''.join(
        f'<a href="{url}"' + (' aria-current="page"' if active == url else '') + f'>{label}</a>'
        for url, label in links
    ) + '</div><a class="btn btn-sm" href="/#buy">加微信购买</a></div></nav>'


def footer():
    return '''<footer class="foot"><div class="wrap foot-in">
<div class="site-footer-links"><a href="/">产品介绍</a><a href="/pricing/">价格</a><a href="/tutorials/">使用教程</a><a href="/changelog/">更新日志</a><a href="/download/">下载客户端</a><a href="/#buy">联系作者</a></div>
<p><b>闲鱼智控</b>　闲鱼卖家的电脑客户端</p><p class="small">本软件为第三方卖家工具，与闲鱼官方无关</p></div></footer>'''


def page(url, title, desc, body, active, article=False):
    schemas = []
    if article:
        schemas.append({'@context': 'https://schema.org', '@type': 'TechArticle', 'headline': title,
                        'description': desc, 'inLanguage': 'zh-CN', 'url': ORIGIN + url,
                        'publisher': {'@type': 'Organization', 'name': '闲鱼智控'}})
        schemas.append({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': '首页', 'item': ORIGIN + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': '使用教程', 'item': ORIGIN + '/tutorials/'},
            {'@type': 'ListItem', 'position': 3, 'name': title, 'item': ORIGIN + url}]})
    schema = ''.join('<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False).replace('<', '\\u003c') + '</script>' for s in schemas)
    output = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · 闲鱼智控</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{ORIGIN}{url}"><meta property="og:type" content="{'article' if article else 'website'}"><meta property="og:title" content="{esc(title)} · 闲鱼智控"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{ORIGIN}{url}"><meta property="og:image" content="{ORIGIN}/img/t-msg.webp">
<link rel="stylesheet" href="/style.css"><link rel="stylesheet" href="/site.css"><link rel="icon" type="image/png" href="/img/favicon.png"><link rel="apple-touch-icon" href="/img/apple-touch-icon.png">{schema}</head>
<body>{nav(active)}<main id="content">{body}</main>{footer()}<script src="/site.js" defer></script></body></html>
'''
    destination = ROOT / url.lstrip('/') / 'index.html'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(output)
    return url


def head(title, desc, eyebrow, meta='', breadcrumb=False):
    crumbs = '<div class="breadcrumbs"><a href="/tutorials/">使用教程</a><span>/</span>' + esc(title) + '</div>' if breadcrumb else ''
    return f'<header class="wrap page-head">{crumbs}<p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p class="lede">{desc}</p>{meta}</header>'


def inline(text):
    text = esc(text)
    text = re.sub(r'\[([^\]]+)\]\((/[^ )]+|https://[^ )]+)\)', r'<a href="\2">\1</a>', text)
    return re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)


def image_size(path):
    # 导入图片为 WebP；解析 VP8X / VP8 / VP8L 的固有尺寸，保留布局空间。
    raw = (ROOT / path.lstrip('/')).read_bytes()
    kind = raw[12:16]
    if kind == b'VP8X':
        return int.from_bytes(raw[24:27], 'little') + 1, int.from_bytes(raw[27:30], 'little') + 1
    if kind == b'VP8 ':
        w, h = struct.unpack('<HH', raw[26:30])
        return w & 0x3fff, h & 0x3fff
    if kind == b'VP8L':
        bits = int.from_bytes(raw[21:25], 'little')
        return (bits & 0x3fff) + 1, ((bits >> 14) & 0x3fff) + 1
    raise ValueError(f'未知图片格式：{path}')


def markdown_windows():
    """飞书导出正文只含标题、段落、链接和独立图片，按原顺序生成。"""
    source = (ROOT / 'content/tutorials/windows.md').read_text()
    parts, toc = [], []
    for paragraph in re.split(r'\n\s*\n', source.strip()):
        paragraph = paragraph.strip()
        if paragraph.startswith('# '):
            continue
        if paragraph.startswith('## '):
            title = paragraph[3:]
            anchor = f'step-{len(toc) + 1}'
            toc.append((anchor, title))
            parts.append(f'<h2 id="{anchor}">{esc(title)}</h2>')
            continue
        match = re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)', paragraph)
        if match:
            alt, path = match.groups()
            w, h = image_size(path)
            parts.append(f'<figure class="guide-image"><a href="{esc(path)}" aria-label="放大查看：{esc(alt)}"><img src="{esc(path)}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></a><figcaption>{esc(alt)} · 点击图片可放大</figcaption></figure>')
        else:
            parts.append('<p>' + inline(paragraph.replace('\n', ' ')) + '</p>')
    return '\n'.join(parts), toc


def article_body(body, toc, after=''):
    sidebar = '<aside class="doc-toc" aria-label="本页目录"><p>本页内容</p>' + ''.join(f'<a href="#{key}">{title}</a>' for key, title in toc) + '<a href="/tutorials/">← 全部教程</a></aside>'
    return '<div class="wrap doc-layout">' + sidebar + '<article class="doc-body">' + body + after + '''<div class="article-next"><a href="/tutorials/">← 返回教程中心</a><a href="/download/">下载客户端 →</a></div></article></div>
<dialog class="image-viewer" id="image-viewer" aria-label="教程截图大图"><button type="button" autofocus>关闭大图 ×</button><figure><img alt=""><figcaption></figcaption></figure></dialog>'''


def minutes(seconds):
    return f'{seconds // 60} 分 {seconds % 60} 秒'


def video_card(video):
    auto = video['auto']
    return (f'<a class="video-card" href="/tutorials/{video["slug"]}/"><img src="{auto["cover"]}" width="1200" height="675" alt="{esc(video["cover_alt"])}" loading="lazy">'
            f'<div class="video-copy"><span class="tag">视频教程 · {minutes(auto["duration"])}</span><h3>{esc(video["card_title"])}</h3>'
            f'<p>{esc(video["card_text"])}</p><span class="card-link">查看教程与 B 站视频 →</span></div></a>')


def video_page(video):
    auto, url = video['auto'], video['auto']['url']
    chapters = ''.join(f'<li><a href="{url}?t={seconds}" target="_blank" rel="noopener"><span>{stamp}</span>{esc(label)} ↗</a></li>'
                       for stamp, seconds, label in auto['chapters'])
    guide = (ROOT / 'content/tutorials' / f'{video["slug"]}.html').read_text().strip()
    article = f'''<a href="{url}" target="_blank" rel="noopener"><img src="{auto["cover"]}" width="1200" height="675" alt="在 B 站观看{esc(video["title"])}完整演示"></a><div class="actions"><a class="btn" href="{url}" target="_blank" rel="noopener">去 B 站看完整演示 ↗</a></div>
<p class="page-meta"><span>时长 {minutes(auto["duration"])}</span><span>图文摘要 + 视频章节</span></p>
{guide}
<h2 id="chapters">按章节观看</h2><p>点击章节，在 B 站打开对应时间点。</p><ul class="chapter-list">{chapters}</ul>
<div class="note"><p>{esc(video["note"])}</p></div>'''
    body = head(video['title'], video['desc'], 'Feature Guide / Video', breadcrumb=True) + article_body(article, video['toc'])
    return page(f'/tutorials/{video["slug"]}/', video['title'], video['desc'], body, '/tutorials/', True)


def build():
    pages = ['/']
    title = '使用教程'
    desc = '从安装激活到功能设置，按步骤开始使用闲鱼智控。图文说明与视频演示，选择适合你的方式。'
    body = head(title, desc, 'Guides & Tutorials') + '''<div class="wrap">
<section class="content-section" aria-labelledby="getting-started"><div class="section-heading"><h2 id="getting-started">先从安装开始</h2><p>第一次使用，先完成下载、安装与激活</p></div>
<div class="guide-grid"><a class="guide-card" href="/tutorials/windows/"><span class="tag">Windows · 图文教程</span><h3>安装与激活</h3><p>从浏览器下载到安装向导，再到输入激活码。11 张操作截图，跟着一步步完成。</p><span class="card-link">查看 Windows 教程 →</span></a>
<a class="guide-card" href="/tutorials/mac/"><span class="tag">Mac · 快速开始</span><h3>安装与首次使用</h3><p>适用于 Apple 芯片 Mac。下载 DMG、拖入应用程序，完成激活后开始使用。</p><span class="card-link">查看 Mac 教程 →</span></a></div></section>
<section class="content-section" aria-labelledby="feature-guides"><div class="section-heading"><h2 id="feature-guides">跟着视频配置功能</h2><p>看操作过程，也看完成后的实际效果</p></div>
''' + ''.join(map(video_card, VIDEOS)) + '''</section>
<div class="help-strip"><p>安装或设置时遇到问题？可以联系作者说明具体情况。</p><a href="/#buy">联系作者 →</a></div></div>'''
    pages.append(page('/tutorials/', title, desc, body, '/tutorials/'))

    title = 'Windows 安装与激活'
    desc = '从下载安装包、完成安装，到输入激活码。按照图文步骤，完成闲鱼智控的首次安装。'
    article, toc = markdown_windows()
    article = '<div class="note"><p>适用系统：64 位 Windows 10 / 11。截图保留原教程界面，下载区域与按钮位置可能随版本调整，请以当前页面为准。</p></div>' + article
    body = head(title, desc, 'Installation / Windows', '<p class="page-meta"><span>图文教程 · 11 张操作截图</span><span>整理自原飞书安装教程</span></p>', True) + article_body(article, toc)
    pages.append(page('/tutorials/windows/', title, desc, body, '/tutorials/', True))

    title = 'Mac 安装与首次使用'
    desc = '下载、拖入应用程序、完成激活。适用于 Apple M 系列芯片的 Mac。'
    article = '''<div class="note"><p>系统要求：Apple 芯片（M 系列），macOS 11 及以上。暂不支持 Intel Mac，也不能安装在 iPhone 或 iPad 上。</p></div>
<h2 id="download">一、下载 Mac 安装包</h2><p>打开<a href="/download/">下载客户端</a>页面，选择「下载 Mac 版」，等待 DMG 文件下载完成。</p>
<h2 id="install">二、拖入应用程序</h2><ol><li>双击下载的 DMG 文件，打开安装窗口。</li><li>将「闲鱼智控」拖到「应用程序」文件夹。</li><li>在访达的「应用程序」中打开闲鱼智控。首次询问是否打开从互联网下载的 App 时，确认打开。</li></ol>
<h2 id="activate">三、完成激活</h2><p>可以先打开查看界面。需要登录闲鱼店铺时，点击客户端的「输入激活码」，输入自己的激活码并按提示完成激活。</p><p>输入时核对激活码是否完整，避免多余空格。尚未购买激活码，可<a href="/#buy">联系作者</a>。一份授权可以激活两台电脑。</p>
<h2 id="running">四、保持客户端运行</h2><p>闲鱼智控在电脑上运行。添加店铺后，需要电脑保持开机联网、软件保持运行，自动回复和自动发货等任务才会工作。需要长时间运行时，可在客户端设置里开启「挂机不休眠」。</p>
<p>安装完成后，可继续看<a href="/tutorials/auto-delivery/">自动发货教程</a>和<a href="/tutorials/keyword-reply/">关键词自动回复教程</a>，跟着视频配置功能。</p>'''
    body = head(title, desc, 'Installation / Mac', breadcrumb=True) + article_body(article, [('download','下载安装包'),('install','拖入应用程序'),('activate','完成激活'),('running','保持客户端运行')])
    pages.append(page('/tutorials/mac/', title, desc, body, '/tutorials/', True))

    pages += [video_page(video) for video in VIDEOS]

    # 价格页：价格与版本规则来源——基础版 19 元 / 月、高级版 29 元 / 月（作者 2026-11-02 定），
    # 账号规则见软件本体 cloud/license-server/README.md「码分两个版本」。没定的价格（季付、年付、升级补差）不写。
    title = '价格'
    desc = '两个版本功能完全一样，区别只在每台电脑能登录几个闲鱼账号。基础版 19 元一个月，高级版 29 元一个月。'
    plans = [
        ('基础版', '19', '一台电脑管一个店铺', '', [
            '每台电脑登录 1 个闲鱼账号，两台电脑一共 2 个',
            '换账号先退出当前账号，再扫码登录新账号',
            '一份授权激活两台电脑，Mac 和 Windows 都能用',
            '全部功能：自动发货、自动回复、提醒收货、自动评价、经营数据']),
        ('高级版', '29', '一台电脑管多个店铺', '多店铺选这个', [
            '每台电脑登录的闲鱼账号数量不限',
            '多个店铺在同一个客户端里，顶栏一点就切换',
            '一份授权激活两台电脑，Mac 和 Windows 都能用',
            '全部功能：自动发货、自动回复、提醒收货、自动评价、经营数据']),
    ]
    plan_html = ''.join(
        f'<section class="plan{" plan-featured" if badge else ""}" aria-labelledby="plan-{n}"><div class="plan-top"><h2 id="plan-{n}">{name}</h2>'
        + (f'<span class="tag">{badge}</span>' if badge else '')
        + f'</div><p class="plan-fit">{fit}</p><p class="plan-price"><b>{price}</b> 元 / 月</p><ul>'
        + ''.join(f'<li>{esc(item)}</li>' for item in items)
        + '</ul><a class="btn" href="/#buy">加微信购买</a></section>'
        for n, (name, price, fit, badge, items) in enumerate(plans))
    yes = '<span class="yes" aria-label="包含">✓</span>'
    rows = [
        ('价格', '19 元 / 月', '29 元 / 月'),
        ('可激活的电脑', '2 台', '2 台'),
        ('每台电脑可登录的闲鱼账号', '1 个', '<b>不限</b>'),
        ('两台电脑一共可登录', '2 个', '<b>不限</b>'),
        ('换账号', '先退出当前账号，再扫码登录', '直接扫码添加'),
        ('Mac（Apple 芯片）与 Windows 客户端', yes, yes),
        ('自动发货：卡密、网盘链接、多规格', yes, yes),
        ('关键词自动回复', yes, yes),
        ('提醒收货、自动评价', yes, yes),
        ('经营数据与订单明细', yes, yes),
        ('设备交接', yes, yes),
        ('应用内自动更新', yes, yes),
        ('有问题直接找作者', yes, yes),
    ]
    table = ('<div class="compare-wrap"><table class="compare"><caption class="sr-only">基础版与高级版对比</caption>'
             '<thead><tr><th scope="col">权益</th><th scope="col">基础版</th><th scope="col">高级版</th></tr></thead><tbody>'
             + ''.join(f'<tr><th scope="row">{label}</th><td>{a}</td><td>{b}</td></tr>' for label, a, b in rows)
             + '</tbody></table></div>')
    faqs = [
        ('两个版本有什么区别？', '功能完全一样，区别只在每台电脑能登录几个闲鱼账号：基础版 1 个，高级版不限。只有一个店铺选基础版就够了。'),
        ('基础版怎么换账号？', '点顶部账号旁的 × 退出当前账号，再扫码登录新账号。退出后聊天记录、订单和设置都留在本机，以后重新登录同一个账号即可恢复。'),
        ('买了基础版，以后能升级吗？', '能。联系作者把激活码升级为高级版，不用重新激活。在客户端「关于与更新」的授权信息里点「重新检查」立即生效，不点也会在 10 分钟内生效。'),
        ('以前买的激活码算哪个版本？', '此前购买的激活码都按高级版使用，账号数量不限，更新客户端后也不变。'),
        ('基础版激活码对客户端版本有要求吗？', '需要 1.4.0 及以上版本。官网下载的就是最新版；装着旧版本的，先在「关于与更新」里检查更新。'),
        ('没买能先下载看看吗？', '能。下载安装后不激活也能打开，看看界面和功能；想登录店铺实际用一用，联系作者可以领 7 天免费试用。正式使用要输入激活码。'),
    ]
    faq_html = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)
    body = head(title, desc, 'Pricing') + f'''<div class="wrap">
<div class="plans">{plan_html}</div>
<section class="content-section" aria-labelledby="compare"><div class="section-heading"><h2 id="compare">两个版本对比</h2><p>按月付费，两个版本都最多激活两台电脑</p></div>{table}</section>
<section class="content-section" aria-labelledby="pricing-faq"><div class="section-heading"><h2 id="pricing-faq">关于版本和购买</h2></div><div class="faq">{faq_html}</div></section>
<div class="help-strip"><p>拿不准选哪个？加作者微信说说你有几个店铺。</p><a href="/#buy">加微信购买 →</a></div></div>'''
    pages.append(page('/pricing/', title, desc, body, '/pricing/'))

    title = '更新日志'
    desc = '记录每个安装版的新功能、体验优化与问题修复。看看闲鱼智控最近有哪些变化。'
    releases = []
    for n, release in enumerate(RELEASES):
        groups = ''.join(f'<div class="release-group"><b>{esc(group["label"])}</b><ul>' + ''.join('<li>'+esc(item)+'</li>' for item in group['items']) + '</ul></div>' for group in release['groups'])
        releases.append(f'<article class="release" id="v{release["version"]}"><div class="release-top"><h2>v{release["version"]}</h2>' + ('<span class="tag">当前版本</span>' if n==0 else '') + f'<time datetime="{release["date"]}">{release["date"]}</time></div><h3>{esc(release["title"])}</h3><p>{esc(release["summary"])}</p>{groups}<div class="note"><p>{esc(release["upgrade"])}</p></div></article>')
    sidebar = '<aside class="doc-toc" aria-label="版本目录"><p>安装版发布记录</p>' + ''.join(f'<a href="#v{r["version"]}">v{r["version"]} · {r["date"]}</a>' for r in RELEASES) + '<a href="/download/">下载当前版本 →</a></aside>'
    body = head(title, desc, 'Product Updates') + '<div class="wrap release-layout">'+sidebar+'<div>'+''.join(releases)+'<p class="page-meta">这里记录已发布的安装版。开发中的改动将在正式发布后列出。</p></div></div>'
    pages.append(page('/changelog/',title,desc,body,'/changelog/'))

    title = '下载客户端'
    desc = '选好你的电脑系统，下载闲鱼智控。可以先打开看看界面，登录店铺前再完成激活。'
    body = head(title,desc,'Download',f'<p class="page-meta"><span>当前版本 v{LATEST["version"]}</span><span>发布于 {LATEST["date"]}</span><a href="/changelog/">查看更新内容 →</a></p>') + '''<div class="wrap"><div class="download-platforms">
<section class="platform"><svg class="platform-icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="11" rx="1.5"/><path d="M2 19h20l-2-4H4z"/></svg><h2>Mac 版</h2><p>Apple M 系列芯片<br>macOS 11 及以上 · DMG 安装包<br>暂不支持 Intel 芯片 Mac</p><a class="btn" href="https://dl.longjinapi.com/xianyu-zhikong-mac-arm64.dmg">下载 Mac 版 ↓</a><div class="platform-links"><a href="/tutorials/mac/">安装与首次使用 →</a></div></section>
<section class="platform"><svg class="platform-icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M9 20h6M12 16v4"/></svg><h2>Windows 版</h2><p>64 位 Windows 10 / 11<br>EXE 安装包<br>按安装向导完成安装</p><a class="btn" href="https://dl.longjinapi.com/xianyu-zhikong-windows-x64.exe">下载 Windows 版 ↓</a><div class="platform-links"><a href="/tutorials/windows/">图文安装与激活教程 →</a></div></section></div>
<div class="note"><p>手机不能安装此客户端。请用电脑打开本页下载；如果你正在手机上浏览，可以先查看教程，再把本页链接发到电脑。</p></div>
<div class="download-info"><section><h2>第一次使用，三步开始</h2><ol><li>下载对应系统的安装包，按<a href="/tutorials/">安装教程</a>完成安装。</li><li>先打开查看界面；登录闲鱼店铺前，输入激活码完成激活。想先试用，联系作者可以领 7 天免费试用。<a href="/pricing/">看两个版本的价格 →</a></li><li>电脑保持开机联网、客户端保持运行，自动化任务才能持续工作。</li></ol></section>
<section><h2>已经安装？在客户端更新</h2><p>在客户端「关于与更新」里检查更新，按提示下载并重启安装。更新会暂时中断自动化任务，请选择合适的时间。</p><p><a href="/changelog/">查看本次更新了什么 →</a></p></section></div>
<section class="content-section" style="margin-top:48px"><h2>下载与安装常见问题</h2><div class="faq">
<details><summary>Windows 下载或安装时出现提示怎么办？</summary><p>当前 Windows 安装包没有微软代码签名。请确认下载来自本站，并结合具体提示操作。浏览器的保留步骤见<a href="/tutorials/windows/">图文教程</a>；如果系统显示「Windows 已保护你的电脑」，确认来源后可选择「更多信息」→「仍要运行」。遇到无法确认的提示，可联系作者。</p></details>
<details><summary>Mac 第一次打开怎么安装？</summary><p>打开 DMG，将「闲鱼智控」拖入「应用程序」，再从应用程序中打开。首次询问是否打开从互联网下载的 App 时确认打开。详见<a href="/tutorials/mac/">Mac 安装教程</a>。</p></details>
<details><summary>没买激活码，能先下载吗？</summary><p>能。安装后可以先打开查看界面。想登录店铺实际用一用，联系作者可以领 7 天免费试用；正式使用再购买激活码。一份授权可以激活两台电脑。</p></details>
<details><summary>官网下载慢，有其他下载入口吗？</summary><p>可到<a href="https://github.com/dev-longshun/xianyu-zhikong/releases" target="_blank" rel="noopener">GitHub Releases</a>查看镜像和校验文件。GitHub 镜像已同步当前版本，与官网下载使用同一批安装包，附有 SHA-256 校验文件。</p></details>
</div></section><div class="help-strip"><p>准备好开始配置功能了？</p><a href="/tutorials/">前往使用教程 →</a></div></div>'''
    pages.append(page('/download/',title,desc,body,'/download/'))
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{ORIGIN}{url}</loc></url>\n' for url in pages) + '</urlset>\n')
    (ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n')
    print(f'已生成 {len(pages)-1} 个内容页、sitemap.xml 与 robots.txt。')


if __name__ == '__main__':
    build()
