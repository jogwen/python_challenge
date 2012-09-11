#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/def/oxygen.html"

def is_gray(four_tuple):
    return four_tuple[0] == four_tuple[1] == four_tuple[2]

if __name__ == "__main__":
    from itertools import izip_longest
    from PIL import Image
    import re

    import utils

    image = Image.open('/tmp/oxygen.png')
    pixels = image.getdata()
    width = image.size[0]
    pixel_lines = izip_longest(*[iter(pixels)]*width)
    for line in pixel_lines:
        if is_gray(line[0]):
            break
    #print [p[0] for p in line]
    output = ''.join(map(chr, [p[0] for p in line[::7]]))
    #print output

    list_pattern = re.compile(r'(\[\d+(?:, \d+)*\])')
    l = eval(re.search(list_pattern, output).group(1))
    #print l
    print utils.update_url(url, utils.return_this, ''.join(map(chr, l)))

