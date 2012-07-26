#!/usr/bin/env python

import re
import string

import utils

url = "http://www.pythonchallenge.com/pc/def/equality.html"

def get_horizontal_matches(textlines, letter_pattern):
    coords = []
    # No letter in first/last 3 lines could have exactly 3 capitals above/below so ignore them
    line_number = 3
    for line in textlines[3:-3]:
        for match in re.findall(letter_pattern, line):
            char_index = line.find(match) + 4 
            coords.append((line_number, char_index))
        line_number += 1
    return coords

def get_vertical_matches(textlines, horizontal_match_coords):
    coords = []
    for l, c in horizontal_match_coords:
        for d in range(1, 4):
            if not textlines[l-d][c] in string.uppercase:
                continue
        if l > 3:
            if textlines[l-4] in string.uppercase:
                continue
        if l < len(textlines) - 3:
            if textlines[l+4] in string.uppercase:
                continue
        coords.append((l, c))
    return coords


if __name__ == "__main__":
    secret_text_pattern = re.compile(r'<!--\n(.*?)\n-->', re.DOTALL)
    text = re.search(secret_text_pattern, utils.wget(url)).group(1)

    textlines = text.split('\n')
    letter_pattern = re.compile(r'(?:^|[^A-Z])[A-Z]{3}[a-z][A-Z]{3}(?:[^A-Z]|$)')
    horizontal_matches = get_horizontal_matches(textlines, letter_pattern)
    vertical_matches = get_vertical_matches(textlines, horizontal_matches)
    new_filename = ''
    for l, c in vertical_matches:
        new_filename += textlines[l][c]
    print utils.update_url(url, utils.return_this, new_filename)

