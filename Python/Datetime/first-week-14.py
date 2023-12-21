# Write a Python program to find the date of the first Monday of a given week.
# Sample Year and week : 2015, 50
# Expected Output : Mon Dec 14 00:00:00 2015

import time

year_and_week = '2015 50 1'
print(time.asctime(time.strptime(year_and_week, '%Y %W %w')))
