#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/return/italy.html"
title = "walk around"
comment = "remember: 100*100 = (100+99+99+98) + (..."

img1 = "http://www.pythonchallenge.com/pc/return/italy.jpg"
img2 = "http://www.pythonchallenge.com/pc/return/wire.png"

auth = ("huge", "file")

if __name__ == "__main__":
    from PIL import Image
    import requests
    from StringIO import StringIO

    wire = requests.get(img2, auth=auth)

    input_im = Image.open(StringIO(wire.content), 'r')
    input_width, input_height = input_im.size
    pixel_count = input_width * input_height
    input_pix = input_im.load()
    
    side_length = 100
    output_im = Image.new('RGB', (side_length, side_length), (255, 255, 255))
    output_pix = output_im.load()

    def get_side_lengths(side_length):
        return (side_length, side_length-1, side_length-1, side_length-2)

    directions = [
        [1, 0], # right
        [0, 1], # down
        [-1, 0], # left
        [0, -1] # up
    ]
    count = 0
    instructions = []
    while count < pixel_count:
        side_lengths = get_side_lengths(side_length)
        count += sum(side_lengths)
        instructions.extend(zip(directions, side_lengths))
        side_length -= 2

    x, y = -1, 0
    count = 0
    for i in range(pixel_count):
        if count == 0: 
            direction, limit = instructions.pop(0)
        x += direction[0]
        y += direction[1]
        output_pix[x, y] = input_pix[i, 0]
        count += 1
        if count == limit:
            count = 0

    output_im.save('spiral.png')
