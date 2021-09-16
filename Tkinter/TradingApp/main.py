# Tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

root = tk.Tk()
root.title("My Trade")
root.geometry("900x500")
root.resizable(0, 0)

# Tabs
tabs = ttk.Notebook(root, ) # create tab object
# tab 1
crTrans = tk.Frame(tabs, bg="blue")
tabs.add(crTrans, text="Cr Transaction")


# tab 2
drTrans = tk.Frame(tabs, bg="yellow")
tabs.add(drTrans, text="Dr Transaction")
# tab 3
crCustomer = tk.Frame(tabs, bg="pink")
tabs.add(crCustomer, text="Cr Customers")
# tab 4
stockIn = tk.Frame(tabs, bg="pink")
tabs.add(stockIn, text="Stock in House")
# tab 5
stockOut = tk.Frame(tabs, bg="pink")
tabs.add(stockOut, text="Stock out House")
# tab 6
orders = tk.Frame(tabs, bg="pink")
tabs.add(orders, text="Orders")
# tab 7
report = tk.Frame(tabs, bg="pink")
tabs.add(report, text="Report")

tabs.pack(expand=1, fill="both")


root.mainloop()
