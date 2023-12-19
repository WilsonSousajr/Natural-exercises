# Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False



list1 = [1, 5, 8 ,3]
value = input("Enter a value(number): ")

def isNumber(value):
    try:
        checkedValue = int(value)
        if(checkedValue in list1):
            print("True")
        else:
            print("False")
    except ValueError:
        string = input("Enter a value(number): ")
        isNumber(value)

isNumber(value)
