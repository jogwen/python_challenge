#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/def/peak.html"
url = "http://www.pythonchallenge.com/pc/def/banner.p"

if __name__ == "__main__":
    import pickle
    import sys
    import utils

    data = pickle.loads(utils.wget(url))
    # Got help from below in recongnising data as a run length encoding!
    # http://unixwars.com/2007/09/11/python-challenge-level-5-peak-hell/
    for line in data:
        print ''.join(map(lambda pair: pair[0]*pair[1], line))

