#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/def/0.html"

if __name__ == "__main__":
    import utils

    print utils.update_url(url, utils.return_this, str(2**38))

