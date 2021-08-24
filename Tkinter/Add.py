# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 20:58:28 2021

@author: Sayed
"""

def add(self, *kws):
    result = 0
    value = kws
    for i in value:
        result += i 
    return result  

class Calc:
    def __init__(self):
        
        self.result = 0
        
        
    def add(self, *kws):
        value = kws
        for i in value:
            self.result += i 
        return self.result
    
    def sub(self, *kws):
        self.value = kws
        for i in self.value:
            self.result = self.result - i            
        return self.result
    
    
if __name__ == '__main__':    
    c1 = Calc()
    vResult = 0
    vResult = c1.add(10, 20, 30, 40)    
    print(vResult)
       