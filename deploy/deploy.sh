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

rsync -rlzi --checksum --delete ${1:-} \
  --include='/index.html' --include='/style.css' --include='/main.js' \
  --include='/img/' --include='/img/*.webp' \
  --include='/fonts/' --include='/fonts/*.woff2' \
  --exclude='*' \
  ./ "$HOST:$DEST/"

[ "${1:-}" = "--dry-run" ] && exit 0
echo "已发布到 $HOST:$DEST"
curl -s --noproxy '*' -o /dev/null -w '线上首页：HTTP %{http_code}\n' https://xianyu.dongeai.com/ || true
