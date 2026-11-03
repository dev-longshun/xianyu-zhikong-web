#!/bin/sh
# 发布官网：推送到 GitHub 就会自动上线。
#   push main → GitHub Actions 构建镜像 ghcr.io/dev-longshun/xianyu-zhikong-web:latest
#   → 服务器 shan-hk 的全局 Watchtower 60 秒内拉取，重建容器 xianyu-web → 宿主 nginx 反代到它。
# 本脚本先从 B 站投稿回执同步视频、重新生成页面；有没提交的改动就停下，先提交再发布。
# 推送后等线上 /version.txt 变成本次提交，最多等 6 分钟。
# 用法：sh deploy/deploy.sh
set -eu
cd "$(dirname "$0")/.."

python3 tools/sync_videos.py
python3 tools/build_pages.py
if [ -n "$(git status --porcelain)" ]; then
  echo '有没提交的改动（含刚重新生成的页面），先检查并提交再发布：' >&2
  git status --short >&2
  exit 1
fi

REV=$(git rev-parse HEAD)
git push origin main
echo "已推送 ${REV}，等 GitHub Actions 构建、服务器拉取上线…"
i=0
while [ $i -lt 72 ]; do
  ONLINE=$(curl -s --noproxy '*' -m 10 "https://xianyu.dongeai.com/version.txt" || true)
  if [ "${ONLINE}" = "${REV}" ]; then
    echo "已上线：https://xianyu.dongeai.com/（${REV}）"
    exit 0
  fi
  i=$((i + 1))
  sleep 5
done
echo '6 分钟内没等到新版本上线：到 GitHub 的 Actions 页面看构建是否失败，或在服务器上看 docker logs watchtower。' >&2
exit 1
