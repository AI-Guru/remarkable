from PIL import Image, ImageDraw, ImageFont
import os
import math

size = (1404, 1872)
center = (1404 // 2, 1872 // 2)


output_path = os.path.join("templates-custom", "goalplanning.png")
output_image = Image.new("RGB", size, "white")

draw = ImageDraw.Draw(output_image)


def draw_todo(x, y):
    rectangle_size = 50
    draw.rectangle((x, y, x + rectangle_size, y + rectangle_size), outline="gray")
    draw.line((x + rectangle_size + 25, y + rectangle_size, x + rectangle_size + 550, y + rectangle_size), fill="gray", width=1)


def draw_planner(x, y, number):

    for i in range(number):
        #y = i * 100 + 125
        draw_todo(x, y + i * 100 + 125)

    #y += 100

    #rectangle_width = 600
    #rectangle_height = 600

#font_path = "/Library/Fonts/Times New Roman.ttf"
font_path = "/Users/tristanbehrens/Library/Fonts/GARA.TTF"
font = ImageFont.truetype(font_path, 50)
def draw_text(text, x, y, line_length=None):
    draw.text((x, y), text, font=font, fill="black")
    if line_length != None:
        line_offset = 125
        draw.line((x + line_offset, y + 50, x + line_offset + line_length, y + 50), fill="gray", width=1)

# Here comes the real thing.

# Draw the goal text.
text = "Goal:"
x = 50
y = 100
draw_text(text, x, y, 1175)

# Draw the goal dates text.
y += 100
for x, text in zip([50, center[0] + 50], ["Start:", "End:"]):
    draw_text(text, x, y, 475)


# Draw Todos
text = "Todos:"
x = 50
y += 150
draw_text(text, x, y)
y -= 25
number_of_todos = 10
for x in [50, center[0] + 50]:
    draw_planner(x, y, number_of_todos)

# Draw Todos
text = "Success criteria:"
x = 50
y += 125 * number_of_todos - 50
draw_text(text, x, y)
y -= 25
number_criteria = 2
for x in [50, center[0] + 50]:
    draw_planner(x, y, number_criteria)


#draw.line((center[0], 25, center[0], size[1] - 25), fill="gray", width=1)

#draw.rectangle((50, 50, size[0] - 50, 100), outline="gray")



del draw

output_image.save(output_path)
print(output_path + " saved.")
