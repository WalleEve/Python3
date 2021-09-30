# MEMBERSHIP OPERATOR: 
    
in 

s = "uma sanaker"
subs = 'a'

if subs in s:
    print(f" {subs} found in {s}")
else:
    print(f"{subs} not found in {s}")
    
    
    
# Comparison of string: 
    
<
>
<=
>=
==
!= 


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 == s2:
    print("Both string are eqal!")
elif s1 > s2:
    print(f" {s1} is greater than {s2}")
elif s1 < s2:
    print(f" {s1} is smaller than {s2}")
else:
    print("Hi")
    
    
# Removing Space from the String: 
    
we can use 3 methods to remove space from a string 
1. rstrip() # TO remove space at the right hand side 
2. lstrip() # To remove space at the left hand side 
3. strip() # To remvoe space at both the side 


city = input("Enter your city: ")

city = city.strip()
if city == "Bhubaneswar":
    print("is a temple city")
elif city == "Hyderabad":
    print("nijam city")
elif city == "Banglore":
    print("Smart city")
elif city == "chenni":
    print("larg city")
else:
    print("unable to find your city")
    
 
#  Finding substring: 
    
we can use 4 method 

Forward direction: 
    find()
    index()
    
backward: 
    rfind()
    rindex()
    
 Find: 
 
string.find(substring)
     
s = "uma sanker palai"

print(s.find('k'))
print(s.find('z'))

print(s.find('a'))
print(s.rfind('a'))

s.find(subs , begin , end) 

s = "uma sanker palai"

pos = s.find('z', 0, len(s))
print('pos: ',pos)


s = "uma sanker palai"

print(s.index('k'))
print(s.index('z'))

print(s.index('a'))
print(s.rindex('a'))


# Write a program to display all position of substring in a given string 


us = input("Enter main string: ")  # sadhana
ss = input("Enter search string: ") # a  1, 4, 6

flag = False 
pos  = -1
n  = len(us) # 6

while True: 
    pos = us.find(ss, pos+1, n) # us.find('z', 0, 10)  # -1
    if pos == -1:
        break 
    print("Found at position: ", pos) 
    flag = True
        
if flag == False:
    print("Not Found!")    
















