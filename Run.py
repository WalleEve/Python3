"""name = input("Enter your name ") # character
marks = input("Enter your mark: ") # number
print(name)
print(marks)
print(type(name)) # str
print(type(marks)) # number / int
print(marks + 10)
print(name)"""

"""

a = "12345678910"
print(a[-1:-5])


name = "Jean-luc Picard"
name.lower()
print(name)
print(name.lower())


name = "Jean-luc Picard   "
print(name)
print(len(name.rstrip()))
print(len(name))
"""
"""

STRING PROPEERTIES:
1. String contains character
2. string have length
3. Charactrer in string appear in a sequence

# LENGTH
len()

print(len("hello"))


name2 = input("Enter your name: ")
print(name2)
print(len(name2))
name_length = len(name2)
print(name_length)




alphnum = "123"
print(alphnum)
print(len(alphnum))

'abd'
"abc"

' '
" "
' "



name = "acer"
name : variable / identifier

Python identifiers



# RESERVED WORDS:

. True False None
. and, or, not, is
. if elif else
. while, for, break, continue, return, in, yield
. try, except, finally, raise, assert
. import, from, as, class, def, pass, global, nonlocal, lambda, del, with


# DATA TYPES / Built In OBJECT

NUMBER : 123, 3.123, 3+4j, Decimal, Fraction

STRING: 'acer', "acer", "acer'a", ' brand "acer" ', "123", "a/x01@"

LIST : [1] , ["acer"], ["a", "b", "c"], [a, [a, b, c], d]

DICTIONARY: {"food": 'spam', 'test':'yum'}, {'food':["a", "b", "c"]}

TUPLE: ("hello", "acer", "acb"), ('food', ("a", "b", "c"))

FILES: myfile = open("egg", "r")

SET: set("abc"), {"a", "b", "c"}

BOOLEAN: True, False, None
None: None



a = "hello"
a = "hello
acer "


"""

a = "hello \
Python \
              Tutorial"

#print(a)

""" Hello
Pthon
Tutorial"""

"""
 print hello
 Python

print(b) # print
print(c)


Arith Opt: + , _ , * , /

+
*


# + (Join)
a = "hello"
b = "Python"
print(a, b)
print(a + b)
print(a + " " + b)

c = a, b
print(c)
d = a + ' ' + b
print(d)

# *
a = "Python"
print(a)
print(a)
print(a)
print(a)
print(a)

a = a + ' '
print(a * 5)
print((a + ' ') * 5)


# STRING INDEX and SLICING

name = "ACER"
#identifier_name/ variable_name[1]

#any programming language: index start woth 0 
print(name[1])
print(name[0])

last_index = len(name) - 1
print(last_index)
print(name[last_index])


L | E | N | O | V | O   len = 6
0   1   2   3   4   5

name = "LENOVO"
print(name[len(name)-2])

-index number


  L  | E |  N  |  O  |  V  |  O 
 -6   -5   -4    -3    -2    -1


name = "12345" 
print(name[4])

# SLICING: SUBSTRING "LAPTOP BRAND LENOVO"

varibale = "value"
varibale_name[start_index:end_index]
variable_name[:end_index] # start_index default 0
varibale_name[start_ndx:] # end_index default last_index number
 
|  L  |  E  |  N  |  O  |  V  |  O  |
0     1     2     3     4     5     6


|  L  |  E  |  N  |  O  |  V  |  O  |
-6   -5    -4    -3    -2    -1     


name = "LENOVO"
print(name[0:3])
print(name[:])
print(name[1:9])
print(len(name[1:9]))
print(name[3:4])
print(name[:6])



print(name[-6:-2])
print(name[-2:-6])

print(name[6:4])

print(name[-100:]) # None


 function
 method
def
calss
 def 

print("hello")
.print()

len()

# STRING INBUILT METHOD

# UPPER / LOWER

name = " Lenovo " # camel case
print(name.lower())
name2 = name.lower()
print(name2)
print(name)


name = "Lenovo" # camel case
print(name.upper())
name2 = name.upper()
print(name2)
print(name)

+919898976564+91


lstrip
rstrip
strip


name = "   LENOVO   "
print(len(name)) # 12

print(name.lstrip()) # defailt space will be considered 
print(len(name.lstrip()))

print(len(name)) # 12

print(name.rstrip()) # defailt space will be considered 
print(len(name.rstrip()))

print(name.strip()) # defailt space will be considered 
print(len(name.strip()))

phone = "+91 9696392244+91"
print(phone.lstrip("+91"))
print(phone.rstrip("+91"))
print(phone.strip("+91").strip().strip())
"""
# IMMUTABLE

name = "LENOVO"
print(name[1]) # E
name ="O"
print(name)


# NUMBER























































































