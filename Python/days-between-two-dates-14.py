# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date

date1 = date(2014, 7, 1)
date2 = date(2014, 7 ,11)

difference = date2 - date1

print(difference)