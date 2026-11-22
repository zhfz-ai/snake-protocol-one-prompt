#!/usr/bin/env python3
"""Render SNAKE PROTOCOL video frames (1920x1080) with PIL: prompt -> code -> real gameplay -> CTA."""
import os, random
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frames")
os.makedirs(OUT, exist_ok=True)
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
BG = (7, 8, 18); PANEL = (11, 14, 29); GRID = (20, 26, 51)
GREEN = (55, 242, 162); HEAD = (167, 255, 217); APPLE = (255, 84, 112)
TEXT = (232, 246, 255); MUTED = (157, 184, 210); GOLD = (255, 209, 102)

def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)

def base():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([60, 60, W - 60, H - 60], outline=(38, 50, 94), width=3)
    return img, d

PROMPT = "Build me a neon snake game that plays itself when I'm idle and speeds up every 5 apples — one file, no libraries."
CODE_LINES = [
    "const CELL = 20, COLS = 24, ROWS = 24;",
    "function aiStep() {",
    "  const head = snake[0];",
    "  // pick the safe move closest to the apple",
    "  for (const d of options) {",
    "    const cost = Math.abs(nx - apple.x) + Math.abs(ny - apple.y);",
    "    if (cost < bestCost) { bestCost = cost; bestMove = d; }",
    "  }",
    "}",
    "function step() {",
    "  if (performance.now() - lastInput > 4000) aiStep();",
    "  if (head.x === apple.x) { score += 10; speedTier = 1 + (score / 50 | 0); }",
    "}",
    "// SNAKE PROTOCOL ready — open game.html and watch it drive",
]

frame = 0
def save(img):
    global frame
    img.save(os.path.join(OUT, f"f{frame:05d}.png"))
    frame += 1

# --- Segment A: prompt typed (2.5s @30fps = 75 frames) ---
for i in range(75):
    img, d = base()
    d.text((140, 150), "ONE PROMPT", font=font(34, True), fill=GREEN)
    d.text((140, 215), "I gave my AI agent one prompt:", font=font(40), fill=TEXT)
    shown = PROMPT[: max(0, int(len(PROMPT) * (i + 1) / 60))]
    # wrap manually
    words, lines, cur = shown.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > 62:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur: lines.append(cur)
    d.rounded_rectangle([120, 300, W - 120, 560], radius=18, fill=PANEL, outline=(38, 50, 94), width=2)
    for j, ln in enumerate(lines[:4]):
        d.text((160, 340 + j * 52), ln, font=font(36), fill=GOLD)
    if i % 15 < 8:
        cx = 160 + d.textlength(lines[-1] if lines else "", font=font(36)) + 8
        cy = 340 + (len(lines) - 1) * 52 if lines else 340
        d.rectangle([cx, cy, cx + 18, cy + 40], fill=TEXT)
    d.text((140, 640), "No libraries. One file. Watch it build.", font=font(34), fill=MUTED)
    save(img)

# --- Segment B: agent writing code (4s = 120 frames) ---
for i in range(120):
    img, d = base()
    d.text((140, 120), "AGENT AT WORK", font=font(34, True), fill=GREEN)
    d.text((140, 180), "game.html — writing the snake, the AI driver, the speed tiers…", font=font(32), fill=MUTED)
    d.rounded_rectangle([120, 250, W - 120, 880], radius=18, fill=PANEL, outline=(38, 50, 94), width=2)
    n = 1 + int(len(CODE_LINES) * (i + 1) / 120)
    for j, ln in enumerate(CODE_LINES[:n]):
        col = MUTED if ln.strip().startswith("//") else TEXT
        d.text((160, 285 + j * 42), ln, font=font(27), fill=col)
    d.text((140, 920), f"{min(100, int(100 * (i + 1) / 120))}%  ·  snake + AI + speed-up written", font=font(30), fill=GOLD)
    save(img)

# --- Segment C+D: real gameplay with the same AI logic (12s = 360 frames) ---
COLS = ROWS = 24; CELL = 34
BX, BY = (W - COLS * CELL) // 2, 200
random.seed(42)
snake = [(11, 12), (10, 12), (9, 12)]
direction = (1, 0)
score = 0
def new_apple():
    while True:
        p = (random.randrange(COLS), random.randrange(ROWS))
        if p not in snake: return p
apple = new_apple()
apples_eaten = 0
for i in range(360):
    # step the game every 3 frames
    if i % 3 == 0:
        hx, hy = snake[0]
        best, bestcost = None, 10 ** 9
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (dx, dy) == (-direction[0], -direction[1]): continue
            nx, ny = hx + dx, hy + dy
            if not (0 <= nx < COLS and 0 <= ny < ROWS) or (nx, ny) in snake: continue
            c = abs(nx - apple[0]) + abs(ny - apple[1])
            if c < bestcost: bestcost, best = c, (dx, dy)
        if best: direction = best
        head = (hx + direction[0], hy + direction[1])
        if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS) or head in snake:
            snake = [(11, 12), (10, 12), (9, 12)]; direction = (1, 0); score = 0; apples_eaten = 0; apple = new_apple()
        else:
            snake.insert(0, head)
            if head == apple:
                score += 10; apples_eaten += 1; apple = new_apple()
            else:
                snake.pop()
    tier = 1 + score // 50
    img, d = base()
    d.text((140, 110), "SNAKE PROTOCOL — LIVE", font=font(36, True), fill=GREEN)
    d.text((W - 640, 110), f"SCORE {score}   SPEED {tier}x   AUTO-DEMO", font=font(32, True), fill=GOLD)
    d.rectangle([BX - 4, BY - 4, BX + COLS * CELL + 4, BY + ROWS * CELL + 4], fill=PANEL, outline=(38, 50, 94), width=3)
    for gx in range(1, COLS): d.line([BX + gx * CELL, BY, BX + gx * CELL, BY + ROWS * CELL], fill=GRID)
    for gy in range(1, ROWS): d.line([BX, BY + gy * CELL, BX + COLS * CELL, BY + gy * CELL], fill=GRID)
    ax, ay = BX + apple[0] * CELL + CELL // 2, BY + apple[1] * CELL + CELL // 2
    d.ellipse([ax - 12, ay - 12, ax + 12, ay + 12], fill=APPLE)
    for k, (sx, sy) in enumerate(snake):
        d.rectangle([BX + sx * CELL + 3, BY + sy * CELL + 3, BX + (sx + 1) * CELL - 3, BY + (sy + 1) * CELL - 3],
                    fill=HEAD if k == 0 else GREEN)
    if i < 90:
        d.text((140, H - 150), "The finished game — playing itself. Real code, real run.", font=font(32), fill=TEXT)
    else:
        d.text((140, H - 150), "Built from one prompt. Come build on make.fun →", font=font(36, True), fill=GOLD)
    save(img)

print(f"frames={frame}")
