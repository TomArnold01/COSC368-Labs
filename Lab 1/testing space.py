from tkinter import *
from tkinter.ttk import *


def change(the_value, n):
    the_value.set(the_value.get()+n)


def add_one():
    count.set(count.get()+1)


window = Tk()
value = IntVar(window, 0)
count = IntVar(window, 0)
label = Label(window, textvariable=value)
label1 = Label(window, textvariable=count)
label1.pack()
label.pack()
button1 = Button(window, text="Add one", command=add_one)

button = Button(window, text="Left +1, Right -1")
button.bind("<Button-1>", lambda event: change(value, 1))

button.bind("<Button-3>", lambda event: change(value, -1))
button1.pack()
button.pack()
window.mainloop()
