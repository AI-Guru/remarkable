from PIL import Image, ImageDraw
import os
import math

remarkable = False
remarkable = True
if remarkable = True:
    size = (1404, 1872)
    px_per_cm = 118 // 1.8
    line_width = 2
    output_path = os.path.join("templates-custom", "mandalacard.png")
else:
    size = (2480, 3507)
    px_per_cm = 118
    line_width = 2
    output_path = os.path.join("mandalacard.png")

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

    for radius_in_cm in [1.0, 2.5, 4.0, 5.0]:
        radius_in_px = cm_to_px(radius_in_cm)
        ellipse_shape = (c_x - radius_in_px, c_y - radius_in_px, c_x + radius_in_px, c_y + radius_in_px)
        draw.ellipse(ellipse_shape, outline="gray", width=line_width)

    draw_rays(c_x, c_y, 1.0, 5.0, 32)


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


del draw

output_image.save(output_path)
print(output_path + " saved.")
exit(0)



for index, radius in enumerate(range(0, 3000, 50)):
    ellipse_shape = (center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius)
    width = 1
    if index % 3 == 0:
        width = 2
    if index % 9 == 0:
        width = 3
    draw.ellipse(ellipse_shape, outline="gray", width=width)

for index, angle in enumerate(range(0, 360, 5)):
    offset = (int(3000 * math.sin(math.radians(angle))), int(3000 * math.cos(math.radians(angle))))
    x1 = center[0]
    y1 = center[1]
    x2 = center[0] + offset[0]
    y2 = center[1] + offset[1]
    width = 1
    if index % 3 == 0:
        width = 2
    if index % 9 == 0:
        width = 3
    draw.line((x1, y1, x2, y2), fill="gray", width=width)

del draw
