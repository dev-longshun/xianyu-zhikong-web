"""搜索引擎与 AI 助手可读性：robots.txt、llms.txt、每页的 Markdown 版本、结构化数据。

由 tools/build_pages.py 调用，只用 Python 标准库。
- 每个页面 /x/ 旁边生成 /x/index.md；容器 nginx 让 /x.md、/x/index.html.md 和带 Accept: text/markdown 的请求都拿到它。
- 首页 index.html 是手写的，只重写其中 <!-- seo:start --> 到 <!-- seo:end --> 之间的 head 片段。
"""
from html.parser import HTMLParser
import html
import json
import re

# 搜索引擎和 AI 助手的爬虫一律放行。逐个点名，免得各家走默认规则时被误判。
CRAWLERS = [
    # 国内搜索
    'Baiduspider', 'Sogou web spider', '360Spider', 'YisouSpider', 'Bytespider',
    # 国际搜索
    'Googlebot', 'Bingbot',
    # AI 助手：OpenAI、Anthropic、Perplexity、Google、Apple 等
    'GPTBot', 'OAI-SearchBot', 'ChatGPT-User',
    'ClaudeBot', 'Claude-SearchBot', 'Claude-User',
    'PerplexityBot', 'Perplexity-User',
    'Google-Extended', 'Applebot', 'Applebot-Extended',
    'CCBot', 'DeepSeekBot', 'Amazonbot', 'meta-externalagent', 'DuckAssistBot', 'MistralAI-User',
]


def robots(origin):
    agents = ''.join(f'User-agent: {name}\n' for name in CRAWLERS)
    return ('# 全站公开，欢迎搜索引擎和 AI 助手抓取、引用。\n'
            '# 每个页面都有 Markdown 版本：在网址后加 index.md，或请求时带 Accept: text/markdown。\n\n'
            'User-agent: *\nAllow: /\n\n'
            f'{agents}Allow: /\n\n'
            f'Sitemap: {origin}/sitemap.xml\n')


def ld(schemas):
    return ''.join('<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False).replace('<', '\\u003c') + '</script>'
                   for s in schemas)


def strip_tags(text):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', text))).strip()


def faqs_in(markup):
    """页面里 <details><summary>问</summary><p>答</p></details> 形式的常见问题。"""
    return [(strip_tags(q), strip_tags(a)) for q, a in
            re.findall(r'<details>\s*<summary>(.*?)</summary>\s*<p>(.*?)</p>\s*</details>', markup, re.S)]


def faq_schema(faqs):
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faqs]}


def organization(origin):
    return {'@type': 'Organization', '@id': origin + '/#org', 'name': '闲鱼智控', 'url': origin + '/',
            'logo': origin + '/img/apple-touch-icon.png'}


def software(origin, plans, latest, features):
    """软件本身：系统、版本、价格（价格与价格页同源，见 build_pages.PLANS）。"""
    return {
        '@context': 'https://schema.org', '@type': 'SoftwareApplication', '@id': origin + '/#app',
        'name': '闲鱼智控', 'alternateName': ['闲鱼自动发货软件', '闲鱼卖家电脑客户端'],
        'description': '闲鱼卖家用的电脑客户端：一个窗口登录多个闲鱼店铺，买家付款自动发货（卡密、网盘链接、文字），关键词自动回复，到点提醒收货，确认收货后自动好评。',
        'applicationCategory': 'BusinessApplication',
        'operatingSystem': 'macOS 11+（Apple 芯片）, Windows 10/11（64 位）',
        'softwareVersion': latest['version'], 'dateModified': latest['date'],
        'url': origin + '/', 'downloadUrl': origin + '/download/', 'releaseNotes': origin + '/changelog/',
        'screenshot': origin + '/img/t-msg.webp', 'inLanguage': 'zh-CN',
        'featureList': features,
        'publisher': {'@id': origin + '/#org'},
        'offers': [{
            '@type': 'Offer', 'name': name, 'description': fit, 'price': price, 'priceCurrency': 'CNY',
            'url': origin + '/pricing/', 'availability': 'https://schema.org/InStock',
            'priceSpecification': {'@type': 'UnitPriceSpecification', 'price': price, 'priceCurrency': 'CNY',
                                   'referenceQuantity': {'@type': 'QuantitativeValue', 'value': 1, 'unitCode': 'MON'}},
        } for name, price, fit, _badge, _items in plans],
    }


