#!/usr/bin/env python

import re
import string

import utils

url = "http://www.pythonchallenge.com/pc/def/ocr.html"

if __name__ == "__main__":
    text_pattern = re.compile(
            r'<!--\nfind rare characters in the mess below:\n-->\n\n<!--\n(.*?)\n-->', 
            re.DOTALL)
    text = re.search(text_pattern, utils.wget(url)).group(1)

    new_filename = ''
    for char in text:
        if char in string.letters:
            new_filename += char

    print utils.update_url(url, utils.return_this, new_filename)

