# NUMBER AND MATH CH1:

# Integers and Floating-point numbers:
Python has three built-in number data types:
. Integer 
. Float 
. complex numbers 

#Integer:
An integer is a whole number with no decimal place. 
The name for the integer data type is int.

>>>type(1)

We can create an integer by simply typing the number explicitly or using the int() function.

>>> 123 
>>> a = 123
>>>type(a)

>>> a = "123"
>>> type(a)

>>> a = int("123")
>>>type(a)

An integer literal is an integer value that is written explicitly in our code.

For example: 
1 is an integer literal, but int("1") isn't 

>>>a = 1 # integer literal 
>>>a = int("1") # not integer literal 

integer literals can be written in two different ways:
>>>100000
>>>1_000_000

In Python we can't use commas to group digits n integer literals, but we can use an underscore(_). 

>>>a = 1,000,000
>>>type(a)

>>>a = 1_000_000
>>>type(a) 


# Floating-Point Numbers:
a floating-point number or float for short, is a number with a decimal place. 
1.0 is a floating-point number as is -2.75. 
The name of a floating-point data type is float:
>>>type(1.0)

Floats can be created by typing a number directly into our code, or by using the float() function.
Like int(), float() can be used to convert a string containig a number to a floating-point number.

>>>float("1.25")

A floating-point literal is a floating-point value that is written explicitly in our code. 1.25 is a floating-point literal, while float("1.25") is not.

Floating-point literals can be created in three different ways 

>>> 1000000.0
>>>1_000_000.0
>>>1e6 

For really large numbers, we can use E-notation. 
To write a float literal in E-notation, type a number followed by the
letter e and then another number. Python takes the number to the
left of the e and multiplies by 10 raised to the power of the number
after the e. So 1e6 is equivalent to 1×10⁶.

E-notation is short for exponential notation, and is the more
common name for how many calculators and programming languages display large numbers

Python also uses E-notation to display large floating point numbers:
>>>200000000000000000.00
2e+17

The + sign indicates that the exponent 17 is a positive number. 

We can also use negative numbers as the exponent.

>>>le-4
0.0001
The literal 1e-4 is interpreted as 10 raised to the power -4, which is 1/10000, equivalent, 0.0001.

Unlike integer, float do have a maximum size. The maximum floating-point number dependes on our system, but something like 2e400 ought to be well beyound most machin's capabilities.
2e400 is 2 x (10)400, which is far more than the total number of atoms in the universe!


>>>2e400 # inf 

>>>n = 2e400
>>>n # inf
>>>type(n)


# Arithmetic Operators and Expressions:

# Addition:
Addition is performed with the + operator 
>>>1 + 2 # 3 
>>>1.0 + 2 # 3.0 

# Subtraction:
To subtract two numbers, just put - in between them 
>>>1 - 1 # 0
>>>5.0 - 3 # 2.0 
>>>1 - -3 

# Multiplication:
To multiply two numbers, use the * operator 
>>>3 * 3  # 9
>>>2 * 8.0 # 16.0

# Division:
The / operator is used to divide two numbers:
>>>9 / 3 # 3.0 
>>>5.0 / 2 # 2.5 

unlike addition, subtraction and multiplication, division with / operator always returns a float. 

if we want to make sure that we get an integer after dividing two numbers, we can use int() to convert the result.

>>>int(9 / 3) # 3 













