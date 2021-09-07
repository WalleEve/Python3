from tkinter import *
from tkinter import ttk
import configparser
import smtplib
import os
import sys
from tkinter import messagebox

#---------------------------------------------------------------------------------------------------------------------------------------------------
# Functional Part
#---------------------------------------------------------------------------------------------------------------------------------------------------
# SEND MAIL:


def send_email(subject, body_text, to_emails, cc_emails, bcc_emails):
    """
    Send Email
    """
    base_path = os.path.dirname( os.path.abspath(__file__))
    config_path = os.path.join(base_path, "Config.ini")

    if os.path.exists(config_path):
        cfg = configparser.ConfigParser()
        cfg.read(config_path)
    else:
        print("Config File not cound!")
        os.exit()

    host = cfg.get("gmail","server")
    port = cfg.get("gmail","port")
    from_addr = vFrom.get()
    paswd = vPassword.get()


    BODY = "\r\n".join((
    "From: %s" %from_addr,
    "TO: %s" %", ".join(to_emails),
    "CC: %s" %", ".join(cc_emails),
    "BCC: %s" %", ".join(bcc_emails),
    "subject: %s"  %subject,
    "",
    body_text
    ))

    emails = to_emails + cc_emails + bcc_emails
    print(emails)

    server = smtplib.SMTP(host, port)
    print("server:", server)
    server.ehlo()
    server.starttls()
    server.login(from_addr, paswd)
    print("login successfull")
    server.sendmail(from_addr, emails, BODY)
    print("mail send Done")
    messagebox.showinfo("showinfo", "Mail sent successfully!")
    server.quit()




def send():

    toMail = vTo.get()
    ccMail = vCc.get()
    subject = vSubject.get()
    message = messageBox.get("1.0","end-1c")
    bcc_emails = ['x2xcyrus@gmail.com']
    toMail = toMail.split(',')
    ccMail = ccMail.split(',')
    send_email(subject, message, toMail, ccMail, bcc_emails)

    fromEntry.configure(text='')
    fromPassword.configure(text='')
    toEntry.configure(text='')
    ccEntry.configure(text='')
    subEntry.configure(text='')
    messageBox.delete("1.0","end")





# Mail Dashboard
def mailDashboard():
    # Global Variable
    global vFrom
    global vPassword
    global vTo
    global vCc
    global vSubject
    global messageBox

    global fromEntry
    global fromPassword
    global toEntry
    global ccEntry
    global subEntry
    global messageBox

    vFrom = StringVar()
    vPassword = StringVar()
    vTo = StringVar()
    vCc = StringVar()
    vSubject = StringVar()



    mDashboard = Toplevel(root)
    mDashboard.title("Mail Dashboard")
    mDashboard.geometry("600x600")
    mDashboard['background']='lightpink3'
    # From/Button Frame
    bFrame = Frame(mDashboard, bg="azure2", relief="flat", bd=1)
    bFrame.place(x=1, y=1, width=400, height=80)

    # Button
    sendButton = Button(bFrame, text="Send", width=10, font=("Calibre", 12), command = send)
    sendButton.grid(row=0, column=0, padx=10, pady=10)
    clearButton = Button(bFrame, text="Clear", width=10, font=("Calibre", 12))
    clearButton.grid(row=0, column=1, padx=10, pady=10)
    quitButton = Button(bFrame, text="Quit", width=10, font=("Calibre", 12))
    quitButton.grid(row=0, column=3, padx=10, pady=10)




    # Image Frame
    iFrame = Frame(mDashboard, bg="azure3", relief="flat", bd=1)
    iFrame.place(x=405, y=1, width=190, height=80)

    # To CC Frame
    ftcFrame =  Frame(mDashboard, bg="azure2", relief="flat", bd=1)
    ftcFrame.place(x=1, y=82, width=595, height=140)

    # Text Frame
    tFrame =  LabelFrame(mDashboard, text="Context", bg="azure2", bd=5, relief=RIDGE)
    tFrame.place(x=3, y=225, width=593, height=370)

    # Label
    Label(ftcFrame, text="From: ", font=("Calibre", 12), bg="azure2").grid(row=0, column=0, padx=3, pady=2, sticky=W)
    Label(ftcFrame, text="Password: ", font=("Calibre", 12), bg="azure2").grid(row=0, column=2, padx=3, pady=2, sticky=W)
    Label(ftcFrame, text="To: ", font=("Calibre", 12), bg="azure2").grid(row=1, column=0, padx=3, pady=2, sticky=W)
    Label(ftcFrame, text="Cc: ", font=("Calibre", 12), bg="azure2").grid(row=2, column=0, padx=3, pady=2, sticky=W)
    Label(ftcFrame, text="Subject", font=("Calibre", 12), bg="azure2").grid(row=4, column=0, padx=3, pady=10, sticky=W)

    # Entry Box
    fromEntry = Entry(ftcFrame, font=("Calibre", 12), width=25, textvariable = vFrom)
    fromEntry.grid(row=0, column=1, padx=3, pady=2, sticky=W)
    fromPassword = Entry(ftcFrame, font=("Calibre", 12), width=20, textvariable= vPassword, show='*')
    fromPassword.grid(row=0, column=3, padx=3, pady=2, sticky=W)

    toEntry = Entry(ftcFrame, font=("Calibre", 12), width=40, textvariable = vTo)
    toEntry.grid(row=1, column=1, padx=3, pady=2, sticky=W, columnspan=3)
    ccEntry = Entry(ftcFrame, font=("Calibre", 12), width=40, textvariable = vCc)
    ccEntry.grid(row=2, column=1, padx=3, pady=2, sticky=W, columnspan=3)
    subEntry = Entry(ftcFrame, font=("Calibre", 12), width=40, textvariable = vSubject)
    subEntry.grid(row=4, column=1, padx=3, pady=10, sticky=W, columnspan=3)

    # Text Box
    messageBox = Text(tFrame, height=20, width=71)
    messageBox.pack(expand=True)




# Login Function
def login():
    tempUser = UserName.get()
    tempPassword = Password.get()

    config = configparser.ConfigParser()
    config.read("C:\\Users\\Sayed\\Documents\\GitHub\\Python3\\TheEmail\\Config.ini")
    if tempUser in config:
        passwd = config[tempUser]['password']
        if passwd == tempPassword:
            noticeLable.configure(text="")
            mailDashboard()
        else:
            noticeLable.configure(text="incorrect password!")
    else:
        noticeLable.configure(text="user not found!")






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
global noticeLable
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
Label
Label(eFrame, text="", bg="honeydew2").grid(row=0, column=0)
Label(eFrame, text="", bg="honeydew2").grid(row=1, column=0)
Label(eFrame, text="user name: ", font=("Calabri", 12, "bold"), bg="honeydew2" ).grid(row=2, column=0)
Label(eFrame, text="", bg="honeydew2").grid(row=3, column=0)
Label(eFrame, text="password: ", font=("Calabri", 12, "bold"), bg="honeydew2").grid(row=4, column=0)

noticeLable = Label(eFrame, text="", bg="honeydew2", fg="red")
noticeLable.grid(row=5, column=1)

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
