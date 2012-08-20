#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/return/bull.html"
title = "what are you looking at?"

a = [1, 11, 21, 1211, 111221]
target_index = 30
        
if __name__ == "__main__":
    import utils

    while len(a) <= target_index + 1:
        a.append(utils.look_and_say(a[-1]))

    print utils.update_url(url, utils.return_this, str(len(str(a[target_index]))))

