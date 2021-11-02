from tkinter import *
import main




root = Tk()
root.title("Child Page")
root.geometry("200x400")
m = main.Main_(root)
f1 = Frame(root, bg="Red")
f1.place(x=1, y=1, height=100, width=100)
m.frame1(f1)
root.mainloop()
