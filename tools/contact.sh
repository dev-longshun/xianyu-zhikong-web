#!/bin/sh
# 一键开关购买卡上的作者微信（二维码 + 微信号），改完直接发布到线上。
# 「加微信购买」按钮和标题不受影响，只动二维码和微信号这一块。
# 用法：sh tools/contact.sh on      放上二维码和微信号并发布
#       sh tools/contact.sh off     去掉二维码和微信号并发布（线上的二维码图片也一并删掉）
#       sh tools/contact.sh status  看现在是开还是关
#       NO_DEPLOY=1 sh tools/contact.sh on|off   只改本地文件不发布（先本地预览用）
# 块的内容存在 tools/contact-block.html，换微信号、换二维码改那个文件和 img/wechat-qr.webp。
set -eu
cd "$(dirname "$0")/.."

is_on() { grep -q 'class="buy-contact"' index.html; }

case "${1:-}" in
  status)
    if is_on; then echo "现在：开（页面上有二维码和微信号）"; else echo "现在：关（页面上没有二维码和微信号）"; fi
    exit 0 ;;
  on)
    if is_on; then echo "已经是开的，不用改"; else
      python3 - <<'PY'
from pathlib import Path
page = Path("index.html"); text = page.read_text()
block = Path("tools/contact-block.html").read_text()
end = "      <!-- contact:end -->"
assert text.count(end) == 1, "index.html 里找不到 contact:end 标记"
page.write_text(text.replace(end, block + end))
PY
      echo "已放上二维码和微信号"
    fi ;;
  off)
    if ! is_on; then echo "已经是关的，不用改"; else
      python3 - <<'PY'
import re
from pathlib import Path
page = Path("index.html"); text = page.read_text()
new, count = re.subn(r"(<!-- contact:start[^\n]*-->\n).*?(      <!-- contact:end -->)", r"\1\2", text, flags=re.S)
assert count == 1, "index.html 里找不到 contact 标记"
page.write_text(new)
PY
      echo "已去掉二维码和微信号"
    fi ;;
  *)
    sed -n '2,7p' "$0"; exit 1 ;;
esac

[ "${NO_DEPLOY:-}" = 1 ] && { echo "没有发布（NO_DEPLOY=1）"; exit 0; }
sh deploy/deploy.sh
