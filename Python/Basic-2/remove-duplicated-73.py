# 73. Write a Python program that removes duplicate elements from a given array of numbers 
# so that each element appears only once and returns the new length of the array.
# Sample Input:
# [0,0,1,1,2,2,3,3,4,4,4]
# [1, 2, 2, 3, 4, 4]
# Sample Output:
# 5
# 4

list1 = [0,0,1,1,2,2,3,3,4,4,4]

print(f"Old list: {list1}\nOld length: {len(list1)} ")

unDuplicated = set(list1)

print(f"New list: {unDuplicated}\nNew length: {len(unDuplicated)}")