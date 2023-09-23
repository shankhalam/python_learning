from tkinter import *


def selected():
    sugar = sugar_var.get()
    ice = ice_var.get()
    cream = cream_var.get()

    if sugar:
        sugar = "Sugar"
    else:
        sugar = "Not Selected"
    if ice:
        ice = "Ice"
    else:
        ice = "Not Selected"
    if cream:
        cream = "Cream"
    else:
        cream = "Not Selected"

    label.config(text="The Beverage options  you want was: \n" + sugar + "\n" + ice + "\n" + cream)


root = Tk()
root.geometry("250x150")

sugar_var = BooleanVar()
ice_var = BooleanVar()
cream_var = BooleanVar()
# Checkbox
sugar = Checkbutton(root, text="Sugar", variable=sugar_var, command=selected)
ice = Checkbutton(root, text="Ice", variable=ice_var, command=selected)
cream = Checkbutton(root, text="Cream", variable=cream_var, command=selected)

sugar.pack()
ice.pack()
cream.pack()

label = Label(root)
label.pack()

root.mainloop()
