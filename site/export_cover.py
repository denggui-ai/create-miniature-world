"""Optional cover export: python3 site/export_cover.py (requires PyMuPDF).

Composes text and an existing case image; does not generate or retouch the case.
Not needed to install the Skill or view the website.
"""
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parent
doc = fitz.open()
page = doc.new_page(width=1200, height=630)
paper = (247 / 255, 246 / 255, 241 / 255)
ink = (37 / 255, 41 / 255, 34 / 255)
muted = (106 / 255, 111 / 255, 99 / 255)
page.draw_rect(page.rect, color=paper, fill=paper)
page.insert_font(fontname="cn", fontbuffer=fitz.Font("cjk").buffer)


def text(x, y, value, size, font="cn", color=ink):
    page.insert_text((x, y), value, fontsize=size, fontname=font, color=color)


text(56, 77, "微缩摄影", 23)
text(173, 75, "MINIATURE WORLD / SKILL", 10, "helv", muted)
text(56, 197, "A SMALL WORLD. A SECOND LOOK.", 11, "helv", muted)
text(52, 292, "日常物件，", 68)
text(52, 382, "另有天地。", 68)
text(56, 440, "让日常物件，成为有故事的小世界。", 18)
text(56, 536, "AI 微缩摄影与缩微场景创作", 12, color=muted)
text(56, 558, "Codex / Claude Code · 实验候选版", 12, color=muted)
page.insert_image(fitz.Rect(754, 46, 1144, 566),
                  filename=str(ROOT.parent / "examples" / "correction-tape-hiking.png"),
                  keep_proportion=True)
text(754, 590, "修正带 · 山地步道", 11, color=muted)
text(1063, 590, "AI 生成案例", 11, color=muted)
page.get_pixmap(alpha=False).save(ROOT / "cover.png")
print(ROOT / "cover.png")
