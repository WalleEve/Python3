# pythongui.py

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


def exit_qk():
    obj.quit()
    obj.destroy()
    exit()


# obj of Tkinter
obj = tk.Tk()
obj.geometry("500x200+50+50")
obj.resizable(0, 0) # switch off resizable

tabs = ttk.Notebook(obj) # create tab object
# tab 1
tab1 = tk.Frame(tabs)
tabs.add(tab1, text="Tab 1")
# add item to tab 1
label1 = tk.Label(tab1, text="Hello Tab1")
label1.grid()

# tab 2
tab2 = tk.Frame(tabs)
tabs.add(tab2, text="Tab 2")
# add item to tab 2
label2 = tk.Label(tab2, text="Hello Tab2")
label2.grid()

tabs.grid()

obj.mainloop()
