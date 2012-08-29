#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/return/disproportional.html"
title = "call him"
screen_text = "phone that evil"

url1 = "http://www.pythonchallenge.com/pc/phonebook.php"


if __name__ == "__main__":
    import xmlrpclib

    import utils

    phonebook = xmlrpclib.ServerProxy(url1)
    print utils.update_url(url, utils.return_this, phonebook.phone('Bert').strip('5-').lower())

