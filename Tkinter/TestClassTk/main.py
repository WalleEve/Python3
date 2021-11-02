from tkinter import *

class Main_:
    def __init__(self, master):
        self.master = master

    def frame1(self, master):
        Frame1 = Frame(self.master, bg="Blue")
        Frame1.place(x = 1, y = 1, height=50, width=50)



def main():

    root = Tk()
    root.title("Main Screen")
    root.geometry("300x400")
    m = Main_(root)
    m.frame1(root)

    root.mainloop()



if __name__ == '__main__':
    main()
