#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/def/oxygen.html"

def is_gray(four_tuple):
    return four_tuple[0] == four_tuple[1] == four_tuple[2]

if __name__ == "__main__":
    from PIL import Image
    import re

    image = Image.open('/tmp/oxygen.png')
    pixels = image.getdata()
    #print [p[0] for p in pixels if p[0]==p[1]==p[2]]
    width = image.size[0]
    gray_values = []
    for pixel in pixels:
        if is_gray(pixel):
            if not gray_values or gray_values[-1] != pixel[0]:
                gray_values.append(pixel[0])
            
    output = ''.join(map(chr, gray_values))
    print output

    list_pattern = re.compile(r'(\[\d+(?:, \d+)*\])')
    l = eval(re.search(list_pattern, output).group(1))
    print l
    print ''.join(map(chr, l))

