#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/def/map.html"

def apply_translation(s1, trantab):
    return s1.translate(trantab)

if __name__ == "__main__":
    import string
    import utils

    instring = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

    trantab = string.maketrans(string.lowercase, string.lowercase[2:] + string.lowercase[:2])
    #print instring.translate(trantab)
    print utils.update_url(url, apply_translation, trantab)

