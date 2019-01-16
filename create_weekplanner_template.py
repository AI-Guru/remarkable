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


texts = ["M", "D", "M", "D", "F", "W"]
for index, text in enumerate(texts):
    y1 = int(size[1] * index / len(texts))
    y2 = int(size[1] * (index + 1) / len(texts))
    draw_box(text, y1, y2, index == len(texts) - 1)


del draw

output_image.save(output_path)
print(output_path + " saved.")
exit(0)



def draw_mandalacard(x1, y1, x2, y2):
    c_x = (x1 + x2) // 2
    c_y= (y1 + y2) // 2

    for radius_in_cm in [2.5, 4.0, 5.0]:
        radius_in_px = cm_to_px(radius_in_cm)
        ellipse_shape = (c_x - radius_in_px, c_y - radius_in_px, c_x + radius_in_px, c_y + radius_in_px)
        draw.ellipse(ellipse_shape, outline="gray", width=line_width)

    draw_rays(c_x, c_y, 2.5, 5.0, 32)


def draw_rays(x, y, radius_1, radius_2, rays):
    radius_1 = cm_to_px(radius_1)
    radius_2 = cm_to_px(radius_2)

    factors = [0]
    while factors[-1] < rays:
        if len(factors) % 2 == 0:
            factors.append(factors[-1] + 3)
        else:
            factors.append(factors[-1] + 1)

    for r in factors:
        angle = r * 360.0 / rays - 0.5 * 360.0 / rays
        angle = math.radians(angle)

        x1 = x + math.sin(angle) * radius_1
        y1 = y + math.cos(angle) * radius_1
        x2 = x + math.sin(angle) * radius_2
        y2 = y + math.cos(angle) * radius_2
        draw.line((x1, y1, x2, y2), fill="gray", width=line_width)


def draw_border(x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill="gray", width=4)



draw_mandalacard(0, 0, center[0], center[1])
draw_mandalacard(center[0], 0, size[0], center[1])
draw_mandalacard(0, center[1], center[0], size[1])
draw_mandalacard(center[0], center[1], size[0], size[1])
draw_border(0, center[1], size[0], center[1])
draw_border(center[0], 0 , center[0], size[1])


d
