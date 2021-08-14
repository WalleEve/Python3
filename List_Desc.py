# List are Mutable Sequence:
The list data structure is another sequence type in Python. Just like string and tuple, list contains that are indexed by integers, starting with 0.

Lists are mutable, meaning we can chagne the value at an index even the list has been created.

# CREATE LIST:
A list literal look extactly like a tuple literal, except that it is surrounded with sqare brackets ([ and ]) instead of parentheses.

>>> colors = ["red", "youllow", "green", "blue"]
>>>print(colors)
>>>print(type(colors))

Like tuples, lists values are not required to be the same type. The list literal["one", 2, 3.2]

We can also use the list() built-in to create a new list object from any other sequence.

For instance, the tuple (1, 2, 3) can be passed to list() to create the list [1, 2, 3]

>>>a = (1, 2, 3)
>>>list_a = list(a)
>>>print(list_a)

>>>list_a = list("Python")
>>>print(list_a)

# Here each letter in the string becomes an element of the list.

# There is more useful way to create a list from a string.
we can create a list from a string of a comma-separated list  of items using the string object's .split() method. 

>>>groceries = "egg, milk, cheese"
>>>grocery_list = groceries.split(", ")
>>>print(grocery_list)

# The string argument passed to .split() is called the separator.

# Split string on semi-colon

>>>"a;b;c".split(";")

# Split string on spaces 
>>>"The quick brown fox".split(" ")

# Split string on multiple characters 
>>>"abbaabba".split("ba")

.split() always returns a string whose length is one or more than the number of separators contained in the string.

if the separator is not containing in the string at all, .split() returns a list with the string as its only element:

>>>"abbaabba".split("c")

# We have seen three ways to create a list 
1. A list literal
2. The list() built-in 
3. The string .split() method 

# Basic List Operatons:
Indexing and slicing operations work on lists the same way they do on tuples.

We can access list element using index notaion:

>>>numbers = [1, 2, 3, 4]
>>>print(numbers[1])

We can create a new list from an existing once using slice notaion.
>>>numbers[1:2]

We can check for the existing of list elements using the in operator:
>>> # Check existence of an element
>>> "bob" in numbers 
>>> # False

Because lists are iterable, we can iterate over them with a for loop.

>>> # Print only the even numbers in the list 
>>>for number in numbers:
	if number % 2 == 0:
		print(number)


Note: The major difference between lists and tuples is that elements of lists may be changed,
	  But element of tuples can not 


# CHanging Elements in a List:
The ability to swap values in a list for other values is called mutability.
Lists are mutable. The elements of tuples may not be swapped for new values,
so tuples are said to be immutable 

 