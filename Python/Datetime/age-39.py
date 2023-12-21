# Write a Python program to calculate an age in years

from datetime import date, datetime

def calculateAge(born_date):
    today = date.today()
    age = today.year - born_date.year - ((today.month, today.day) < (born_date.month, born_date.day))

    return age

print(calculateAge(date(2005,11,21)))