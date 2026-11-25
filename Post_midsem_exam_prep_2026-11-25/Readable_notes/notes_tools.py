"""Render the scanned notes and provide a searchable textbook reference.

All generated files stay beside this script. Source documents are read-only.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pymupdf

OUT = Path(__file__).resolve().parent
WORKSPACE = OUT.parents[1]
NOTES = WORKSPACE / "Study_material_after_mid_sems/MFOCS_Notes_Aug-Nov_2026.pdf"
TEXTBOOK = WORKSPACE / "Study_material_after_mid_sems/MCS_Textbook_Lehman_Leighton_Meyer.pdf"


def render(start: int, end: int, width: int = 1550) -> None:
    target = OUT / "source_pages"
    target.mkdir(exist_ok=True)
    with pymupdf.open(NOTES) as doc:
        for number in range(start, end + 1):
            page = doc[number - 1]
            scale = width / page.rect.width
            path = target / f"page_{number:03}.png"
            if not path.exists():
                page.get_pixmap(matrix=pymupdf.Matrix(scale, scale)).save(path)
            # Long phone scans also get overlapping crops for reading.
            pixel_height = page.rect.height * scale
            if pixel_height > 2300:
                chunk_height = 2100 / scale
                step = 1850 / scale
                y = 0.0
                part = 1
                while y < page.rect.height:
                    crop = target / f"page_{number:03}_part_{part:02}.png"
                    rect = pymupdf.Rect(0, y, page.rect.width, min(y + chunk_height, page.rect.height))
                    if not crop.exists():
                        page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), clip=rect).save(crop)
                    if y + chunk_height >= page.rect.height:
                        break
                    y += step
                    part += 1
            print(f"Rendered PDF page {number}: {path.name}")


def textbook_reference() -> None:
    reference = OUT / "reference"
    reference.mkdir(exist_ok=True)
    sections = []
    with pymupdf.open(TEXTBOOK) as doc:
        for number, page in enumerate(doc, 1):
            label = f"PDF PAGE {number}"
            if number >= 9:
                label += f" | PRINTED PAGE {number - 8}"
            sections.append(f"\n\n===== {label} =====\n\n{page.get_text(sort=True)}")
        (reference / "textbook_extracted.txt").write_text("".join(sections), encoding="utf-8")
        toc = doc.get_toc()
        (reference / "textbook_toc.json").write_text(json.dumps(toc, ensure_ascii=False, indent=2), encoding="utf-8")
    with pymupdf.open(NOTES) as doc:
        inventory = [
            {"pdf_page": n, "width": p.rect.width, "height": p.rect.height,
             "embedded_text_characters": len(p.get_text())}
            for n, p in enumerate(doc, 1)
        ]
    (reference / "notes_inventory.json").write_text(json.dumps(inventory, indent=2), encoding="utf-8")
    print("Prepared searchable textbook reference and 221-page notes inventory.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("reference")
    render_parser = sub.add_parser("render")
    render_parser.add_argument("start", type=int)
    render_parser.add_argument("end", type=int)
    render_parser.add_argument("--width", type=int, default=1550)
    args = parser.parse_args()
    if args.command == "reference":
        textbook_reference()
    else:
        render(args.start, args.end, args.width)
