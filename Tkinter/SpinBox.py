# pythongui.py

import tkinter as tk
from tkinter import ttk


# obj of Tkinter
obj = tk.Tk()
obj.geometry("500x200+50+50")
obj.resizable(0, 0) # switch off resizable

# relief : GROOVE, FLAT, SUNKEN, RAISED, RIDGE
spinbox = tk.Spinbox(obj, from_=0, to=5, width=3, bd=5, relief=tk.GROOVE)
spinbox.grid()

obj.mainloop()
