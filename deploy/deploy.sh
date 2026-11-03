#!/bin/sh
# 一键发布：把网页文件同步到 shan-dmit-hk 的 /var/www/xianguanjia-web。
# 只传页面要用的文件，服务器上多出来的旧文件会被删掉；nginx 配置不在这里动。
# 不带 -p，新文件按服务器 root 的 umask 落成 644/755（macOS 自带的 rsync 不支持 --chmod）。
# 用法：sh deploy/deploy.sh          正式发布
#       sh deploy/deploy.sh --dry-run 只列出会改哪些文件
set -eu

HOST=shan-hk   # ~/.ssh/config 里的别名，root@103.117.101.244
DEST=/var/www/xianguanjia-web
cd "$(dirname "$0")/.."

# 微信开关关着时（tools/contact.sh off）不上传二维码，线上已有的那张也删掉。
# 只排除并删除二维码，避免使用 --delete-excluded 扩大到其他服务器文件。
DRY_RUN="${1:-}"
case "$DRY_RUN" in
  ''|--dry-run) ;;
  *) echo '用法：sh deploy/deploy.sh [--dry-run]' >&2; exit 2 ;;
esac
set --
if ! grep -q 'wechat-qr.webp' index.html; then
  set -- --filter='hide /img/wechat-qr.webp' --filter='risk /img/wechat-qr.webp'
fi

# 先从 B 站投稿回执同步已公开的视频（BV 号、章节、封面），再重新生成页面；
# 仅同步公开静态产物，不上传 content/、tools/ 或本地文件。
python3 tools/sync_videos.py
python3 tools/build_pages.py
rsync -rlzi --checksum --delete ${DRY_RUN:-} "$@" \
  --include='/index.html' --include='/style.css' --include='/main.js' \
  --include='/site.css' --include='/site.js' --include='/robots.txt' --include='/sitemap.xml' \
  --include='/tutorials/' --include='/tutorials/**/' --include='/tutorials/**/index.html' --include='/tutorials/index.html' \
  --include='/changelog/' --include='/changelog/index.html' \
  --include='/download/' --include='/download/index.html' \
  --include='/pricing/' --include='/pricing/index.html' \
  --include='/img/' --include='/img/**/' --include='/img/**/*.webp' --include='/img/*.webp' --include='/img/*.png' \
  --include='/fonts/' --include='/fonts/*.woff2' \
  --exclude='*' \
  ./ "$HOST:$DEST/"

[ "$DRY_RUN" = "--dry-run" ] && exit 0
echo "已发布到 $HOST:$DEST"
curl -s --noproxy '*' -o /dev/null -w '线上首页：HTTP %{http_code}\n' https://xianyu.dongeai.com/ || true
