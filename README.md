# xianyuzhikong-web

闲鱼智控官网：静态产品首页、使用教程、更新日志与客户端下载，引导访客了解、安装与使用产品。

- 页面：`index.html` + `style.css` + `main.js`，原生 HTML/CSS/JS，没有构建步骤
- 新增页面：`tutorials/` 教程中心（Windows 图文安装、Mac 安装、自动发货视频），`changelog/` 更新日志，`download/` 下载；共用 `site.css` 与 `site.js`。
- 内容生成：`python3 tools/build_pages.py`，只用 Python 标准库。共享导航、页脚与页面模板在此脚本；生成的 HTML 一起纳入版本管理。
- Windows 图文原稿：`content/tutorials/windows.md`，由飞书 ZIP 导入，11 张截图压缩为 `img/tutorials/windows/*.webp`，激活输入区域已遮盖。改正文后运行生成命令。
- 版本内容：`content/releases.json` 是新增页面的版本真源，按已发布安装版倒序维护；下载页自动取第一条，不把未发布的源码更新写进公开日志。首页保留原内容，发布新版本时仍需核对其版本说明。
- 视频教程：清单在 `content/videos.json`（slug、卡片文案、本页目录），每期的图文摘要写在 `content/tutorials/<slug>.html`。`python3 tools/sync_videos.py` 从 `../video/publish/<source>/` 的 B 站投稿回执读 BV 号、时长、章节，把 16:9 封面转成 `img/tutorials/<slug>.webp`；回执写明已公开（`publication=public`）才上官网。部署时会自动先跑一遍。新视频公开后，由 agent 在清单里加一条、写好摘要（依据 `../video/episodes/<期>/script.md` 的旁白和功能口径，不写视频里没讲的功能），再部署；封面、BV 号、时长、章节都从投稿记录直接复用，不用手填。教程页含摘要与章节，不依赖嵌入式播放器。
- `sitemap.xml` 与 `robots.txt` 随页面生成。镜像只按白名单放静态文件（见 `Dockerfile`），不带内容原稿和工具。
- 截图：`img/`，全部来自闲鱼智控真实界面，买家、商品、店铺已打码
- 字体：`fonts/` 是思源宋体（Noto Serif SC）子集，只含页面上用到的字
- 来历：2026-10-28 在 `design-lab/poc/xianguanjia/simple/` 定稿（第 3 版），过程记录在 `design-lab/tasks/xianguanjia-landing.md`

## 发布

公开仓库 [dev-longshun/xianyu-zhikong-web](https://github.com/dev-longshun/xianyu-zhikong-web)，推送 `main` 就自动上线，和 Readex 官网同一套做法：

1. GitHub Actions（`.github/workflows/docker-publish.yml`）先重新生成页面，和提交的不一致就失败（改了 `content/` 或 `tools/` 记得生成后一起提交）；再构建 `ghcr.io/dev-longshun/xianyu-zhikong-web:latest`。
2. 服务器 shan-hk 的全局 Watchtower 每 60 秒检查一次，有新镜像就重建容器 `xianyu-web`（`/root/xianyu-web/docker-compose.yml`，127.0.0.1:8796）。
3. 宿主 nginx 管 HTTPS 和域名，反代到容器（`deploy/nginx.conf`）；缓存头在容器里（`docker/nginx.conf`）。

回滚：服务器上 `cd /root/xianyu-web`，把 compose 里的镜像改成 `ghcr.io/dev-longshun/xianyu-zhikong-web:sha-<旧提交>` 再 `docker compose up -d`（这时 Watchtower 不会再追 latest，修好后改回）。改容器前的宿主 nginx 配置备份在 `/root/xianyu.dongeai.com.nginx.bak-before-container-20261103`，旧的静态目录 `/var/www/xianguanjia-web` 暂时保留没删。

日常用 `sh deploy/deploy.sh`：同步视频、重新生成页面，有没提交的改动就停下；干净的话推送，并等到线上 `/version.txt` 变成本次提交才算发布完成，一般 2～3 分钟。

仓库是公开的：不放 `.env`、密钥、登录态、后台地址和未公开的价格或数据；截图要打码。

## 本地预览

```bash
python3 -m http.server 4176 --bind 127.0.0.1 --directory .
```

打开 http://127.0.0.1:4176/

## 作者微信一键开关

购买卡上的二维码和微信号可以随时关掉（比如交给别人推广时），「加微信购买」按钮和标题不受影响：

```bash
sh tools/contact.sh off      # 去掉二维码和微信号并发布，线上的二维码图片也删掉
sh tools/contact.sh on       # 放回去并发布
sh tools/contact.sh status   # 看现在是开还是关
NO_DEPLOY=1 sh tools/contact.sh on   # 只改本地不发布，先预览
```

块的内容在 `tools/contact-block.html`，换微信号改它，换二维码替换 `img/wechat-qr.webp`。切换后脚本会提交 `index.html` 并发布；`NO_DEPLOY=1` 时只改本地文件，不提交。

## 改了文案以后：重新切字体

字体子集只含现有的字，新加的字会退回系统宋体，所以改完文案要重切：

```bash
# 字体源（25MB，不进仓库）：
curl -L -o /tmp/NotoSerifSC.ttf "https://github.com/google/fonts/raw/main/ofl/notoserifsc/NotoSerifSC%5Bwght%5D.ttf"
python3 -m venv /tmp/fontvenv && /tmp/fontvenv/bin/pip install fonttools brotli
/tmp/fontvenv/bin/python tools/subset_font.py /tmp/NotoSerifSC.ttf . fonts/
```

## 不准做的

- 不编造：价格、用户数、评价、销量都只写真实的；联系方式没给就显示「未配置」
- 页面上的数字来自作者生产库的只读查询，更新时写明截止日期
- 不用闲鱼官方 logo，不叫「闲管家」，页脚保留「与闲鱼官方无关」
- 商业版安装包没有云端同步和客服站台，这两项不能当卖点（设备交接 2026-10-31 起安装版也有）
