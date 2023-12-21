# Write a Python program to print all distinct values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

dict_list = [
    {"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
    {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}
    ]

print(f"Original list: {dict_list}")

distinct_values = set(value for dictionary in dict_list for value in dictionary.values())

print(f"Distinc values: {distinct_values}")