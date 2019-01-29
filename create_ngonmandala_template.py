from PIL import Image, ImageDraw
import os
import math

size = (1404, 1872)
center = (1404 // 2, 1872 // 2)

def render(edges, segments):
    output_path = os.path.join("templates-custom", "ngonmandala{}.png".format(edges))
    output_image = Image.new("RGB", size, "white")

    draw = ImageDraw.Draw(output_image)

    pentagon_descriptions = []
    radius = 75
    while radius < size[1] // 1.75:
        width = 1
        pentagon_descriptions.append((radius, width))
        radius = radius / math.cos(math.radians(180.0 /  edges))


    for (radius, width) in pentagon_descriptions:

        # Render the circle.
        ellipse_shape = (center[0] - radius + 1, center[1] - radius + 1, center[0] + radius - 1,  center[1] + radius - 1)
        draw.ellipse(ellipse_shape, outline="gray", width=width)

        # Render the polygon.
        xy = []
        for index in range(edges):
            angle = index * 360.0 / float(edges)
            offset = (int(radius * math.sin(math.radians(angle))), int(radius * math.cos(math.radians(angle))))
            x = center[0] + offset[0]
            y = center[1] + offset[1]
            xy.append((x, y))
        draw.polygon(xy, outline="gray")


    # L
    line_descriptions = []
    #segments = 10
    segments_offset = 360.0 / (edges * segments)
    for index in range(edges):
        angle = index * 360.0 / edges
        width = 2
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
        #if index % 3 == 0:
        #    width = 2
        #if index % 9 == 0:
        #    width = 3
        draw.line((x1, y1, x2, y2), fill="gray", width=width)

    del draw
    output_image.save(output_path)
    print(output_path + " saved.")

edges_list = [4, 5, 6, 7]
segments_list = [16, 10, 6, 7]
for edges, segments in zip(edges_list, segments_list):
    render(edges, segments)
