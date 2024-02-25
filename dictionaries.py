# 4. Dictionaries:
#
# Pre: Explain in a few sentences what a dictionary is in Python and why it's useful.

print('''
A dictionary is a an ordered collection of values, used to store a collection of values
using a key-value pair. This is useful because sometimes a key may contain a list with
lots of values and it may be easier to reference the key in the dictionary rather than
all of the values contained within said key.
''')

# Explain and give an example of why we would use it instead of any of these other data structures.

print('''
If were creating a program for a car manufacturer to input info of different vehicles they had
it would be more useful to use a dictionary. For example: the year, make, and model would be
the keys in this instance.
''')

# a. Create a dictionary representing a student's grades in different subjects (e.g., Math: 85, Science: 90, etc.). Print the dictionary.

dict1 = {
    "Math": 93,
    "Science": 86,
    "English": 79
}
print(dict1)

# b. Add a new subject and grade to the dictionary. Print the updated dictionary.

dict1["History"] = 83
print(dict1)

# c. Remove a subject and its corresponding grade from the dictionary. Print the updated dictionary.

del dict1["English"]
print(dict1)

# d. Check if "Math" is a key in the dictionary. Print True or False accordingly.

if "Math" in dict1:
    print("True")
else:
    print("False")

# e. Print all the subjects for which the student has grades, one subject per line.
    
for key in dict1:
    print(key)