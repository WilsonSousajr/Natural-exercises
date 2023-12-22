# Write a Python program that accepts a sequence of comma-separated numbers from the user 
# and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

import re

numbers = input("Enter a sequence of comma-separated numbers:")
pattern = re.compile(r"^[0-9]+(,[0-9]+)+$")

def isValid(input_string):
    if pattern.match(input_string) == None:
        return False
    else:
        return True

while isValid(numbers) == False:
    print("Invalid format.")
    numbers = input("Enter a sequence of comma-separated numbers:")

numbers_list = numbers.split(',')
numbers_tuple = tuple(numbers.split(','))
print(f"List: {numbers_list}\n Tuple: {numbers_tuple}")




 





