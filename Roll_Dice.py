# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:02:50 2021

@author: Sayed
"""

import random as r

def d1():
    print()
    print(" -------")
    print("|       |")
    print("|   0   |")
    print("|       |")
    print(" ------- ")
    
def d2():
    print()
    print(" -------")
    print("|       |")
    print("| 0   0 |")
    print("|       |")
    print(" ------- ")
    
def d3():
    print()
    print(" -------")
    print("| 0     |")
    print("|   0   |")
    print("|     0 |")
    print(" ------- ")    
    

def d4():
    print()
    print(" -------")
    print("| 0   0 |")
    print("|       |")
    print("| 0   0 |")
    print(" ------- ")    
 
def d5():
    print()
    print(" -------")
    print("| 0   0 |")
    print("|   0   |")
    print("| 0   0 |")
    print(" ------- ")     
  
def d6():
    print()
    print(" -------")
    print("| 0 0 0 |")
    print("|       |")
    print("| 0 0 0 |")
    print(" ------- ")       
     

def rollDice():
    flag = True 
    while flag:
        u_input = input("Do you want to roll Dice: (Y/N)")
        if u_input.upper() == 'Y':
            rollDice = r.randint(1, 6)
            if rollDice == 1:
                d1()
            elif rollDice == 2:
                d2()
            elif rollDice == 3:
                d3()
            elif rollDice == 4:
               d4()
            elif rollDice == 5:
                d5()
            elif rollDice == 6:
                d6()
        
        else:
            flag = False 
    


rollDice()      
        
    
            
            
            
        

    
