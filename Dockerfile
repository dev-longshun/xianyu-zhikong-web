# 官网镜像：nginx 托管生成好的静态页面。push main 后由 GitHub Actions 构建推送 GHCR，
# 服务器上的全局 Watchtower 60 秒内拉取上线（见 README「发布」）。
FROM nginx:1.28-alpine
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
WORKDIR /usr/share/nginx/html
RUN rm -f index.html 50x.html
# 只放页面要用的文件；content/、tools/、deploy/ 等原稿和工具不进镜像
COPY index.html style.css main.js site.css site.js robots.txt sitemap.xml ./
COPY tutorials ./tutorials
COPY changelog ./changelog
COPY download ./download
COPY pricing ./pricing
COPY img ./img
COPY fonts ./fonts
ARG REVISION=dev
# 微信开关关着时（tools/contact.sh off）不带二维码图片；version.txt 供发布脚本确认新版本已上线
RUN if ! grep -q 'wechat-qr.webp' index.html; then rm -f img/wechat-qr.webp; fi \
 && echo "${REVISION}" > version.txt
