from PIL import Image, ImageDraw
import os
import math

#remarkable = False
remarkable = True
if remarkable == True:
    size = (1404, 1872)
    px_per_cm = 118 // 1.8
    line_width = 2
    output_path = os.path.join("templates-custom", "table.png")
else:
    size = (2480, 3507)
    px_per_cm = 118
    line_width = 2
    output_path = os.path.join("table.png")

# Center.
center = (size[0] // 2, size[1] // 2)

# Conversions.
def cm_to_px(cm):
    return px_per_cm * cm

# Prepare output.

output_image = Image.new("RGB", size, "white")

draw = ImageDraw.Draw(output_image)

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


columns = 2
rows = 4
for column in range(columns):
    for row in range(rows):
        offset = cm_to_px(1)
        x1 = int(size[0] * column / columns) + offset
        y1 = int(size[1] * row / rows) + offset
        x2 = int(size[0] * (column + 1) / columns) - offset
        y2 = int(size[1] * (row + 1) / rows) - offset
        draw.rectangle((x1, y1, x2, y2), fill="white", outline="gray")

#draw_border(0, 0.5 * center[1], size[0], 0.5 * center[1])
#draw_border(0, center[1], size[0], center[1])
#draw_border(0, 1.5 * center[1], size[0], 1.5 * center[1])
#draw_border(center[0], 0 , center[0], size[1])


del draw

output_image.save(output_path)
print(output_path + " saved.")
