# 1. Lists:
#
# Pre: Describe in a few sentences what a list is in Python and why it's useful.

print('''
A list is an ordered colleciton of items used to store information.
The information can be accessed and modified by index which is very quick.
It's useful becuase we can store multiple items in a single variable.
''')
 
#
# a. Create a list containing the numbers from 1 to 10. Print the list.

nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)

# b. Add the number 11 to the end of the list. Print the updated list.

nums.append(11)
print(nums)

# c. Remove the number 3 from the list. Print the updated list.

nums.remove(3)
print(nums)

# d. Check if the number 5 is present in the list. Print True or False accordingly.

if 5 in nums:
    print("True")
else:
    print("False")

# e. Sort the list in descending order. Print the sorted list.
    
nums.sort(reverse=True)
print(nums)