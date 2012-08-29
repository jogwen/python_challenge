#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/return/italy.html"
title = "walk around"
comment = "remember: 100*100 = (100+99+99+98) + (..."

img1 = "http://www.pythonchallenge.com/pc/return/italy.jpg"
img2 = "http://www.pythonchallenge.com/pc/return/wire.png"


if __name__ == "__main__":
    import math
    from PIL import Image

    input_im = Image.open('wire.png', 'r')
    input_width, input_height = input_im.size
    pixel_count = input_width * input_height
    input_pix = input_im.load()
    
    output_width = 100
    output_im = Image.new('RGB', (output_width, int(math.ceil(float(pixel_count)/output_width))), (255, 255, 255))
    output_pix = output_im.load()
    for i in range(pixel_count): 
        x, y = fold_into_coordinates(i, output_width) 
        output_pix[x, y] = input_pix[i, 0]
    output_im.save('spiral.png')
