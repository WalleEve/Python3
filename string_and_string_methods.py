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
