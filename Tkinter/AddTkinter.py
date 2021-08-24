# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 20:57:53 2021

@author: Sayed
"""
from tkinter import *
from tkinter import ttk
from  Add import Calc

global eValue
global result
result = 0

def main():

    valueList = []
    tempValue = eValue.get()
    #valueList = eValue.split(',')
    result = Calc.add(valueList)
    #return result


root = Tk()
eValue = StringVar()
entryBox = Entry(root, textvariable = eValue)
entryBox.pack()
addbutton = Button(root, text= "Add", command=main)
addbutton.pack()
rLabel = Label(root, text=result)
rLabel.pack()
root.mainloop()
