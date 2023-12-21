# Write a Python program to convert a string to datetime.
# Sample String : Jan 1 2014 2:43PM
# Expected Output : 2014-01-01 14:43:00

import datetime

string = "Jan 1 2014 2:43PM"

def convert(arg):
    format = '%b %d %Y %I:%M%p'
    datetime_converted = datetime.datetime.strptime(arg, format)

    return datetime_converted

print(convert(string))
