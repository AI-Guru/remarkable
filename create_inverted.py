import os
import glob


source_directory = "templates-custom"
destination_directory = "templates-custom"

png_paths = glob.glob(os.path.join(source_directory, "*.png"))
png_paths = [path for path in png_paths if "_inverted" not in path]
for png_path in png_paths:
    print("Converting  {}...".format(png_path))
    output_path = png_path.replace(".png", "_inverted.png")

    shell_command = ""
    shell_command += "convert "
    shell_command += png_path
    shell_command += " -channel RGB -negate "
    shell_command += output_path
    print(shell_command)
    os.system(shell_command)
    print("")
