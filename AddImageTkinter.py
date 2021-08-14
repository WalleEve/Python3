import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open("TheWorld\\India_Flag.jpg")
image1 = image1.resize((50, 50))
test = ImageTk.PhotoImage(image1)


label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=20, y=20)
root.mainloop()


#img = getflag()
image1 = Image.open("India_Flag.jpg")
image1 = image1.resize((50, 50))
test = ImageTk.PhotoImage(image1)

label1 = Label(fFrame, image=test)
label1.image = test
label1.place(x=20, y=20)
