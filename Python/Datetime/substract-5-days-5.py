# Write a Python program to subtract five days from the current date.
# Sample Date :
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17

from datetime import date, timedelta

five_days_before = date.today() - timedelta(days=5)
print(f"Current Date: {date.today()}\n5 days before Current Date: {five_days_before}")