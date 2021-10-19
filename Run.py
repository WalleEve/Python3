# Find:
    
str = "uma sanker palai"  # a
print(str.find('z'))
print(str.rfind('z'))


# index 

str = "uma sanker palai"  

print(str.index('z'))
print(str.rindex("z"))



# Program to display all possible of substring in a given main string 
 
str1 = input("Enter a strting: ")
sub = input("Enter a search string: ")

a = len(str1) 
pos = -1 
flag = False 

while True:
    pos = str1.find(sub, pos+1, a)
    if pos == -1:
        break
    print("Substring found at position ", pos )
    flag = True
    
if flag == False:
    print("Substring not found")


# FOR 

str1 = input("Enter a strting: ")
sub = input("Enter a search string: ")
n = len(str1)
indx = -1

for i in str1:
    indx = indx + 1 
    if sub == i:
        print(indx)
        
  
# Count 

a = 'sadhana behera mca bhadrak'

print(a.count('a'))
print(a.count('ad'))
print(a.count('a', 19)) 
print(a.count('a', 19, 22)) 


# Replacing :
    
a = 'sadhana behera mca bhadrak' # immutable  
r = 'chandbali'

x = a.replace('bhadrak', r)

print(x)


# Splitting:
    
We can split the given string according to specified separator by sing split() method.

l = s.split(separator)

The default separator is space. 
The return type of split() method is List 

a = 'sadhana behera mca bhadrak'
l = a.split()
print(l)

, -, 'a'

l = a.split('a')
print(l)

# Join of String:
We can join a group of strings (list or tuple) with the given separator.

s = seperator.join(group of strings)
separator should be string type 
the return type of a join() method is string.

t = ('uma', 'sadhana', "tanjima", "acer") # Tuple 
s = '-'.join(t)
print(s)

t = ('uma', 'sadhana', "tanjima", "acer") # Tuple 
j = ("sayed", 'dell')
s = j.join(t) # AttributeError: 'tuple' object has no attribute 'join'
print(s)









        
        
    



























