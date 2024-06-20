from tkinter import *
from tkinter.ttk import *


def add_one():
    value.set(value.get()+1)


window = Tk()
value = IntVar(window, 0)
label = Label(window, textvariable=value)
label.pack()
label2 = Label(window)
label2.pack()
button = Button(window, text="Add one", command=add_one)

button.pack()
window.mainloop()
