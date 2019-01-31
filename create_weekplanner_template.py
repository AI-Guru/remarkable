from PIL import Image, ImageDraw, ImageFont
import os
import math

size = (1404, 1872)
output_path = os.path.join("templates-custom", "weekplanner.png")


home_path = os.path.expanduser("~")
font_path = os.path.join(home_path, "Library/Fonts/GARA.TTF")
font_size = 50
font = ImageFont.truetype(font_path, font_size)

# Prepare output.
output_image = Image.new("RGB", size, "white")
draw = ImageDraw.Draw(output_image)

def draw_box(text, y1_in, y2_in, last):
    line_width = 2
    offset = 100

    # Line from left to right.
    x1 = 0
    x2 = size[0]
    y1 = y2_in
    y2 = y2_in
    draw.line((x1, y1, x2, y2), fill="gray", width=line_width * 2)
    print((x1, y1, x2, y2))


    # Line from top to bottom
    x1 = offset
    x2 = x1
    y1 = y1_in
    y2 = y2_in
    draw.line((x1, y1, x2, y2), fill="gray", width=line_width * 2)
    print((x1, y1, x2, y2))

    # Line from top to bottom
    x1 = (offset + size[0]) // 2
    x2 = x1
    y1 = y1_in
    y2 = y2_in
    draw.line((x1, y1, x2, y2), fill="gray", width=line_width)
    print((x1, y1, x2, y2))

    # Draw text.
    x = offset // 2 - font_size // 2
    y = (y1 + y2) // 2 - font_size // 2
    draw.text((x, y), text, font=font, fill="black")


offset = 100
texts = ["M", "D", "M", "D", "F", "W"]
for index, text in enumerate(texts):
    y1 = int((size[1] - offset) * index / len(texts)) + offset
    y2 = int((size[1] - offset) * (index + 1) / len(texts)) + offset
    draw_box(text, y1, y2, index == len(texts) - 1)


# Line from top to bottom
x1 = 0
x2 = size[0]
y1 = offset
y2 = offset
line_width = 2
draw.line((x1, y1, x2, y2), fill="gray", width=line_width)
print((x1, y1, x2, y2))

# Draw text.
x = offset // 2 - font_size // 2 + offset
y = offset // 2 - font_size // 2
draw.text((x, y), "Week number:", font=font, fill="black")

del draw

output_image.save(output_path)
print(output_path + " saved.")
exit(0)
