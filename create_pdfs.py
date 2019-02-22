import os
import glob


source_directory = "templates-custom"
destination_directory = "templates-custom-pdf"

if os.path.exists(destination_directory) == False:
    os.mkdir(destination_directory)

png_paths = glob.glob(os.path.join(source_directory, "*.png"))
for png_path in png_paths:
    print("Converting  {}...".format(png_path))
    pdf_path = png_path.replace(".png", ".pdf")
    shell_command = "convert -quality 100 -density 50"
    for _ in range(12):
        shell_command += " " + png_path
    shell_command += " " + pdf_path
    print(shell_command)
    os.system(shell_command)
    print("")
