#!/usr/bin/env python3
"""Local photographic finish for a generated miniature photo.

Optionally adds grain or stylized blur above and below a horizontal band.
Blur uses image rows, not scene depth or subject boundaries. Effects default
to off; the output is not evidence of physically accurate depth of field.
Writes a new file; never overwrites the input or an existing output.
Applies EXIF orientation before finishing. Retains RGB ICC profiles for
RGB/RGBA inputs saved as PNG/JPEG/TIFF/WebP; unsupported profiles or formats
stop finishing so the caller can deliver the original without color conversion.

Usage:
  python3 photo_finish.py IN.png OUT.png [--focus-y 0.6] [--dof none|mild|shallow] [--grain 0]
  python3 photo_finish.py IN.png GRAIN.png --dof none --grain 3.5
"""
import argparse
import io
import math
import os
import sys

try:
    import numpy as np
    from PIL import Image, ImageFilter, ImageOps
except ImportError as exc:  # report and stop; caller delivers the original
    sys.exit(f"photo_finish: missing dependency ({exc}); deliver the original image")

# max blur radius as a fraction of image width, for the far (top) and near (bottom) ends
DOF_PRESETS = {"none": (0.0, 0.0), "mild": (0.004, 0.003), "shallow": (0.009, 0.007)}


def depth_blur(img, focus_y, band, far_r, near_r):
    w, h = img.size
    max_r = max(far_r, near_r)
    if max_r <= 0:
        return np.asarray(img).astype(np.float32)
    steps = 5
    radii = [max_r * i / (steps - 1) for i in range(steps)]
    stack = [np.asarray(img).astype(np.float32)]
    stack += [np.asarray(img.filter(ImageFilter.GaussianBlur(r))).astype(np.float32) for r in radii[1:]]
    y = (np.arange(h) + 0.5) / h
    # 0 inside the focus band, rising to 1 at the top/bottom edge
    above = np.clip((focus_y - band - y) / max(focus_y - band, 1e-6), 0, 1) * (far_r / max_r)
    below = np.clip((y - focus_y - band) / max(1 - focus_y - band, 1e-6), 0, 1) * (near_r / max_r)
    level = np.maximum(above, below) * (steps - 1)
    lo = np.floor(level).astype(int)
    hi = np.minimum(lo + 1, steps - 1)
    t = level - lo
    out = np.zeros_like(stack[0])
    for i in range(steps):
        wgt = (lo == i) * (1 - t) + (hi == i) * t
        out += stack[i] * wgt[:, None, None]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--focus-y", type=float, default=0.6, help="center of the clear horizontal band, 0<value<1 (top to bottom)")
    ap.add_argument("--band", type=float, default=0.05, help="half-height of the sharp band")
    ap.add_argument("--dof", choices=DOF_PRESETS, default="none", help="stylized horizontal-band blur; default none")
    ap.add_argument("--grain", type=float, default=0.0, help="grain strength in 8-bit levels; default 0 (off)")
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()

    if os.path.exists(a.dst):
        sys.exit(f"photo_finish: {a.dst} exists; choose a new name")
    if not 0 < a.focus_y < 1:
        sys.exit("photo_finish: --focus-y must be between 0 and 1")
    for name, value in (("band", a.band), ("grain", a.grain)):
        if not math.isfinite(value) or value < 0:
            sys.exit(f"photo_finish: --{name} must be finite and non-negative")

    img = Image.open(a.src)
    has_alpha = "A" in img.getbands() or "transparency" in img.info
    if has_alpha and img.format == "PNG":
        # PNG IHDR stores bit depth at byte 24. Pillow can downsample 16-bit
        # channels before exposing alpha, so keep the original in this case.
        with open(a.src, "rb") as source:
            header = source.read(25)
        if header[24] > 8:
            sys.exit("photo_finish: cannot reliably check high-bit-depth PNG transparency; skip finishing and deliver the original")
    if has_alpha and img.convert("RGBA").getchannel("A").getextrema()[0] < 255:
        sys.exit("photo_finish: transparent image; skip finishing and deliver the original")
    output_format = Image.registered_extensions().get(os.path.splitext(a.dst)[1].lower(), "PNG")
    save_options = {}
    profile = img.info.get("icc_profile")
    if profile is not None:
        # Keep the existing RGB encoding; never attach a CMYK/Gray/Lab profile
        # to converted RGB pixels. No new color-management dependency is needed.
        if img.mode not in ("RGB", "RGBA") or output_format not in ("PNG", "JPEG", "TIFF", "WEBP"):
            sys.exit("photo_finish: cannot preserve this ICC profile/output combination; deliver the original")
        try:
            from PIL import ImageCms
            color_space = ImageCms.ImageCmsProfile(io.BytesIO(profile)).profile.xcolor_space.strip()
        except (ImportError, OSError, ValueError):
            sys.exit("photo_finish: cannot validate ICC profile; deliver the original")
        if color_space != "RGB":
            sys.exit("photo_finish: ICC profile is not RGB; deliver the original")
        save_options["icc_profile"] = profile
    img = ImageOps.exif_transpose(img).convert("RGB")
    far, near = (f * img.size[0] for f in DOF_PRESETS[a.dof])
    out = depth_blur(img, a.focus_y, a.band, far, near)
    if a.grain > 0:
        rng = np.random.default_rng(a.seed)
        # luminance grain, slightly coarser than one pixel
        h, w = out.shape[:2]
        g = rng.normal(0, a.grain, (h // 2 + 1, w // 2 + 1)).repeat(2, 0).repeat(2, 1)[:h, :w]
        out = out + g[:, :, None]
    buf = io.BytesIO()
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(buf, format=output_format, **save_options)
    try:
        # exclusive create: never replace a file that appeared after the first check
        with open(a.dst, "xb") as f:
            f.write(buf.getvalue())
    except FileExistsError:
        sys.exit(f"photo_finish: {a.dst} exists; choose a new name")
    print(f"photo_finish: wrote {a.dst} (dof={a.dof}, focus_y={a.focus_y}, grain={a.grain})")


if __name__ == "__main__":
    main()
