from tkinter import *


root = Tk()
root.geometry("970x570")
root.title("Password Generator")
root.wm_iconbitmap("password.ico")
root.resizable(0, 0)
Label(root, text="Welcome to Password Generator", font=("Times", 35, "bold underline"), fg="green").pack()
Label(root, text="Enter length of Password: ", font=("Times", 15, "bold")).place(x=10, y=110)
length_entry = Entry(root, font=("Helvetica", 25), bd=10)
length_entry.place(width=300, height=48, x=240, y=105)
lowercase = IntVar()
lcbtn = Checkbutton(root, text="Lowercase", variable=lowercase, font=("Times", 15, "bold"))
lcbtn.place(x=10, y=150)
uppercase = IntVar()
lcbtn = Checkbutton(root, text="Uppercase", variable=uppercase, font=("Times", 15, "bold"))
lcbtn.place(x=160, y=150)
numbers = IntVar()
lcbtn = Checkbutton(root, text="Numbers", variable=numbers, font=("Times", 15, "bold"))
lcbtn.place(x=310, y=150)
spchar = IntVar()
lcbtn = Checkbutton(root, text="Special Characters", variable=spchar, font=("Times", 15, "bold"))
lcbtn.place(x=460, y=150)
Label(root, text="Password:", font="Helvetica 35 bold").place(x=10, y=310)
passwd_entry = Entry(root, font=("Times", 35, "bold"), bd=10)
passwd_entry.place(x=270, y=310)


def getpasswd():
    from random import sample
    from tkinter import messagebox as msgbx

    def gettext():
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "0123456789"
        spc = "!@#$&()<>{[}]/?"
        if lowercase.get() == 0 and uppercase.get() == 0 and numbers.get() == 0 and spchar.get() == 0:
            text = lower + upper + nums + spc
        elif lowercase.get() == 0 and uppercase.get() == 0 and numbers.get() == 0 and spchar.get() == 1:
            text = spc
        elif lowercase.get() == 0 and uppercase.get() == 0 and numbers.get() == 1 and spchar.get() == 0:
            text = nums
        elif lowercase.get() == 0 and uppercase.get() == 0 and numbers.get() == 1 and spchar.get() == 1:
            text = nums + spc
        elif lowercase.get() == 0 and uppercase.get() == 1 and numbers.get() == 0 and spchar.get() == 0:
            text = upper
        elif lowercase.get() == 0 and uppercase.get() == 1 and numbers.get() == 0 and spchar.get() == 1:
            text = upper + spc
        elif lowercase.get() == 0 and uppercase.get() == 1 and numbers.get() == 1 and spchar.get() == 0:
            text = upper + nums
        elif lowercase.get() == 0 and uppercase.get() == 1 and numbers.get() == 1 and spchar.get() == 1:
            text = upper + nums + spc
        elif lowercase.get() == 1 and uppercase.get() == 0 and numbers.get() == 0 and spchar.get() == 0:
            text = lower
        elif lowercase.get() == 1 and uppercase.get() == 0 and numbers.get() == 0 and spchar.get() == 1:
            text = lower + spc
        elif lowercase.get() == 1 and uppercase.get() == 0 and numbers.get() == 1 and spchar.get() == 0:
            text = lower + nums
        elif lowercase.get() == 1 and uppercase.get() == 0 and numbers.get() == 1 and spchar.get() == 1:
            text = lower + nums + spc
        elif lowercase.get() == 1 and uppercase.get() == 1 and numbers.get() == 0 and spchar.get() == 0:
            text = lower + upper
        elif lowercase.get() == 1 and uppercase.get() == 1 and numbers.get() == 0 and spchar.get() == 1:
            text = lower + upper + spc
        elif lowercase.get() == 1 and uppercase.get() == 1 and numbers.get() == 1 and spchar.get() == 0:
            text = lower + upper + nums
        else:
            text = lower + upper + nums + spc

        return text

    try:
        passwd = "".join(sample(gettext(), int(length_entry.get())))
        passwd_entry.delete(0, END)
        passwd_entry.insert(END, passwd)
    except ValueError or UnboundLocalError:
        msgbx.showinfo("Error", "Please enter any number in range from 1 to 77")


def copytxt():
    from pyperclip import copy
    copy(passwd_entry.get())


Button(root, text="→Get Password←", command=getpasswd, bd=10, font="Helvetica 15 bold").place(x=370, y=200, height=80, width=300)
Button(root, text="Copy", command=copytxt, bd=10, bg="blue", fg="white", font="Helvetica 15 bold").place(x=800, y=320)
Label(root, text="@Paras4902", font=("Times", 15, "bold")).pack(side=BOTTOM, anchor=E)

root.mainloop()
