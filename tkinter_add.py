from tkinter import *


def add_num():
    n1 = int(num1.get())
    n2 = int(num2.get())

    result = n1 + n2
    result = str(result)
    display.config(text="The sum is " + result)


root = Tk()
root.geometry("250x100")

num1 = Entry()
num2 = Entry()
num1.pack()
num2.pack()

button = Button(root, text="Add", command=add_num)
button.pack()

display = Label(root)
display.pack()

root.mainloop()
