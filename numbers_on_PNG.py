"""
TEXT_TO_IMAGE
Authors: Subbotin Grigory, WirelessM8

This program must be used to create ASCII art from a simple image.

Enjoy)

"""
from PIL import Image, ImageFont, ImageDraw
from random import randint, choice
from math import sqrt, pi

import colorsys

# Grayscale to Ascii character map
Gray2Ascii = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,`'. "


# Current length is 68

#Some number generator
def num_generator(x, y, hsv, mode, **kwargs):
    if mode == 0:
        char = 2 ** randint(x, y)
    if mode == 1:
        # Brightness is expecting to be in 0-255 range, so to fit the charmap it is divided by 4
        char = Gray2Ascii[hsv[2] // 4]
    if mode == 2:
        char = 2 ** (int(hsv[1]*8)+4)
    return str(char)

#RGB color generator
def rgb_random(min, max):
    r = randint(min, max)
    g = randint(min, max)
    b = randint(min, max)
    return [r, g, b]


#Image resizer
def image_sizer(input_path,output_path,width_new, height_new,size, x, y,):
    image = Image.open(input_path)
    image_new = Image.new("RGB", (width_new,height_new), "black")
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    draw = ImageDraw.Draw(image_new)
    step = 1
    bias = image.size 
    for i in range(0,width,step):
        for j in range(0,height,step):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            draw.line((i,j//2)+bias, fill = (r,g,b))
    image_new.save(output_path)
    image_new.show()

#Imgae modifier
def image_mod(input_path, output_path, font, **kwargs):
    # Setting up function config
    size = 12
    resolution_coeff = 1
    font_spacing = 1
    randomness = 0
    mode = 0
    bw = 0
    for key, value in kwargs.items():
        if key == 'resolution':
            resolution_coeff = value
        if key == 'fontspacing':
            font_spacing = value
        if key == 'jitter':
            randomness = int(value)
        if key == 'mode':
            if value == "number_color":
                mode = 2
            if value == "ascii":
                mode = 1
            if value == "number":
                mode = 0
        if key == 'bw':
            bw = value
        if key == 'fontsize':
            size = value
    # Setting up file config
    image = Image.open(input_path)
    width = image.size[0]
    height = image.size[1]
    image_new = Image.new("RGB",
                          (int(width * resolution_coeff * font_spacing), int(height * resolution_coeff * font_spacing)),
                          "black")
    pix = image.load()
    draw = ImageDraw.Draw(image_new)
    font = ImageFont.truetype(font, size)

    # Defining step for each pixel in input image
    step = round(size * pi / 1.7 / resolution_coeff)
    for i in range(0, width, step // 2):
        for j in range(0, height, step // 2):
            r, g, b = pix[i, j]
            hsv = colorsys.rgb_to_hsv(r, g, b)

            if bw == 1:
                r, g, b = colorsys.hsv_to_rgb(hsv[0], 0, hsv[2])

            if bw == 2:
                r, g, b = 255, 255, 255
            text_pos = (i * resolution_coeff * font_spacing + randint(-randomness, randomness),
                        j * resolution_coeff * font_spacing + randint(-randomness, randomness))
            draw.text(text_pos, (num_generator(4, 9, hsv, mode)), font=font, fill=(r, g, b))
    image_new.save(output_path)
    image_new.show()

#main function 
#@username@ choocing edit mode and use this mode on image

if __name__ == "__main__":
    # kwargs are all optional
    # resolution 1 is by default, modifying resolution (obviously)
    # fontsize , 12 by default, optional too (bigger fontsize lowers count of symbols)
    # fontspacing, 1 by default, modifies distance between symbols, changes final resuliton too 1 is default
    # jitter, a coeff for randomness of symbol position
    # mode, ascii or numbers, default is numbers, ascii uses hsv brightness
    # bw - blackwhite mode, 0 for full color, 1 for black and white, 2 for white symbols only
    # examples
    #image_sizer("putin.png", "output_3.png",3840 ,2160, 4, 0, 0)
    # image_mod("input.png", "output.png", "numbers_1024.ttf")
    #image_mod("input.png", "output.png", "numbers_1024.ttf",mode = 'ascii')
    #image_mod("input.png", "output.png", "numbers_1024.ttf", mode='ascii', fontspacing=0.7, resolution=2, bw=2)
    image_mod("input1.png", "output.png","numbers_1024.ttf", fontsize = 10, resolution = 0.5, fontspacing = 2, jitter = 0, mode = "number_color")