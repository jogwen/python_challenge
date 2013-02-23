from PIL import Image


def swap(line):
    i=0
    while line[i] != 195:
        i += 1
    return line[i:] + line[:i]


im = Image.open("mozart.gif")

for y in range(im.size[1]):
    line = [im.getpixel((x,y)) for x in range(im.size[0])]
    line = swap(line)
    for x in range(im.size[0]):
        im.putpixel((x,y), line[x])

im.save('16.gif')
