7. Do python lists store values or pointers?

# pointer 


8. What does “del” do?

l1 = [1, 2, 3, 4, 5, 6]
print(l1)
del l1[3] # [1, 2, 3, 5, 6]
del l1[l1.index(5)] # [1, 2, 3, 6]
print(l1) # 

l1 = [1, 2, 3, 4, 5, 6]

| 1 | 2 | 3 | 4 | 5 | 6 |
0   1   2   3   4   5   

print(l1)
del l1[2:4] # : slicing 
del l1[2:5]
print(l1)


9. What is the difference between “remove” and “pop”?

# remove accept values
# pop accepts index 
# pop return the deleted value 
# remove returns None 
 # .pop()
car = ["BMW", "AUDI", "FORD", "TATA"]
print(car)
a = car.pop(car.index("FORD")) 
print(car)
print(a)

# .remove()
car = ["BMW", "AUDI", "FORD", "TATA"]
print(car)
a = car.remove("FORD") 
print(car)
print(a)


10. Remove duplicates from a list

li = [3, 2, 1, 3, 1, 4, 6, 3, 7]

eli = []

for i in li:
    if i not in eli:
        eli.append(i)
    print(eli)
    
# SET Data type 

li = [3, 2, 1, 3, 1, 4, 6, 3, 7] 
nli = list(set(li))
print(nli)   



11. Find the index of the 1st matching element

car = ["BMW", "AUDI", "FORD", "TATA", "BMW", "AUDI", "BMW"]

print(car.index("BMW"))
print(car.index("BMW",1, 5))

print(car.index("BMW", car.index("BMW") + 1 ))

print(car.index("BMW", car.index("BMW", car.index("BMW") + 1 ) + 1))



12. Remove all elements from a list

car = ["BMW", "AUDI", "FORD", "TATA", "BMW", "AUDI", "BMW"]
del car[:] # 
print(car)
car = ["BMW", "AUDI", "FORD", "TATA", "BMW", "AUDI", "BMW"]
del car[:3] 
print(car)
car = ["BMW", "AUDI", "FORD", "TATA", "BMW", "AUDI", "BMW"]
del car[-3:]
print(car)
car = ["BMW", "AUDI", "FORD", "TATA", "BMW", "AUDI", "BMW"]
del car[1:5]
print(car)
car = ["BMW", "AUDI", "FORD", "TATA", "BMW", "AUDI", "BMW"]
del car[-1]
print(car)





13. Iterate over both the values in a list and their indices # enumerator  / interpolation f string

car = ["BMW", "AUDI", "FORD", "TATA", "BMW", "AUDI", "BMW"]
print(list(enumerate(car)))

car = ["BMW", "AUDI", "FORD", "TATA", "BMW", "AUDI", "BMW"]

for inx, val in enumerate(car):
    print(f"Car brand {val} and it's index number {inx}")
    #print("car brand " + val + " it's index number " + str(inx)) 
    

14. How to concatenate two lists

car = ["BMW", "AUDI", "FORD", "TATA"]
car2 = ["TOYOTA", "KIA"]
    
car.extend(car2) 
print(car)

car = ["BMW", "AUDI", "FORD", "TATA"]
car2 = ["TOYOTA", "KIA"]

print(car + car2)
print(car)
print(car2)


15. How to manipulate every element in a list with list comprehension

la = [2, 3, 4, 5, 6] 
b = 5 

c = [i + b for i in la ]
print(c)
 

for i in la:
    print(i + 5)


16. Count the occurrence of a specific object in a list

car = ["BMW", "AUDI", "FORD", "TATA", "AUDI", "KIA", "BMW", "AUDI"]

print(car.count("BMW"))
print(car.count("AUDI"))
  

 
car = ["BMW", "AUDI", "FORD", "TATA", "BMW", "AUDI", "BMW"] 

for inx, val in enumerate(car):
    #print(inx, val)
    if val =="BMW":
        
        print(inx, val)

 
car = ["BMW", "AUDI", "FORD", "TATA", "BMW", "AUDI", "BMW"] 

c= [ val for ind, val in  enumerate(car) if val == "BMW"]
print(c)

    

    





