from tkinter import *
from tkinter import ttk

root = Tk()

s = ttk.Style()
s.configure('TNotebook.Tab', font=('URW Gothic L','15','bold') )

notebook = ttk.Notebook(root)

f1 = Frame(notebook, bg='red', width=200, height=200)
f2 = Frame(notebook, bg='blue', width=200, height=200)

notebook.add(f1, text="frame 1" )
notebook.add(f2, text="frame 2 longer" )

notebook.grid(row=0, column=0, sticky="nw")
root.mainloop()
