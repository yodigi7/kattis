from PIL import Image
import os


def change_size(path_to_file, save_path_with_name):
    image = Image.open(path_to_file)
    size = width, height = image.size
    image = image.resize((220, 120))
    image.save(save_path_with_name)

for file in os.listdir()
change_size("testing_broken_1.png", "holder_file/testing_broken_1.png")