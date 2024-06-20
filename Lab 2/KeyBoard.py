from tkinter import *
from tkinter.ttk import *  

board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

window = Tk()
window.title("Keyboard")

word = ""

def addLetter(letter):
    global word
    word += letter
    updateLabel()

def clearWord():
    global word
    word = ""
    updateLabel()

def updateLabel():
    label.config(text = word)

Title = Label(text="tk",font=("bold", 20))
Title.pack(side=TOP)

label = Label(font=("bold", 20))
label.pack(side=TOP)

clear_button = Button(text="Clear", command=lambda: clearWord())
clear_button.place(relx=1.0, y=15, anchor=NE)

main_frame = Frame(
    master=window,
    relief=RAISED,
    borderwidth=5
)
main_frame.pack(expand=True, fill=BOTH)

for i, row in enumerate(board):
    
    for j in range(len(row)):
        
        frame = Frame(main_frame, height=64, width=64)
        frame.pack_propagate(0) # don't shrink
        frame.grid(row=i, column=j)
        letter = board[i][j]
        button = Button(master=frame,
                            text=letter, 
                            command=lambda l=letter: addLetter(l))
        button.pack(fill=BOTH, expand=1)
        

window.mainloop()

