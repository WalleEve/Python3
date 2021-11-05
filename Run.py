# FUNCTION RETURN:
    
# Returning multiple values from a Function

# def keyword to create a function
# sum_num function name 
# a, b Parameter 
def sum_num(a, b): 
    res = a + b 
    print(res) # print the value in console we can not store this the value using print statement in the colling environment  
    return res # It return the value to the colling env , we can store the return value 


x = 5 
y = 6 

result = sum_num(x, y) # x, y argument 
print(result)


def calc(a, b): 
    res_sum = a + b 
    res_sub = a - b
    res_mul = a * b
    #print(res) # print the value in console we can not store this the value using print statement in the colling environment  
    return res_sum, res_sub, res_mul  # It return the value to the colling env , we can store the return value 


x = 5 
y = 6 

result = calc(x, y) # x, y argument 
print(result)

rSum, rSub, rMul = calc(x, y)
print(f"SUM: {rSum} SUB: {rSub}  MUL: {rMul}")


def calc(x, y):
    
    return x+y, x-y, x*y

a = 10
b = 30 
res = calc(a, b)
print(res)    
    

def calc(x, y):
    print(x + y)
    return 

a = 10 
b = 30 
r = calc(a, b)
print(r)
    


def calc(x, y): # Parameter 
    print(f"x{x}") 
    print(f"y{y}")
    print(f"x + y: {x + y}") # 40

# Function always returns values 
# Function always return None if there is no Return statement in the function    

a = 10 
b = 30 
r = calc(a, b) # arguemnt 
print(r)


# TYPES OF ARGUMENT:
#1: Formal Argument 
#2: Actual Argument 

def calc(x, y):
    print(x + y)
    return  x + y

a = 10 
b = 30 
r = calc(a, b) # Formal Argument
print(r)   

# a, b : FORMAL ARGUMENT 
# 10, 30 : ACTIUL Argument 


def calc(x, y):
    print(x + y)
    return x + y


r = calc(10, 30) # Actual  Argument
print(r) 

# There are 4 types of argument are allowed in Python: 

#1. Positional Argument 
#2. Keyword Argument 
#3. Default Argument 
#4. Variable length argument 


# Positional Argument

def calc(x, y):
    print(x + y)
    return  x + y

a = 10 
b = 30 
r = calc(a, b) 
print(r) 



def message(name, age):
    print(f"Hello {name} your age is {age}")
    if age >=18:
        return "You are Eligible to Vote"
    else:
        return "Sorry your age is under eligible list."

name = input("Inser your name: ")
age = eval(input("Enter your age: "))

msg = message(name, age)
print(msg)


def message(name, age):
    print(f"Hello {name} your age is {age}")
    if age >=18:
        return "You are Eligible to Vote"
    else:
        return "Sorry your age is under eligible list."

name = input("Inser your name: ")
age = eval(input("Enter your age: "))

msg = message(age, name)
print(msg)

    



        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    