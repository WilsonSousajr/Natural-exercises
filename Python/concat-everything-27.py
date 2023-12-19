# Write a Python program that concatenates all elements in a list into a string and returns it.

list1 = ['H','e','l','l','o',' ','W','o','r','l','d','!']

def returnConcatenated(list):
    resul = ''.join(list)
    return resul

print(returnConcatenated(list1))