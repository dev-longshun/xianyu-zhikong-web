# xianguanjia-web

闲鱼智控的宣传页：一个纯静态网页，展示功能，引导访客加作者微信购买。

- 页面：`index.html` + `style.css` + `main.js`，原生 HTML/CSS/JS，没有构建步骤
- 截图：`img/`，全部来自闲鱼智控真实界面，买家、商品、店铺已打码
- 字体：`fonts/` 是思源宋体（Noto Serif SC）子集，只含页面上用到的字
- 来历：2026-10-28 在 `design-lab/poc/xianguanjia/simple/` 定稿（第 3 版），过程记录在 `design-lab/tasks/xianguanjia-landing.md`

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

块的内容在 `tools/contact-block.html`，换微信号改它，换二维码替换 `img/wechat-qr.webp`。切换后记得在仓库里提交 `index.html`。

## 改了文案以后：重新切字体

字体子集只含现有的字，新加的字会退回系统宋体，所以改完文案要重切：

```bash
# 字体源（25MB，不进仓库）：
curl -L -o /tmp/NotoSerifSC.ttf "https://github.com/google/fonts/raw/main/ofl/notoserifsc/NotoSerifSC%5Bwght%5D.ttf"
python3 -m venv /tmp/fontvenv && /tmp/fontvenv/bin/pip install fonttools brotli
/tmp/fontvenv/bin/python tools/subset_font.py /tmp/NotoSerifSC.ttf index.html fonts/
```

## 不准做的

- 不编造：价格、用户数、评价、销量都只写真实的；联系方式没给就显示「未配置」
- 页面上的数字来自作者生产库的只读查询，更新时写明截止日期
- 不用闲鱼官方 logo，不叫「闲管家」，页脚保留「与闲鱼官方无关」
- 商业版安装包没有云端同步和客服站台，这两项不能当卖点（设备交接 2026-10-31 起安装版也有）
