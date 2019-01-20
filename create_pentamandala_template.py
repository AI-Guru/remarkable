from PIL import Image, ImageDraw
import os
import math

size = (1404, 1872)
center = (1404 // 2, 1872 // 2)


output_path = os.path.join("templates-custom", "pentamandala.png")
output_image = Image.new("RGB", size, "white")

draw = ImageDraw.Draw(output_image)

circle_descriptions = []
pentagon_descriptions = []
for index, radius in enumerate(range(0, 3000, 50)):
    ellipse_shape = (center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius)
    width = 1
    if index % 5 == 0:
        pentagon_descriptions.append((radius, width))
        width = 2
    circle_descriptions.append((radius, width))

for (radius, width) in circle_descriptions:
    ellipse_shape = (center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius)
    draw.ellipse(ellipse_shape, outline="gray", width=width)

for (radius, width) in pentagon_descriptions:
    xy = []
    print(width)
    for index in range(5):
        angle = index * 360.0 / 5.0
        offset = (int(radius * math.sin(math.radians(angle))), int(radius * math.cos(math.radians(angle))))
        x = center[0] + offset[0]
        y = center[1] + offset[1]
        xy.append((x, y))
    print(xy)
    draw.polygon(xy, outline="gray")


# L
line_descriptions = []
segments = 5
segments_offset = 360.0 / (5.0 * segments)
for index in range(5):
    angle = index * 360.0 / 5.0
    width = 3
    line_descriptions.append((angle, width))

    width = 1
    for segment in range(1, segments):
        line_descriptions.append((angle + segment * segments_offset , width))


for (angle, width) in line_descriptions:
    offset = (int(3000 * math.sin(math.radians(angle))), int(3000 * math.cos(math.radians(angle))))
    x1 = center[0]
    y1 = center[1]
    x2 = center[0] + offset[0]
    y2 = center[1] + offset[1]
    if index % 3 == 0:
        width = 2
    if index % 9 == 0:
        width = 3
    draw.line((x1, y1, x2, y2), fill="gray", width=width)

del draw
output_image.save(output_path)
print(output_path + " saved.")
