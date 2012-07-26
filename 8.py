#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/def/integrity.html"

if __name__ == "__main__":
    import re

    import utils

    pattern = re.compile(r"<!--\nun: '(.+)'\s+pw: '(.+)'")
    un, pw = re.findall(pattern, utils.wget(url))[0]
    print un
    print pw

