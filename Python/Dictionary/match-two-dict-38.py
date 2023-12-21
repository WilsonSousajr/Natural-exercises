# Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

for key in dict1:
    if key in dict2:
        if dict1.get(key) == dict2.get(key):
            print(f"{key}: {dict1.get(key)} is present in both x and y")