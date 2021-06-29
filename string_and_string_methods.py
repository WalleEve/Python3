# Reserve Key Word:
in Python some words are reserved to prevent some meaning of functionality. Such type of words are called Reserved word
There are 33 reserved words available in Python
. True, False, None
. and, or, not, is
. if, elif, else
. while, for, break, continue, return, in, yield
. try, except, finally, raise, assert
. import, from, as, class, def, pass, global, nonlocal, lambda, del, with


>>>import keyword
>>>keyword.kwlist # Will print all the reserved key word available in Python


# Datatype:
Datatype represent the type of data present inside a variable.
In Python we are not required to specify the type explicitly. Based on value provided, the type will assigned automatically. Hence Python is Dinamically Typed Language

Python contains the following inbuilt data types

1. int # 1, 123, 123456
2. float # 1.0, 1.2, 123.12
3. complex # 4+3j
5. bool # True, False
5. str  # "acer", 'acer' ,'1234', 'Acer123'
6. bytes
7. bytearray
8. range
9. list
10. tuple
11. set
12. frozenset
13. dict
14. None

Note: Python contains several inbuilt functions

1. type() # to get the type of variable
a = 123456
print(type(a))


2. id() # to get address of object
name = "acer"
print(id(name))





# Strings and String Methods
Collection of test in Python are called string. Special functions called string methods are use to manipulate strings.

# The String Data Type:
Strings are one of the fundamental Python data types. The term data type refers to what kind of data a value represents. Strings are used to represent text.

The string data type has a special abbreviation name in Python: str.
We can see this by using type() function, which is used to determine the data type of a given value.

>>>type("Hello, World")
<class 'str'>

type() also works for values that have been assigned to a variable:
>>>phrase = "Hello World"
>>>type(phrase)
<class 'str'>

#--------------------------------------------------------------------------------------------------------------------------------------------------
String have three properties.
1. String contains characters, which are individual letters or symbols
2. String have length, which is the number of characters contained in the string.
3. Characters in a string appear in a sequence, meaning each character has a numbered position in the string.

# String Literals:
We can create a string by surrounding some test with quotation marks:
string1 = 'Hello, World'
string2 = "1234"

Either single quotes(string1) or double quotes(string2) can be used to create a string.

Whenever we create a string by surrounding test with quotation marks, the string is called a string literal.

Note: Not every string is a string literal.
For example: a string captured as user input isn't a string literal because it isn't explicitly written out in the program's code.

The quotes surrounding a string are called delimiters.
After Python reads the first delimiter, all of the characters after it are considered a part of the string until a second matching delimiter is read.This is why we can use a single quote in a string delimited by double quotes and vice versa.

# Determine the Length of a String:
The number of characters contained in  a string, including space, is called the length of the string.
For example: "abc" has a length of 3 and the string "don't panic" has a length of 11.

To determine a string's length, we use Python's built-in len() function.
len("abc")

We can also use len() to get the length of a string that's assigned to a variable.
letters = "Abcd"
num_letters = len(letters)
print(num_letters)

# Multiline Srtring:
The PEP 8 style guide recommends that each line of Python code contain no more than 79 characters- including spaces.

To deal with long strings, we can break the string up across multiple lines into a multiline string.

paragraph = "This planet has - or rather had - a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."

With a backslash at the end, however, we can keep writing the same string on the next line.
When we print() a multiline string that is broken up by backslashs, the output displayed on a single line.

>>> long_string = "This multiline string is\
displayed on one line"
>>>print(long_string)


