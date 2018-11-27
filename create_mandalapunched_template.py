from PIL import Image, ImageDraw
import os
import math

size = (1404, 1872)
center = (1404 // 2, 1872 // 2)


output_path = os.path.join("templates-custom", "mandalapunched.png")
output_image = Image.new("RGB", size, "white")

draw = ImageDraw.Draw(output_image)
radius = 75
radius_change = radius
for index in range(0, 50):
    ellipse_shape = (center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius)
    width = 1
    if index % 3 == 0:
        width = 2
    if index % 9 == 0:
        width = 3
    draw.ellipse(ellipse_shape, outline="gray", width=width)
    radius_change *= 0.94
    radius += radius_change

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


output_image.save(output_path)
print(output_path + " saved.")
