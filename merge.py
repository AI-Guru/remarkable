import sys
from PIL import Image, ImageOps, ImageMath

if len(sys.argv) != 3:
    print("USAGE: python merge.py TEMPLATE_PATH CONTENT_PATH")
    exit(0)

template_path = sys.argv[1]
content_path = sys.argv[2]
output_path = content_path.replace(".png", "-merged.png")

template_image = Image.open(template_path)
template_image = template_image.convert("RGBA")
content_image = Image.open(content_path)
content_image = content_image.convert("RGBA")

assert template_image.size == content_image.size, "Incompatible sizes: " + str(template_image.size) + " " + str(content_image.size)
size = template_image.size

mask_image = content_image.convert("RGB")
mask_image = ImageOps.invert(mask_image)
mask_image = mask_image.convert("RGBA")

output_image = Image.new("RGB", size, (255, 0, 0))
output_image.paste(template_image, (0, 0))
output_image.paste(content_image, (0, 0), mask=mask_image.split()[0])
output_image.save(output_path)
print(output_path + " saved.")
