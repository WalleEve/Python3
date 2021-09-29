del 
-------------

x = 10 
print(x)
del x 
print(x)

a = 'uma sanker'
del a[0] # TypeError: 'str' object doesn't support item deletion
print(a)
del a
print(a)

a = ['uma', 'sadhana', 'tanjima']
del a[0]
print(a)

del a 
print(a)


a = 10 

del a 

a = None


#  String 

any sequence of character within either single quote or double quote is consider as a string.

syntax: 
a = "uma" # string 
b = 'uma' # string 
c = "10" # string 
d = "10.5" # string 
    
print(type(a))    

a = """
uma 
sanker 
palai 
"""

print(a)

a = " uma \
    sanker \
        palai"
        
print(a)





