# Write a Python Script:
There are two main window that we will work in IDLE:
the INTERACTIVE Window
the SCRIPT Window

The interactive window contains a Python Shell, which is a textual user interface used to interact with Python language.

The  >>> symbol is called PROMT.

>>> 1 + 1
2
>>>

The sequence of events in the interactive window can be described as a loop with three steps.
1. First, Python reads the code entered at the prompt.
2. Then the code is evaluated.
3. Finally the output is printed in the window and a new prompt is displayed.

This loop is commonly referred as READ-EVALUATE-PRINT Loop, or REPL.

To print text to the screen in Python, we use the print() function. A function is a bit of code that typically takes some input, called an argument, does something with that input and produces output, called the return value.

# Errors:
Mistake made in a program are called errors, and there are two main types of errors we weill experience
1. Syntax errors
2. Run-Time errors

# Syntax Errors: occurs when we write some code that isn't allowed in the Python language.

Ex: print("Hello,world') # SyntaxError: EOL while scanning string literal

EOL: Stands for End Of Line

A String literal is text contained in between two double quotation marks.
Ex: "Hello' World" is a string literal.

# Run-Time Error:
IDLE catches syntax errors before a program starts running, but some errors cannot be caught until a program is executed. These errors are known as run-time errors because they only occur at the time that a program is run.

Ex: print(Hello, world) # NameError: name 'Hello' is not defined

# CREATE A VARIABLE:
In Python, variables are names that can be assigned a value and used to reference that value throughout our code.
1. Variables keep values accessible
2. Variables give values context

# The Assignment Operator:
Values are assigned to a variable using a special symbol = called the assignment operator.
An operator is a symbol like = or + that performs some operation on one or more values.
The = operator takes a value to the right of the operator and assign it to the name on the left of the operator.

phrase = "Hello World"
print(phrase)

Note: Variable names are case-sensitive

phrase = "Hello World"
print(Phrase) # NameError: name 'Phrase' is not defined

# Rules for Valid Variable Names
Variable name can be as long or as short as we like, but there are a couple of rules we must follow. Variable can only contain uppercase and lowercase letters(A-Z, a-z), digits(0-9) and user-score(_), Variable names cannot begin with a digit.

Descriptive names are better than short names

In Python, It is more common to write variable names in snake case like num_students and list_of_names. Every letter is lower case, and each word is separated by an underscore.

PPE 8

# Inspect Values in the Interactive Window:
>>>phrase = "Hello, World"
>>>phrase

when we type phrase and press enter, we are telling Python to inspect the variable phrase.


# How to Write a Comment
The most common way to write a comment is to begin a new line in our code with # character.
Comments that start on a new line are called block comments.

# This is a block comment.

phrase = "Hello World"
print(phrase) # This is an in-line comment
