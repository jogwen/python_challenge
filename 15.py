#!/usr/bin/env python

url = "http://www.pythonchallenge.com/pc/return/cat.html"
title = "uzi"
screen_text = "and its name is uzi. you'll hear from him later."

url = "http://www.pythonchallenge.com/pc/return/uzi.html"
title = "whom?"
screen_text1 = "he ain't the youngest, he is the second"
screen_text2 = "todo: buy flowers for tomorrow"

if __name__ == "__main__":
    import datetime
    print [leapyear 
        for leapyear in range(2000, 0, -4) 
        if datetime.date(leapyear, 1, 1).weekday() == 3 and str(leapyear)[-1] == "6"
    ][1]
