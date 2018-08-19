from PIL import Image, ImageDraw
import os
import math

size = (1404, 1872)


output_path = os.path.join("templates-custom", "smallgrid.png")
output_image = Image.new("RGB", size, "white")

draw = ImageDraw.Draw(output_image)

# 1, 2, 3, 4, 6, 9, 12, 13, 18, 26, 36, 39, 52, 78, 117, 156, 234, 468
step = 26

for x in range(step, size[0], step):
    draw.line((x, 0, x, size[1]), fill="gray", width=1)

for y in range(step, size[1], step):
    draw.line((0, y, size[0], y), fill="gray", width=1)

del draw


output_image.save(output_path)
print(output_path + " saved.")
