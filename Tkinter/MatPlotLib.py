# tkoops.py

import matplotlib as mpl
import matplotlib.pyplot as plt
#import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

import tkinter as tk
from tkinter import ttk # ttk changes the look of widgets

#tkagg = mpl.backends.TkAgg



# inherit from tk.Frame
class HomePage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets() # call user defined createWidgets

    def createWidgets(self):
        # create Label
        self.myLabel = ttk.Label(self, text="Hello World! This is Home page")
        # set grid parameters
        self.myLabel.grid(
                row=0, column=0,
                rowspan=3, columnspan=2,
                padx=10, pady=10,
                ipadx=3, ipady=3, # internal pad

                # use this or below
                # sticky="nsew"  # north south east west
                # sticky=tk.E
            )

        x = np.random.rand(100)
        fig = mpl.figure.Figure(figsize=(5,5))
        sf = fig.add_subplot(111)
        sf.plot(x)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().grid(row=5, column=1)
        canvas.show()

def main():
    app = HomePage()
    app.master.title("Plot graphs")
    app.mainloop()

if __name__ == '__main__':
    main()
