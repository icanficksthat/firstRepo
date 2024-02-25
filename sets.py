# 3. Sets:
#
# Pre: Describe in a few sentences what a set is in Python and why it's useful.

print('''
A set is similar to a list or tuple in that it is still a collection of items used to store 
information however, it does not show duplicate items contained within. This is useful for
if the user was only wanting to see what types of items were contained in the set and not all
occurances of the item repeated. It also has no order to it so the index() function would not
work on a set.
''')

# Explain and give an example of why we would use it instead of any of these other data structures.

print('''
As stated above we would use a set to see the different types of items in a list or tuple and
not all occurances of said items. An example is if we were had a collection of assorted fruits
and made a list of all the fruits contained, we may have 6 oranges, 3 bananas, 5 apples, and
10 strawberries but we only wanted to see the different types of fruits. We would use a set
and it would tell us orange, banana, apple and straberry.
''')

# a. Create two sets containing the numbers 1 to 5 and 4 to 8 respectively. Print both sets.

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1, set2)

# b. Find and print the intersection of the two sets.

setIntersec = set1.intersection(set2)
print(setIntersec)

# c. Find and print the union of the two sets.

setUnion = set1.union(set2)
print(setUnion)

# d. Add the number 9 to the first set. Print the updated set.

set1.add(9)
print(set1)

# e. Remove the number 6 from the second set. Print the updated set.

set2.remove(6)
print(set2)