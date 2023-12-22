# Write a Python program that prints out all colors from color_list_1 that are 
# not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

notIn = color_list_1 - color_list_2
print(notIn)