class _Markdown(HTMLParser):
    """把本站页面的 <main> 转成 Markdown。只覆盖本站用到的标签：标题、段落、列表、链接、图片、表格、折叠问答。"""
    SKIP_TAGS = {'script', 'style', 'svg', 'nav', 'aside', 'dialog', 'footer', 'noscript', 'template'}
    SKIP_CLASSES = {'breadcrumbs', 'skip-link', 'stage-bar', 'image-viewer', 'sr-only', 'dl-mobile', 'buy-contact'}
    BLOCKS = {'p', 'div', 'section', 'article', 'header', 'figure', 'figcaption', 'details', 'main', 'blockquote', 'dl', 'dt', 'dd'}

    def __init__(self, origin):
        super().__init__(convert_charrefs=True)
        self.origin, self.skip, self.lines, self.buf, self.prefix = origin, 0, [], '', ''
        self.lists, self.hrefs, self.row, self.rows = [], [], None, 0

    def url(self, value):
        if value.startswith(('http://', 'https://')):
            return value
        return self.origin + '/' + value.lstrip('/')

    def flush(self, kind='p'):
        text = re.sub(r'[ \t\n]+', ' ', self.buf).strip()
        text = re.sub(r'\*\*\s*\*\*', '', text)
        if text:
            self.lines.append((kind, self.prefix + text))
        self.buf, self.prefix = '', ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set((attrs.get('class') or '').split())
        if self.skip or tag in self.SKIP_TAGS or classes & self.SKIP_CLASSES:
            if tag not in ('img', 'br', 'input', 'source', 'meta', 'link'):
                self.skip += 1
            return
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.flush(); self.prefix = '#' * int(tag[1]) + ' '
        elif tag == 'summary':
            self.flush(); self.prefix = '### '
        elif tag in self.BLOCKS:
            self.flush()
        elif tag in ('ul', 'ol'):
            self.flush(); self.lists.append([tag, 0])
        elif tag == 'li':
            self.flush()
            if self.lists:
                self.lists[-1][1] += 1
                kind, n = self.lists[-1]
                self.prefix = '  ' * (len(self.lists) - 1) + ('- ' if kind == 'ul' else f'{n}. ')
            else:
                self.prefix = '- '
        elif tag == 'button' and attrs.get('data-text'):
            # 首页截图切换按钮：按钮上只有两个字，说明在 data-text 里
            self.flush(); self.prefix = '- '; self.buf = '**'; self.hrefs.append(('button', attrs['data-text']))
        elif tag == 'a':
            href = attrs.get('href') or ''
            if href and not href.startswith('#'):
                self.buf += '['; self.hrefs.append(('a', self.url(href)))
            else:
                self.hrefs.append(('a', None))
        elif tag in ('strong', 'b'):
            self.buf += '**'
        elif tag == 'em':
            self.buf += '*'
        elif tag == 'span' and self.buf and not self.buf.endswith(' '):
            self.buf += ' '
        elif tag == 'br':
            self.buf += ' '
        elif tag == 'img':
            alt = attrs.get('alt') or ''
            if alt:
                self.buf += f'![{alt}]({self.url(attrs.get("src", ""))})'
        elif tag == 'table':
            self.flush(); self.rows = 0
        elif tag == 'tr':
            self.row = []
        elif tag in ('th', 'td'):
            self.buf = ''

    def handle_endtag(self, tag):
        if self.skip:
            if tag not in ('img', 'br', 'input', 'source', 'meta', 'link'):
                self.skip -= 1
            return
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'summary', 'li') or tag in self.BLOCKS:
            self.flush('li' if tag == 'li' else 'p')
        elif tag in ('ul', 'ol'):
            self.flush('li')
            if self.lists:
                self.lists.pop()
        elif tag == 'button' and self.hrefs and self.hrefs[-1][0] == 'button':
            self.buf += '**：' + self.hrefs.pop()[1]; self.flush('li')
        elif tag == 'a' and self.hrefs:
            _kind, href = self.hrefs.pop()
            if href:
                self.buf += f']({href})'
        elif tag in ('strong', 'b'):
            self.buf += '**'
        elif tag == 'em':
            self.buf += '*'
        elif tag in ('th', 'td') and self.row is not None:
            self.row.append(re.sub(r'\s+', ' ', self.buf).strip().replace('|', '\\|')); self.buf = ''
        elif tag == 'tr' and self.row is not None:
            self.lines.append(('tr', '| ' + ' | '.join(self.row) + ' |'))
            if self.rows == 0:
                self.lines.append(('tr', '|' + ' --- |' * len(self.row)))
            self.rows += 1; self.row = None

    def handle_data(self, data):
        if not self.skip:
            self.buf += data

    def markdown(self):
        self.flush()
        out, last = [], None
        for kind, text in self.lines:
            if out:
                out.append('\n' if kind == last and kind in ('li', 'tr') else '\n\n')
            out.append(text); last = kind
        return ''.join(out).strip() + '\n'


