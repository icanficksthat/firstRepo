print('''
1. Typecasting Concepts:
Typecasting is a way to convert the value of different data types like int, str and float
into another data type. This is important for being able to combine different data
types with each other and so that the code works. Like converting an int to a str
or vice versa.

Implicit typecasting is python automatically deciding the type the resulting data 
needs to be for the code to work like adding an int to a float.
An example is :
num1 = 56
num2 = 12.67
print(num1 + num2)
''')
num1 = 56
num2 = 12.67
print(num1 + num2)
print('''
num1 is an int and num2 is a float but python automatically recognizes the resulting 
code needs to print as a float.

Explicit typecasting is where the programmer needs to explicitly state what type the
resulting data type needs to be to add two different data types together like str and
int.
An example is:
num3 = "55"
num4 = 37
print(int(num3) + num4)
''')
num3 = "55"
num4 = 37
print(int(num3) + num4)
print('''
num3 in this scenario is a str and needs to be converted to an int using int(num3) to
be able to add to num4 and get a resulting int. This can also be done the other way
around using str(num4) if i wanted to get a str as the result which would be 5537.
Typecasting would come up in things like my dungeon game trying to add the str 
"Your health is" and the int "5" to get the resulting str "Your health is 5". 
''')

print('2. Typecasting Operations:')
print('''
def intToStr(integer):
    return str(integer)
num5 = input("Provide an integer.  ")
strOfInt = intToStr(num5)
print(strOfInt, type(strOfInt)) #added type() to check work
''')
def intToStr(integer):
    return str(integer)
num5 = input("Provide an integer.  ")
strOfInt = intToStr(num5)
print(strOfInt, type(strOfInt)) #added type() to check work

print('''
def strToInt(string):
    return int(string)
str1 = "901"
intOfStr = strToInt(str1)
print(intOfStr, type(intOfStr))
''')
def strToInt(string):
    return int(string)
str1 = "901"
intOfStr = strToInt(str1)
print(intOfStr, type(intOfStr))

print('''
try:
    num1thru5 = [1,2,3,4,5]
    print(num1thru5[5])
except:
    print("That is not a value in the index.")
''')
def floatToInt(float):
    return int(float)
float1 = 7/3
intOfFloat = floatToInt(float1)
print(intOfFloat, type(intOfFloat))

print('''
3. Exception Handling:
An exception error is when the code is syntactically correct (meaning there is no issues
with syntax like missing a paranthesis) but an error occurs during execution.
Exception handling is code in a program that helps bypass any errors that might occur as
the program runs. This is important because the user of the program may input information
that would cause an exception error to occur and render the program inoperable from that
point on.
ArithmeticError: A base class for exceptions that are raised as a result of arithmetic 
errors, such as division by zero.
TypeError: An exception that is raised when an operation is performed on an object of 
the wrong type like when concatinating strings to integers.
ImportError: An exception that is raised when the program is unable to find an operation
from another program like a function that I created in another program.
      
4. Handling Exceptions:
try:
    num1thru5 = [1,2,3,4,5]
    print(num1thru5[5])
except:
    print("That is not a value in the index.")
''')
try:
    num1thru5 = [1,2,3,4,5]
    print(num1thru5[5])
except:
    print("That is not a value in the index.")

print('''
try:
    openFile = open('stuff.py')
    print(openFile)
except:
    print("File not found.")
''')
try:
    openFile = open('stuff.py')
    print(openFile)
except:
    print("File not found.")

print('''
dic = {
    "k1":43,
    "k2":77,
    "k3":"stuff"
}
try:
    print(dic["k4"])
except:
    print("Key not found in directory.")
''')
dic = {
    "k1":43,
    "k2":77,
    "k3":"stuff"
}
try:
    print(dic["k4"])
except:
    print("Key not found in directory.")

print('''
5. Application of Typecasting and Exceptions:
If the input from a user was in string format, like in the sentence "I have 3 apples."
but I only wanted the number of the apples to add to another number of apples, I could
write a try/except clause for if the user input anything but an integer. In the try portion
I could have it only include positive integers and in the except I could have it say,
"Please only include a positive integer for the input." 
      
In a CSV file for example the data would be given with integer values and string values
so if I wanted to concatinate them I would need to use typecasting to convert the integer
values to string values, like if I was given an item "bottle" and the volume as "12" and 
wanted to make the sentence "The bottle is 12 fluid ounces."
      
If the program were to attempt a mathematical problem that would result in an imaginary
number or an undefined number I could avoid this buy putting in a try/except clause. In the
case of an imaginary number I could put in the exception that if the number is a square root 
of a negative number to print "The number cannot be negative." or in the case of a divide by
0 to print "The denominator cannot equal 0."
''')