# 字体源：https://github.com/google/fonts/raw/main/ofl/notoserifsc/NotoSerifSC%5Bwght%5D.ttf（25MB，OFL 许可，不进仓库）
# 依赖：pip install fonttools brotli（建议装在临时 venv 里）
# 用法：python subset_font.py <可变字体> <页面html> <输出目录>
# 按页面里实际出现的中文和全角标点，切出 400 / 600 两个静态字重的 woff2
import re, sys
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools import subset

src, page, out = sys.argv[1:]
text = Path(page).read_text(encoding='utf-8')
chars = set(re.findall(r'[‘-”…⺀-⻿　-〿㐀-䶿一-鿿豈-﫿︰-﹏＀-￯]', text))
print('字数', len(chars))
for w in (400, 600):
    f = TTFont(src)
    f = instantiateVariableFont(f, {'wght': w})
    opts = subset.Options(); opts.flavor = 'woff2'; opts.layout_features = ['*']; opts.name_IDs = ['*']
    s = subset.Subsetter(opts); s.populate(text=''.join(sorted(chars))); s.subset(f)
    p = Path(out) / f'serif-sc-{w}.woff2'; f.flavor = 'woff2'; f.save(p)
    print(p.name, p.stat().st_size // 1024, 'KB')