def markdown_page(page_html, origin, url):
    """整页 HTML → Markdown：标题和描述放在开头，正文取 <main>，结尾写明原网址。"""
    title = strip_tags(re.search(r'<title>(.*?)</title>', page_html, re.S).group(1))
    desc = re.search(r'<meta name="description" content="([^"]*)"', page_html)
    main = re.search(r'<main[^>]*>(.*)</main>', page_html, re.S).group(1)
    parser = _Markdown(origin)
    parser.feed(main)
    body = parser.markdown()
    head = f'---\ntitle: {title}\nurl: {origin}{url}\n' + (f'description: {html.unescape(desc.group(1))}\n' if desc else '') + '---\n\n'
    return head + body + f'\n---\n\n网页版：{origin}{url}　·　闲鱼智控是第三方闲鱼卖家工具，与闲鱼官方无关。\n'


def llms_txt(origin, plans, latest, sections):
    """站点根目录的 llms.txt：一句话说明 + 关键事实 + 按栏目列出的页面（附 Markdown 版地址）。"""
    price = '；'.join(f'{name} {price} 元 / 月（{fit}）' for name, price, fit, _b, _i in plans)
    lines = [
        '# 闲鱼智控',
        '',
        '> 闲鱼卖家用的电脑客户端（Mac / Windows）。一个窗口登录多个闲鱼店铺：买家付款后自动发货（卡密、网盘链接、文字），'
        '买家来问按关键词自动回复，发货后到点提醒收货，确认收货后自动好评，并能看经营数据、逐笔对账。',
        '',
        '关键事实：',
        f'- 价格：{price}。两个版本功能完全一样，区别只在每台电脑能登录几个闲鱼账号。',
        '- 一份授权可以激活两台电脑；下载后联系作者可以先领 7 天免费试用。',
        '- 系统：Mac（Apple 芯片，macOS 11 及以上）、Windows 10 / 11（64 位）。手机不能安装。',
        '- 软件在电脑上运行，电脑开机联网、客户端保持运行时，自动发货和自动回复才会工作。',
        f'- 当前版本 v{latest["version"]}，{latest["date"]} 发布。',
        '- 购买方式：加作者微信购买，见官网首页「加微信购买」。',
        '- 闲鱼智控是第三方卖家工具，与闲鱼官方无关，也不是官方的「闲管家」。',
        '',
        '每个页面都有 Markdown 版本：把网址末尾的 / 换成 /index.md，或请求时带 Accept: text/markdown。',
    ]
    for heading, pages in sections:
        lines += ['', f'## {heading}', '']
        lines += [f'- [{title}]({origin}{url}): {desc}' for url, title, desc in pages]
    return '\n'.join(lines) + '\n'
