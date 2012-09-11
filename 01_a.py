#!/usr/bin/env python

import string

url = "http://www.pythonchallenge.com/pc/def/map.html"

input = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

def translate_char(inchar):
    if inchar in string.lowercase:
        outchar = chr((ord(inchar) + 2 - ord('a') + 1) % len(string.lowercase) + ord('a') - 1)
    elif inchar in string.uppercase:
        outchar = chr((ord(inchar) + 2 - ord('A') + 1) % len(string.uppercase) + ord('A') - 1)
    else:
        outchar = inchar
    print "%s (%d) -> %s (%d)" % (inchar, ord(inchar), outchar, ord(outchar))
    return outchar

output = ''.join(map(translate_char, input))

print output

