#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/return/5808.html"
url_image = "http://www.pythonchallenge.com/pc/return/cave.jpg"
title = "odd even"

if __name__ == "__main__":
    from PIL import Image
    import utils

    im = Image.open('cave.jpg', 'r')
    width, height = im.size
    pix = im.load()
    for y in range(height):
        for x in range(width):
            if (utils.is_even(y) and utils.is_odd(x)) or (utils.is_odd(y) and utils.is_even(x)): pix[x, y] = (0, 0, 0)
    im.save('cave2.jpg', 'jpeg')

