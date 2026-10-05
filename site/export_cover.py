"""Optional README cover export: python3 site/export_cover.py (PyMuPDF).

Only lays out text and the original comb photo. Skill installation and the
website do not require this script. The photo is never retouched or replaced.
"""
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parent
doc = fitz.open()
page = doc.new_page(width=1200, height=630)
paper = (247 / 255, 244 / 255, 238 / 255)
ink = (48 / 255, 39 / 255, 31 / 255)
muted = (104 / 255, 100 / 255, 91 / 255)
green = (52 / 255, 74 / 255, 49 / 255)
page.draw_rect(page.rect, color=paper, fill=paper)
page.insert_font(fontname="cn", fontbuffer=fitz.Font("cjk").buffer)


def text(x, y, value, size, font="cn", color=ink):
    page.insert_text((x, y), value, fontsize=size, fontname=font, color=color)


# Retain the complete photo width. Only empty top/bottom background lies
# outside the page: the comb, tractor, people and seedlings remain in frame.
page.insert_image(fitz.Rect(380, -170, 1160, 870),
                  filename=str(ROOT.parent / "examples" / "comb-farm.png"),
                  keep_proportion=True)
text(46, 57, "微缩摄影", 24)
text(170, 55, "MINIATURE WORLD / SKILL", 10, "helv", muted)
text(46, 159, "A SMALL WORLD. A SECOND LOOK.", 10, "helv", muted)
text(42, 240, "日常物件，", 53)
text(42, 313, "另有天地。", 53)
text(46, 366, "AI 微缩摄影创作 Skill", 20)
text(46, 417, "从熟悉的日常物件，", 15, color=muted)
text(46, 443, "发现意想不到的小世界。", 15, color=muted)
text(46, 549, "Codex / Claude Code", 12, "helv", green)
text(46, 572, "实验候选版 · 图像工具需由宿主提供", 11, color=muted)
# Quiet caption sits in the photograph's empty background above the subject.
text(787, 71, "木梳 · 齿间农田", 17)
text(787, 97, "AI 生成案例", 11, color=muted)
page.get_pixmap(alpha=False).save(ROOT / "cover.png")
print(ROOT / "cover.png")
