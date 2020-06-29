from tkinter import *
from random import sample
from tkinter import messagebox as msgbx

root = Tk()
root.geometry("970x570")
root.title("Password Generator")
root.resizable(0, 0)
root.config(bg="black")
Label(root, text="Welcome to Password Generator", font=("Times", 35, "bold underline"), bg="black", fg="yellow").pack()
Label(root, text="Enter length of Password: ", font=("Times", 35, "bold"), bg="black", fg="white").place(x=70, y=110)
length_entry = Entry(root, font=("Helvetica", 25))
length_entry.place(width=300, height=50, x=610, y=115)
text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$&()<>{[}]/?"


def getpasswd():
    try:
        passwd = "".join(sample(text, int(length_entry.get())))
        passwd_entry.delete(0, END)
        passwd_entry.insert(END, passwd)
    except ValueError or UnboundLocalError:
        msgbx.showinfo("Error", "Please enter any number in range from 1 to 77")


Button(root, text="Get Password", bd=10, bg="grey", fg="black", command=getpasswd, font=("Times", 25, "bold")).place(x=290, y=200, height=80, width=320)
Label(root, text="Password: ", font=("Times", 35, "bold"), bg="black", fg="white").place(x=210, y=305)
passwd_entry = Entry(root, font=("Times", 35, "bold"))
passwd_entry.place(x=430, y=310)


def quitted():
    msgbx.showinfo("Thanks", "Thanks for Using Our Password Generator")
    quit()


Button(root, text="EXIT!!", bd=10, bg="grey", fg="black", command=quitted, font=("Times", 15, "bold")).place(x=370, y=380)
Label(root, text="©Program@Paras4902", bg="black", fg="white", font=("Helvetica", 12)).pack(side=BOTTOM, anchor=SE)
root.mainloop()
