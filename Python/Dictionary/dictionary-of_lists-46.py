# Write a Python program to create a dictionary grouping a sequence 
# of key-value pairs into a dictionary of lists.
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

original_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

def groupingItems(arg):
    grouped = {}
    for key, value in arg:
        grouped.setdefault(key, []).append(value) 
    return grouped

print(f"Original list: {original_list}")
print(f"Grouped list: {groupingItems(original_list)}")
