# Strings are Immutable:
Strings are immutable, which means that we can't change them once we've created them.

>>>word = "goal"
>>>word[0] = "f" # TypeError: 'str' object does not support item assignment

Note: the term str is Python's internal name for the string dsata type.

>>>word = "goal"
>>>word = "f" + word[1:]
>>>word

# Determine if a string starts or ends with a Particular String
Sometime we need to determine if a given string starts with or ends with certain characters. We can use two string methods to solve this Problem:
.startswith()
.endswith()

>>>starship = "ENterprise"
>>>starship.startswith("en")
False

The .startswith() method is case-sensitive.

>>> starship.startswith("En")

>>>starship.endswith("rise")

Note: The True and False value are not strings. THey are a special kind of data type called a Boolean Value .


# Interact With user Input:
We can get some input from a user with the input() function.

>>>input()
When we press Enter, it looks like nothing happens. The cursor moves to a new line, but a new >>> prompt doesn't appear. Python is waiting for us to enter something!

We can give it a prompt to display to the user.
The imput() function displays the prompt and waits for the user to type something on their keybord. When the user hits Enter, input() returns their input as a string that can be assigned to a variable and used to do something in our Program.

prompt = "Hay, what's up?"
user_input = input(prompt)
print("You said: ", user_input)


response = input("what should I shout?")
shouted_response = response.upper()
print("Well, If you insist...", shouted_response)

# Challenge: Pick Apart Your User’s Input
Write a script named first_letter.py that first prompts the user for
input by using the string "Tell me your password:" The script should
then determine the first letter of the user’s input, convert that letter
to upper-case, and display it back.


# Working with String and Numbers:
When we get user input using the input() function, the result is always a string.

# Strings and Arithmetic Operator:
We have seen that string objects can hold many types of characters, including numbers.

>>>num = "2"
>>>num + num

The + operator concatenate two string together. so the result of "2" + "2" = "22"

String can be "multiplied" by a number as long as that number is an integer, or whole number.

>>>num = "12"
>>>num * 3
'121212'

num * 3 concatenates the string "12" with itself three times and returns the string "121212"

To compare this operator to arithmetic with number, notice that
"12" * 3 = "12" + "12" + "12"

If we use * operator between two strings?
>>>"12" * "3" # TypeError: can't multiply sequence by non-int of type 'str'

when we try to add a string and a number
>>> "3" + 3  # TypeError: can only concatenare str (not "int") to str

# Converting Strings to Number:

num = input("Enter a number to be doubled: ")
doubled_num = num * 2
print(doubled_num)

To perform arithmetic on numbers that are contained in a string, we must frist convert then from a string type to a number type.
There are two ways to do this: int() and float()

int() stands for integer and converts objects into whole Numbers
while float() stands for floating-point number and converts object into numbers with decimal points.

>>>int("12") # 12
>>>float("12") # 12.0

Notice how float() adds a decimal point to the number. Floatingpoint numbers always have at least one decimal place of precision. For
this reason, we can’t change a string that looks like a floating-point
number into an integer because we would lose everything after the
decimal point:


num = input("Enter a number to be doubled: ")
doubled_num = float(num) * 2
print(doubled_num)

# Converting Numbers to string
Sometimes we need to convert a number to a string. we might do
this, for example, if we need to build a string from some pre-existing
variables that are assigned to numeric values.


num_panckes = 10
print("I am goint to eat " + num_panckes + " pancakes") # TypeError

Since num_pancakes is a number, Python can’t concatenate it with the
string "I'm going to eat". To build the string, we need to convert
num_pancakes to a string using str():

num_pancakes = 10
print("I am goint eat " + str(num_pancakes) + " pancakes")


we can also call str() on a number literal:
print("I am goint to eat " + str(10) + " pancakes")

str() can even handle arithmetic expressions:

>>>total_pancakes = 10
>>>pancakes_eaten = 5
>>>print("Only "+ str(total_pancakes - pancakes_eaten) + " pancakes left")



