# Write a Python program to get the date of the last Tuesday.

from datetime import datetime, timedelta

today = datetime.today()
difference = (today.weekday() - 1) % 7
last_tuesday = today - timedelta(days=difference)

print(last_tuesday)