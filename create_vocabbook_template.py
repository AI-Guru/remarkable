from PIL import Image, ImageDraw
import os
import math

size = (1404, 1872)
center = (1404 // 2, 1872 // 2)


output_path = os.path.join("templates-custom", "vocabbook.png")
output_image = Image.new("RGB", size, "white")

draw = ImageDraw.Draw(output_image)

def draw_box(y1, y2):
    #step = 54
    step = 78
    for x in range(step * 2, size[0] - step, step):
        draw.line((x, y1, x, y2), fill="gray", width=1)

    draw.line((0, y1, size[0], y1), fill="gray", width=1)
    draw.line((0, y2, size[0], y2), fill="gray", width=1)
    draw.line((0, (y1 + y2) // 2, size[0], (y1 + y2) // 2), fill="gray", width=2)


draw_box(0, 900)
draw_box(972, 1872)

def draw_staple(x):
    offset = 10
    length = 50
    x1 = x - offset
    x2 = x1 - length
    draw.line((x1, size[1] // 2, x2, size[1] // 2), fill="gray", width=4)
    x1 = x + offset
    x2 = x1 + length
    draw.line((x1, size[1] // 2, x2, size[1] // 2), fill="gray", width=4)

draw_staple(468)
draw_staple(468 * 2)


del draw


output_image.save(output_path)
print(output_path + " saved.")
