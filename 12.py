#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/return/evil.html"
url_image = "http://www.pythonchallenge.com/pc/return/evil1.jpg"
download_file = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
title = "dealing evil"

# Solved with the aid of hints from http://unixwars.com/2007/09/18/python-challenge-level-12-dealing-evil/

if __name__ == "__main__":
    fh = open('evil2.gfx', 'rb')
    data = fh.read()
    fh.close()

    filenames = ('file1', 'file2', 'file3', 'file4', 'file5')
    filehandlers = map(open, filenames, ('wb',)*5)
    for i in range(5):
        fh = filehandlers[i]
        fh.write(data[i::5])
        fh.close()

