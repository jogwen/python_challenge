#!/usr/bin/env python

import re
import string

import utils

url = "http://www.pythonchallenge.com/pc/def/linkedlist.html"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

if __name__ == "__main__":
    value_pattern = re.compile(r'and the next nothing is (\d+)')

    this_value = url[-5:]
    count = 0;
    while count <= 400:
        source = utils.wget(url)
        print "%d: %s" % (count, source)
        mo = re.search(value_pattern, source)
        if mo:
            next_value = mo.group(1)
        elif source.find('Divide by two') >= 0:
            next_value = str(int(this_value) / 2)
        else:
            break
        url = url.replace(this_value, next_value)
        this_value = next_value
        count += 1

    print utils.update_url(url, utils.return_this, source)

