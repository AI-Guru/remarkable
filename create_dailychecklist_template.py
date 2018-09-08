from PIL import Image, ImageDraw
import os
import math

size = (1404, 1872)


output_path = os.path.join("templates-custom", "dailychecklist.png")
output_image = Image.new("RGB", size, "white")

draw = ImageDraw.Draw(output_image)


# 1, 2, 3, 4, 6, 9, 12, 13, 18, 26, 36, 39, 52, 78, 117, 156, 234, 468
step = 78
overall_offset_x = step // 2
overall_offset_y = step // 2


width = 1
for index, y in enumerate(range(step * 6, size[1] - step, step)):
    x = 0
    x += step * 4
    draw.line((overall_offset_x + 0 + 10, overall_offset_y + y + step, overall_offset_x + x - 20, overall_offset_y + y + step), fill="gray", width=width)
    for x in range(x, size[0] - step, step):
        offset = 10
        x1 = x
        y1 = y + offset
        x2 = x + step - offset
        y2 = y + step
        draw.line((overall_offset_x + x1, overall_offset_y + y1, overall_offset_x + x2, overall_offset_y + y1), fill="gray", width=width)
        draw.line((overall_offset_x + x1, overall_offset_y + y2, overall_offset_x + x2, overall_offset_y + y2), fill="gray", width=width)
        draw.line((overall_offset_x + x1, overall_offset_y + y1, overall_offset_x + x1, overall_offset_y + y2), fill="gray", width=width)
        draw.line((overall_offset_x + x2, overall_offset_y + y1, overall_offset_x + x2, overall_offset_y + y2), fill="gray", width=width)

for index, x in enumerate(range(step * 4, size[0] - step, step)):
    y = 0
    y += step * 6
    draw.line((overall_offset_x + x, overall_offset_y + 0 + 10, overall_offset_x + x, overall_offset_y + y - 10), fill="gray", width=width)


del draw


output_image.save(output_path)
print(output_path + " saved.")
