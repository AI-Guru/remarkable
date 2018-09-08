from PIL import Image, ImageDraw
import os
import math

size = (1404, 1872)
center = (1404 // 2, 1872 // 2)


output_path = os.path.join("templates-custom", "todos.png")
output_image = Image.new("RGB", size, "white")

draw = ImageDraw.Draw(output_image)


def draw_todo(x, y):
    rectangle_size = 50
    draw.rectangle((x, y, x + rectangle_size, y + rectangle_size), outline="gray")
    draw.line((x + rectangle_size + 25, y + rectangle_size, x + rectangle_size + 550, y + rectangle_size), fill="gray", width=1)


def draw_planner(x):

    for i in range(17):
        y = i * 100 + 125
        draw_todo(x, y)


draw.line((center[0], 25, center[0], size[1] - 25), fill="gray", width=1)

draw_planner(50)
draw_planner(center[0] + 50)

del draw

output_image.save(output_path)
print(output_path + " saved.")
