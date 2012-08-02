#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/def/integrity.html"
title = "working hard?"
auth_popup_message = "inflate"
url2 = "http://www.pythonchallenge.com/pc/return/good.html"

if __name__ == "__main__":
    import bz2
    import re

    import utils

    pattern = re.compile(r"<!--\nun: '(.+)'\s+pw: '(.+)'")
    un, pw = re.findall(pattern, utils.wget(url))[0]
    #print un
    #print pw

    print "un: %s" % bz2.decompress(un.decode('string_escape'))
    print "pw: %s" % bz2.decompress(pw.decode('string_escape'))

