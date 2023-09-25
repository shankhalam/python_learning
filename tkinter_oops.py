from tkinter import *


class Demo:

    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.userlabel = Label(frame, text="Username")
        self.userlabel.grid(row=0, column=0)
        self.username = Entry(frame)
        self.username.grid(row=0, column=1)

        self.passlabel = Label(frame, text="Password")
        self.passlabel.grid(row=1, column=0)
        self.password = Entry(frame)
        self.password.grid(row=1, column=1)

        self.loginbutton = Button(frame, text="Login", command=self.login)
        self.loginbutton.grid(row=2, column=0)

        self.quitbutton = Button(frame, text="Exit", command=frame.quit)
        self.quitbutton.grid(row=2, column=1)

        self.loginlabel = Label(frame)
        self.loginlabel.grid(row=3, column=1)

    def login(self):
        self.loginlabel.config(text="Thank you for login")


root = Tk()
root.geometry("250x150")
d = Demo(root)

my_menu = Menu(root)
root.config(menu=my_menu)


file_menu = Menu(my_menu)
edit_menu = Menu(my_menu)

my_menu.add_cascade(label="File", menu=file_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)


file_menu.add_command(label="Add file")
file_menu.add_command(label="Save file")
edit_menu.add_command(label="Edit file")

status_bar = Label(text="This is current status.", anchor="w", relief="flat", background="white")
status_bar.pack(side="bottom", fill="x")

root.mainloop()
