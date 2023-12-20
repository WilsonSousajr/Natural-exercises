# Write a Python program to remove all instances of a given value from a given array of integers and find the length of the newly created array.
# Sample Input:
# ([1, 2, 3, 4, 5, 6, 7, 5], 5)
# ([10,10,10,10,10], 10)
# ([10,10,10,10,10], 20)
# ([], 1)
# Sample Output:
# 6
# 0
# 5
# 0

list1 = [10,10,10,10,10]
value_to_remove = int(input(f"Enter a value to remove from the list {list1}: "))
print(f"Current list length: {len(list1)}")

def removeFromArray(list, value):
    if value in list:
        list.remove(value)
        removeFromArray(list, value)
        return True
    else:
        return False

if removeFromArray(list1, value_to_remove):
    print(f"New list length: {len(list1)}")
else:
    print("Error: the given value don't exist in the list.")




