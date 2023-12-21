# Write a Python program to get a list of dates between two dates.

from datetime import date, timedelta
import pandas

start_date = date(2023, 12, 1)
end_date = date(2024, 1, 1)

list_of_dates = pandas.date_range(start_date, end_date - timedelta(days=1), freq='d')

print(list_of_dates)