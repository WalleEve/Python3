# Tuples Data Type:

Tuples are Immutable Sequence 
A Sequence is an ordered list of values. Each element in a sequence is assigned an integer, called an index, that determines the order in which the values appear.
Just like the string, the index of the first value in a sequence is 0.

What is a Tuple?
The word tuple comes from mathematics, where it is used to describe
a finite ordered sequence of values.
Usually, mathematicians write tuples by listing each element, separated by a comma, inside a pair of parentheses. (1, 2, 3) is a tuple
containing three integers.
Tuples are ordered because their elements appear in an ordered fashion. The first element of (1, 2, 3) is 1, the second element is 2, and
the third is 3.

How to Create a Tuple
There are a few ways to create a tuple in Python. We will cover two of
them:
1. Tuple literals
2. The tuple() built-in


Tuple Literals
Just like a string literal is a string that is explicitly created by surrounding some text with quotes, a tuple literal is a tuple that is written out
explicitly as a comma-separated list of values surrounded by parentheses.

>>> my_first_tuple = (1, 2, 3)

You can check that my_first_tuple is a tuple using type():
>>> type(my_first_tuple)
<class 'tuple'>


Unlike strings, which are sequences of characters, tuples may contain
any type of value, including values of different types. The tuple (1,
2.0, "three") is perfectly valid

There is a special tuple that doesn’t contain any values. This tuple is
called the empty tuple and can be created by typing two parentheses
without anything between them:
>>> empty_tuple = ()

We can create a tuple with exactly one element.

>>> x = (1)
>>>type(x) # class 'int'

To create a tuple containing the single value 1, we need to include a comma after the 1.
>>>x = (1,)
>>>type(x)
or
>>>x = 1,
>>>type(x)

# The tuple() Built-In 
We can also use the tuple() built-in to create a tuple from another sequence type, such as string:

>>>t = tuple("Python")
>>>print(t)

tuple() only accepts a single parameter, so we can't just list the vlaues we want inthe tuple as individual arguments.
if we do Python raises a TypeError.

>>> tuple(1, 2, 3) # TypeError: tuple expected at most 1 arguments, got 3 

We also get a TypeError if the argument passed to tuple() can't be interpreted as a list of values:

>>>tuple(1) # TypeError: 'int' object is not iterable 

>>> a = 1234
>>> b = tuple(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b = tuple(a)
TypeError: 'int' object is not iterable

The iterable in the error message indicates that a single integer can't be iterated,

The single parameter of tuple() is optional, though and leaving it out produces an empty tuple.
>>>a = tuple()
>>>print(a)

Similarities Between Tuples and Strings
Tuples and strings have a lot in common. Both are sequence types
with a finite length, support indexing and slicing, are immutable, and
can be iterated over in a loop.

The main difference between strings and tuples is that the elements
of tuples can be any kind of value you like, whereas strings can only
contain characters

# Tuples have a Length 
Both string and tuples have a length. THe length of a string is the number of characters in it. The length of atuple is the number of elements it contains.

The len() function can be used to determine the length of a tuple.

>>>numbers = (1, 2, 3)
>>>print(len(numbers))

# Tuple Supports Indexing and Slicing:
Tuples also support index notation:

>>>values = (1, 2, 3, 7, 9)
>>>values[2] # 3 

>>>name = "Python"
>>>name[2:4] # th 

# Tuples are Immutable:
Like string tuples are immutable. This means we can't change the value of an element of a tuple once it has been created.

If we try to change the value at some index of a tuple, Python will raise a TypeError.

>>>name[0] = 'J'	# TypeError 'tuple' objects does not support item assignment.

# Note: Although tuples are immutable, there are some situation in which the values in a tuple can change.

# Tuples are Iterable: 
Just like string, tuple are iterable, so we can loop over them:

>>>vowels = ("a", "e", "i", "o", "u")
>>>for vowel in vowels:
	print(vowel.upper())

# Tuple Packing and Unpacking :
We can type out a comma-separated list of values and leave off the parenthese:

>>>coordinates = 4.21, 9.29
>>>type(coordinates)

It looks like two values are being assigned to the single variable
coordinates. In a sense, they are, although the result is that both
values are packed into a single tuple. You can verify that coordinates
is indeed a tuple with type().
If you can pack values into a tuple, it only makes sense that you can
unpack them as well:

>>>x, y = coordinates
>>>print(x)
>>>print(y)


Here the values contained in the single tuple coordinates are unpacked into two distinct variables x and y.

By combining tuple packing and unpacking,we can make multiple varibale assignments in a single line.

>>>name, age, occupation = "David", 34, "Programmer"
print(name, age, occupation)

Keep in mind that the number of variable names on the left of the
assignment expression must equal the number of values in the tuple
on the right hand side, otherwise Python will rase a ValueError:

>>>a, b, c, d = 1, 2, 3 # ValueError 


# Checking Existance of values with in:
we can check wheather a value is containg in a  tuple with the in keyword.

>>>vowels = ("a", "e", "i", "o", "u")
>>>"o" in vowels 
>>>"x" in vowels 

if the value of the left of in is contained in the tuple ot the right of in, the result is True, otherwise result is False.

# Retruning Multiple Values from a FUnction :
one common use of tuple is to return numtiple values from  a single function.

>>>def adder_subtractor(num1, num2):
	return (num1 + num2 , num1 - nume2)

>>>adder_subtractor(3, 2)





