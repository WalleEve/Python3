from tkinter import *
from tkinter import ttk
import sys

root = Tk()
root.title("Country Details")
root.geometry("400x400")

tFrame = Frame(root, bg='yellow')
tFrame.place(x=4, y=5, height=50, width=392)
Label(tFrame, text="Country Details", font=("Arial",12, "bold"), bg='yellow').pack()

sFrame = Frame(root, bg='yellow')
sFrame.place(x=4, y=60, height=335, width=392)

Button(sFrame, text="Search", width=10, height=1, font=("Arial",12, "bold")).grid(row=0, column=0, padx=10, pady=140)




root.mainloop()