# Streamline our print statement:
Suppose we have a string name = "Zaphod" and two integers heads = 2
and arms = 3. we want to display them in the following line: Zaphod
has 2 heads and 3 arms.

This is called string interpolation,

 which is just a fancy way of saying that we want to insert some variables into
specific locations in a string


The first involves using
commas to insert spaces between each part of the string inside of a
print() function:

name = "Zaphod"
heads = 2
arms = 3
print(name, "has", str(heads), "heads and", str(arms),"arms")

Another way to do this by concatenating the string with the + operator:

print(name + " has " + str(heads) + " heads and " + str(arms) + " arms")



name = "Zaphold"
head = 2
arms = 3

string1 = name, "has", str(head), "heads and", str(arms),"arms"
string2 = name + " has " + str(head) + " heads and " + str(arms) + " arms"

print(string1)
print(type(string1))

print(string2)
print(type(string2))


print(name, "has", str(head), "heads and", str(arms),"arms")


print(type(name + " has " + str(head) + " heads and " + str(arms) + " arms"))

string3 = (name, "has", str(head), "heads and", str(arms),"arms")
print(string3)

# Formatted String
Both techniques produce code that can be hard to read. Trying to keep
track of what goes inside or outside of the quotes can be tough. Fortunately, there’s a third way of combining strings: formatted string
literals, more commonly known as f-strings

f"{name} has {heads} head and {arms} arms"
string3 =  f"{name} has {heads} head and {arms} arms"
print(string3)
print(type(string3))


There are two important things to notice about the above examples:
1. The string literal starts with the letter f before the opening quotation mark
2. Variable names surrounded by curly braces ({ and }) are replaced
with their corresponding values without using str()

We can also insert Python expression in between the curly craces.

n = 3
m = 4
print(f"{n} times {m} is {n * m}")

f-strings are only available in Python version 3.6 and above. In earlier versions of Python, the .format() method can be used to get the
same results. Returning to the Zaphod example, we can use .format()
method to format the string like this:

print("{} has {} heads and {} arms".format(name, hands, arms))




# Find a String in a String:

One of the most useful string method is .find(). we can use this method to find the location of one string in another string-commonly referred to as a substring.

To use .find(), trac it to the end of a variable or a string literal and pass the string we want to find in between the parentheses

>>>phrase = "the surprise is in here somewhere"
>>>phrase.find("surprise")

The value that .find() returns is the index of the first occurrence of the string we passed to it.

if .find() doesn't find the desired substring it will return -1 instead.

>>>phrase = "the surprise is in here somewhare"
>>>phrase.find("eyafjall")

We can call string methods on a string literal directly, so in this case we don't need to create a new string.

>>>"the surprise in here somewhare".find("surprise")

Keep in mind that this matching is done exactly, character by character, and is case-sensitive.

if a subtring appears more than once in a string, .find() only returns the index of the first appearance, starting from the beginning of the string.

>>> "I put a string in your string".find("string")

The .find() method only accepts a string as input. If you want to
find an integer in a string, you need to pass the integer to .find() as a
string. If you do pass something other than a string to .find(), Python
raises a TypeError:

>>>"My number is 555-555-5555".find(5) # TypeError: must be str, not int


# String Replace :
string objects have a .replace()
method that replaces each instance of a substring with another string.

Just like .find(), you tack .replace() on to the end of a variable or
string literal. In this case, though, you need to put two strings inside
of the parentheses in .replace() and separate them with a comma. The
first string is the substring to find, and the second string is the string
to replace each occurrence of the substring with.

For example, the following code shows how to replace each occurrence of "the truth" in the string "I'm telling you the truth; nothing
but the truth" with the string "lies":
>>> my_story = "I'm telling you the truth; nothing but the truth!"
>>> my_story.replace("the truth", "lies")
"I'm telling you lies; nothing but lies!"


Note: Since strings are immutable objects, .replace() doesn’t alter my_story.

To change the value of my_story, you need to reassign to it the new
value returned by .replace():

>>> my_story = my_story.replace("the truth", "lies")
>>>my_story
