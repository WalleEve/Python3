# OPERATOR 
. Arithmetic Operator 
. Comparison operator 
. Assignment Operator
. Logical Operator 
. Bitwise Operator (not completed)
. Membership Operator : in , not in 
. Identity Operator : is 

# Data Type 
. Reserve words :
.  

. String 
. Number

 
. Tuples 
. List 
. Dictionary 
. Set 

. Range 

2 Types of Data type:
    
MUTABLE: LIST, DICTIONARY, SET [We can change the value (Add a value)]
IMMUTABLE:  STR, NUM, TUPLE   [We can not change the value (Add a value) ] 

# CONTROL FLOW 

Control flow describe the order in which statements will be executed at runtime 



a = [1, 2, 3, 4, 5] 

a.append(7)

a = []
a.pop() : IndexError: pop from empty list


Control Flow Statement: 
    
    1. Conditional Statement: 
        1. if
        2. if - elif  
        3. if - elif - else 
        
    2. Transfer Statement:
        1. break 
        2. continue 
        3. pass 
    3. Iterative Statement:
        1. for 
        2. while 
        

1. Conditional Statement: 
    
# IF 

syntax: if condition: statement 
syntax: if condition:
            statement 1
            statement 2 
            .
            .
            

# If the condition is True then the statements will be executed 


# Indentation : compulsory 



print('a')
 print('a') # IndentationError: unexpected indent 
 
a =

1   2
1   4


name = input("Enter your name: ")

if name == "uma":
    print("Hello UMA Good Morning")
    
print("How are you!")



name = input("Enter your name ")

if name:
    print(f"Hello {name}")
     
print(f"Hi {name}") 

name = 'a' # True 
name = None # False 



name = input("Enter your name ")

if name:
    print(f"Hello {name}")
    print("How are you")
    print("Where are you from")
    
print(f"Hi {name}") 


name = input("Enter your name ")

if name:
    print(f"Hello {name}")
    print("How are you")
    print("Where are you from")
if name == '':
    print("Please enter your name")
    name = input("Enter your name ")
    
    
print(f"Hi {name}") 


name = input("Enter your name ")

if name: # True
    print(f"Hello {name}")
    print("How are you")
    print("Where are you from")
    
    if len(name) > 5: # True
        print("Your name contain more than 5 chanracter")
    print("Please choose a small name less than 6 character")

        
    
    
print(f"Hi {name}") 





    

            

    
       




