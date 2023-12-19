# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

from datetime import datetime 

current_time = datetime.now()
current_time = current_time.replace(microsecond=0)

print(f"Current date and time:\n {current_time}")