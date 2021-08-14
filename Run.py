from tkinter import *
from tkinter import ttk

root = Tk()
global vSearch
vSearch =  StringVar()
tempData = []


def check(e):
    v= vSearch.get()
    if v=='':
        data= country_list
        print(data)
    else:
        data=[]
        for item in country_list:
            if v.lower() in item.lower():
                data.append(item)
                print(f"Data: {data}")


country_list = ["india", "nepal", "bhutan", "itly", "newziland", "usa", "united kingdom"]

searchCombo = ttk.Combobox(root, values = country_list, font=("Calibri", 12, "bold"), textvariable = vSearch, height = 2, width=22)
searchCombo.set("Pick an Option")
searchCombo.pack(side=LEFT, padx = 5, pady = 5)
searchCombo.bind('<KeyRelease>',check)


root.mainloop()