Multiline string can also be created using triple quotes as delimiters  (""" or ''').

Note: Triple-quoted string have a special purpose in Python. tey are used to document code. We'll ofter find then at the top of a .py with a description of the code's purpose. THey are also used to document custom functions.
When used to document code, triple-quote string are alled docstring.

# CONCATENATION, INDEXING and SLICING

String Concatination:
Two string can be combined, or concatinated using the + operator.
string1 = "abra"
string2 = "cadabra"
magic_string = string1 + string2
print(magic_string)

Note: that two string are joined without any whitespace

We can use the string concatination to join two related string, such as joining first_name and last_name into a full name

first_name = "Arther"
last_name = "Dent"
full_name = first_name + " " + last_name
print(full_name)

# String Indexing:
Each character in a string has a numbered position called an index.
We can access the character sat the Nth position by putting the number N in between two sqare brackets([and]) immediate after the string.

flavor =  "apple pie"
print(flavor[1])

In Python-and most other programming languages counting always start at zero.
To get the character at the beginning of a string we need to access the character at position 0.

print(flavor[0])

Note: Forgetting that counting starts with zero and trying to access the firat character in a string with the index 1 result in an off-by-one-error.

| a | P | P | l | e |  | p | i | e |
  0   1   2   3   4   5  6   7   8

If we try to access an index beyound the end of a string, Python raises an IndexError:

print(flavor[9])

The largest index in a string is always one less than the string's length.

String also support negative indices:
print(flavor[-1])

|  a  |  P  |  P  |  l  |  e  |    |  p  |  i  |  e  |
  -9    -8    -7    -6    -5    -4   -3    -2    -1

Just like positive indices, Python raises an IndexError if we try to access a negative index less than the index of the first character in the string.

print(flavor[-0])

For example: suppose a string input by a user is assign to the variable user_input.
if we need to get the last character of the string, how do we know what index to use

One way to get the last character of a string is to calculate the final index using len()

final_index = len(user_input) - 1
last_character = user_input[final_index]

Getting the final character with the index -1 takes less typing.
last_character = user_input[-1]


# STRING SLICING:
Suppose we need the string containing just the first three lerrtes of the string "apple pie". We could access each character by index and concatenate them

flavor = "apple pie"
first_three_letters = flavor[0] + flavor[1] + flavor[2]
print(first_three_letters)

We can extract a postion of a string called a substring, by inserting a colon between two index numbers inside of sqare brackets.
flavor = "apple pie"
print(flavor[0:3])

Note: Starting with the character with index 0 and going up to, but not including the character with the index 3.
The [0:3] paert of flavor[0:3] is called slice.

# Normal String Index
|  a  |  P  |  P  |  l  |  e  |    |  p  |  i  |  e  |
   0     1     2     3     4     5    6     7     8
# String Index for Slice
|  a  |  P  |  P  |  l  |  e  |    |  p  |  i  |  e  |
0     1     2     3     4     5    6     7     8     9



# Q : What will be the output :
a = "12345678910"
print(a[-1:-5])


print(flavor[:5])
print(flavor[5:])
print(flavor[:])
print(flavor[:14])

When we try to get a slice where the entire range is out of bounds. flavor[13:15] attempts to get the thirteenth and fourteenth characters, which don't exist. Instead of raising an error, the empty string "" is returned.


flavor[-9:0] # ''
Instead of returning the entire string, [-9:0] returns the empty string "".
This is because the second number in a slice must correspond to a boundry that comes after the boundry corresponding to the first number, but both -9 and 0 correspond to the left-most boundary.
if we need to include the final character of a string in our slice, we can omit the second number:
print(flavor[-9:])

# STRINGS ARE IMMUTABLE
Strings are immutable, which means that we can't change them once we have created then.

word = "goal"
word[0] = "f"

Python throws a TypeError and tells us that str object don't support item assignment.

Note: The term str is Python's internal name for the string data type.


If we want to alter a string, we must create an entire new string.
to change the string "goal" to the string "foal" we can use a string slice to concatename the letter "f" with everything but the first letter of the word "goal"

word = "goal"
word = "f" + word[1:]
print(word)


# Manipulate String with Methods:
String come bundled with special functions called string Methods
that can be used to work with and manipulate strings.

# Converting String Case
To convert a string to all lower case letters, we use the string's.lower() method.
This is done by tracking .lower() on the end of the string itself.

print("Jean-luc Picard").lower()

The dot(.) tells Python that waht follows is the name of the method the lower() method in this case.

Note: We will refer to the name of string methods with a dot at the beginning of then. So for example the .lower() method is written with a dot, instead of lower()

We can also use the .lower() method on a string assigned to variable.

name = "Jean-luc Picard"
name.lower()
print(name)
print(name.lower())

The opposite of the .lower() method is the .upper() method, which converts every character in a string to upper case:

loud_voice = "Can you hear me yet?"
print(loud_voice.upper())



# Removing Whitespace from a string:
Whitespace is any character that is printed as blank space. This includes things like spaces and line feeds, which are special characters that move output to a new line.

Sometime we need to remove whitespace from the beginning or end of a string. This is  specially useful when working with strings that come from user input, where extra whitespace characters may have been introduced by accident.

There are three string methods that we can use to remove whitespace from a string:
1. .rstrip()
2. .lstrip()
3. .strip()

# .rstrip()
Removes whitespaces from the right side of a string.

name = "Jean-luc Picard   "
print(name)
print(name.rstrip())
print(name)

The .lstrip() method works just like .rstrip(), except that it removes whitespace from the left-hand side of the string.

name = "    Jean-luc Picard"
print(name)
new_name = name.lstrip()
print(new_name)


Note: None of the .rstrip(), .lstrip() and .strip() methods remove whitespace from the middle of the string.

# Determine if a string starts or ends with a particular string.
When we work with text, sometimes we need to determine if a given string starts with or end with certain characters. We can use two string methods to slove this problem

.startswith()
.endswith()

starship = "Enterprise"
print(starship.startswith("en")) # False

print(starship.startswith("En")) # True

The .startswith() method is case-sensitive.

Note: The True and False value are not strings. THey are a special kind of data type called a Boolean value.

# String Methods and Immutability:
Most string methods that alter a string, like .upper() and .lower(), actually return copies of the original string with the appropriate modicafication.

name = "Picard"
print(name.upper())
print(name)

name  = "Picard"
name = name.upper()
print(name)

name.upper() returns a new string "PICARD", which is re-assigned to the name variable. This overrides the original string "Picard" assigned to "name"
