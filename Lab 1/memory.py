import tkinter as tk

window = tk.Tk()
string = ""
def handle_keypress(event):
    print(event.char)

def handle_click(event, string):

    print("The button was clicked!\n")
    string += "a"
    print(string)





button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)

button.pack()


window.mainloop()

