from tkinter import *
from tkinter import ttk

#---------------------------------------------------------------------------------------------------------------------------------------------------
# Functional Part
#---------------------------------------------------------------------------------------------------------------------------------------------------

# Mail Dashboard
def mailDashboard():
    mDashboard = Toplevel(root)
    mDashboard.title("Mail Dashboard")
    mDashboard.geometry("600x600")
    mDashboard['background']='lightpink3'
    # From/Button Frame
    bFrame = Frame(mDashboard, bg="azure2", relief="flat", bd=1)
    bFrame.place(x=1, y=1, width=400, height=120)

    # Button
    sendButton = Button(bFrame, text="Send", width=10, font=("Calibre", 12))
    sendButton.grid(row=0, column=0, padx=10, pady=10)
    clearButton = Button(bFrame, text="Clear", width=10, font=("Calibre", 12))
    clearButton.grid(row=0, column=1, padx=10, pady=10)
    quitButton = Button(bFrame, text="Quit", width=10, font=("Calibre", 12))
    quitButton.grid(row=0, column=3, padx=10, pady=10)




    # Image Frame
    iFrame = Frame(mDashboard, bg="azure3", relief="flat", bd=1)
    iFrame.place(x=405, y=1, width=190, height=120)

    # To CC Frame
    ftcFrame =  Frame(mDashboard, bg="azure2", relief="flat", bd=1)
    ftcFrame.place(x=1, y=122, width=595, height=100)

    # Text Frame
    tFrame =  LabelFrame(mDashboard, text="Context", bg="azure2", bd=5, relief=RIDGE)
    tFrame.place(x=3, y=225, width=593, height=370)

    # Label
    Label(ftcFrame, text="From: ", font=("Calibre", 12), bg="azure2").grid(row=0, column=0, padx=3, pady=2, sticky=W)
    Label(ftcFrame, text="To: ", font=("Calibre", 12), bg="azure2").grid(row=1, column=0, padx=3, pady=2, sticky=W)
    Label(ftcFrame, text="Cc: ", font=("Calibre", 12), bg="azure2").grid(row=2, column=0, padx=3, pady=2, sticky=W)

    # Entry Box
    fromEntry = Entry(ftcFrame, font=("Calibre", 12), width=40)
    fromEntry.grid(row=0, column=1, padx=3, pady=2, sticky=W)
    toEntry = Entry(ftcFrame, font=("Calibre", 12), width=40)
    toEntry.grid(row=1, column=1, padx=3, pady=2, sticky=W)
    ccEntry = Entry(ftcFrame, font=("Calibre", 12), width=40)
    ccEntry.grid(row=2, column=1, padx=3, pady=2, sticky=W)

    # Text Box
    messageBox = Text(tFrame, height=20, width=71)
    messageBox.pack(expand=True)




# Login Function
def login():
    mailDashboard()




#-------------------------------------------------------------------------------------------------------------------------------------------------------
#     Main Script
#
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.title("Fennec Mail ")
root.geometry("600x400")
root['background']='#40E0D0'
global UserName
global Password
UserName = StringVar()
Password = StringVar()
# Title Frame
tFrame  = Frame(root, bg="azure2", relief="raised", bd=5)
tFrame.place(x=1, y=0, width=597, height=60)
# Title :
Label(tFrame, text="Fennec Mail", bg = "azure2", font =("Calabri",15, "bold")).pack()

# login Frame
eFrame = Frame(root, bg="honeydew2", relief="flat", bd=5)
eFrame.place(x=1, y=130, width=597, height=150)
#Label
Label(eFrame, text="", bg="honeydew2").grid(row=0, column=0)
Label(eFrame, text="", bg="honeydew2").grid(row=1, column=0)
Label(eFrame, text="user name: ", font=("Calabri", 12, "bold"), bg="honeydew2" ).grid(row=2, column=0)
Label(eFrame, text="", bg="honeydew2").grid(row=3, column=0)
Label(eFrame, text="password: ", font=("Calabri", 12, "bold"), bg="honeydew2").grid(row=4, column=0)

# Entry Box:
userEntry =  Entry(eFrame, width=30, bg="white", font = ("Calabri", 12), textvariable=UserName)
userEntry.grid(row=2, column=1, padx=10)
paswdEntry = Entry(eFrame,  width=30, bg="white", font = ("Calabri", 12), show="*", textvariable=Password)
paswdEntry.grid(row=4, column=1, padx=10)

# login Frame
bFrame = Frame(root, bg="honeydew2", relief="flat", bd=5)
bFrame.place(x=1, y=285, width=597, height=60)

# Button
bLogin = Button(bFrame, text="Login", width=15, height=2, command=login)
bLogin.grid(row=0, column=0, padx=10, pady=5)
bLogin = Button(bFrame, text="Clear", width=15, height=2)
bLogin.grid(row=0, column=1, padx=10, pady=5)
bLogin = Button(bFrame, text="Sign up", width=15, height=2)
bLogin.grid(row=0, column=2, padx=10, pady=5)
bLogin = Button(bFrame, text="Quit", width=15, height=2)
bLogin.grid(row=0, column=3, padx=10, pady=5)


# Label
unameLabel = Label()



root.mainloop()
