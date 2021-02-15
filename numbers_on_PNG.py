from PIL import Image, ImageFont, ImageDraw
from random import randint, choice
from math import sqrt, pi

def num_generator(x, y):
    num = randint(x, y)
    return str(2**num)

def color_generator():
    r = randint(70,255)
    g = randint(70, 255)
    b = randint(70, 255)
    return r, g, b

def text(output_path,width, height , x, y, n, size):
    image = Image.new("RGB", (width,height), "black")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("numbers_1024.ttf", size)
    for j in range(n):
        for i in range(n):
            draw.text((x,y), (num_generator(2,12)), font = font, fill = (color_generator()))
            y = y + (size+(size//3))
        x = x + (size * 3 )
        y = 1
    image.save(output_path)
    image.show()

def image_mod(input_path,output_path,width_new, height_new,size, x, y,):
    image = Image.open(input_path)
    image_new = Image.new("RGB", (width_new,height_new), "black")
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    draw = ImageDraw.Draw(image_new)
    font = ImageFont.truetype("1298.ttf", size)
    step = round(size*pi/1.75)
    for i in range(0,width,step):
        for j in range(0,height,step):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            draw.text((i,j//3), (num_generator(4,9)), font = font, fill = (r,g,b))
    image_new.save(output_path)
    image_new.show()

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
            draw.line((i,j)+bias, fill = (r,g,b))
    image_new.save(output_path)
    image_new.show()

if __name__ =="__main__":
    #text("text.png",width = 2160, height = 3840, x = 1, y = 1, n = 180, size = 8)
    #image_mod("putin.png", "output_5.png",3840 ,2160, 4, 0, 0)
    #image_sizer("input1.png", "output_3.png",3840 ,2160, 4, 0, 0)
