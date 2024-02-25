# 2. Tuples:
#
# Pre: Explain in a few sentences what a tuple is in Python and how it differs from a list.

print('''
"A tuple is similar to a list in which it is a collection of items used to store information.
However, it differs by the fact that the user is immutable and uses () instead of []. 
''')
       
# Explain and give an example of why we would use it instead of a list.

print('''
We would use a tuple instead of a list if we want all of the set of values to stay constant.
For example: if we wanted to contain all of the years between the birth of our dear lord and 
savior Jesus Christ and now.
''')

# a. Create a tuple containing the days of the week (Monday, Tuesday, Wednesday, etc.). Print the tuple.

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
print(days)

# b. Access and print the third element of the tuple.

print(days[2])

# c. Convert the tuple to a list. Print the list.

daysList = list(days)
print(daysList)

# d. Check if "Sunday" is in the tuple. Print True or False accordingly.

if "Sunday" in days:
    print("True")
else:
    print("False")

# e. Find the index of "Thursday" in the tuple. Print the index.
    
thursdaysPos = days.index("Thursday")
print(thursdaysPos)