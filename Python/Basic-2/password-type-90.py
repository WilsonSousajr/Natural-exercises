# Write a Python program that replaces all but the last five characters of a string with "*" and returns the modified string.
# Original String: kdi39323swe
# new string: ******23swe
# Original String: 12345abcdef
# new string: ******bcdef
# Original String: 12345
# new string: 12345

originalString = input("Enter a string:")
n = 5
lastNCharacters = originalString[-n:]
firstCharacters = originalString[:n]

def replaceCharacters(string, key):
    for letter in string:
        string = string.replace(letter, key)
    return string

modifiedCharacters = replaceCharacters(firstCharacters, '*')
newString = modifiedCharacters + lastNCharacters

print(f"Original string: {originalString}\nNew string: {newString}")
