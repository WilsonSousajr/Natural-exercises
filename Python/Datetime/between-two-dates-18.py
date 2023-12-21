# Write a Python program to get days between two dates.
# Sample Dates : 2000,2,28, 2001,2,28
# Expected Output : 366 days, 0:00:00

from datetime import date

date1 = date(2000, 2, 28)
date2 = date(2001, 2, 28)

difference = date2 - date1
print(f"The amount of days between {date1} and {date2} is {difference.days}")