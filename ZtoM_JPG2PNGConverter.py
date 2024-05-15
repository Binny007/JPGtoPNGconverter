# Exercise:  JPG to PNG Pokedex Converter

# --> We want a python script that can run when calling
# "python filename.py (then 2 arguments)"  where (a)first argument is I want to open
# the foldername(Pokedex/) and (b) Second parameter is new/ folder that i want to create

# --> So i want to run above commands and it looks through all the images in Pokedex
# and convert all images from JPG to PNG and save them in new/ folder


# Google and learn on how to use #sys module to grab the first and second argument,
# then google how to use #os module to grab the path (or the #pathlib module),
# so that the files in Pokedex to write to new/ file
# Then use Pillow module to convert the image to PNG


import sys
import os
from PIL import Image

# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exist, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through Pokedex/ and convert images to PNG
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')

# save to the new/ folder



