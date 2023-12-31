# Write a Python program to convert the date to datetime (midnight of the date) in Python.
# Sample Output : 2015-06-22 00:00:00

from datetime import date, datetime

today = date.today()
print(datetime.combine(today, datetime.min.time()))