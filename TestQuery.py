# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 20:52:59 2021

@author: Sayed
"""

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

print(len(universities))

student_enroll_values = []
tution_fees = []
def enrollment_stats(ilist):
    for i in range(0, len(universities)):
        student_enroll_values.append(ilist[i][1])
        tution_fees.append(ilist[i][2])
        
    return student_enroll_values, tution_fees
       

students, fees = enrollment_stats(universities)   
print(students) 
print(fees)

def mean_(ilist):
    pass

def median_(ilist):
    pass