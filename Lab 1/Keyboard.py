import tkinter as tk

board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

window = tk.Tk()
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

label = tk.Label(font=("bold", 20), height=2, padx=15)
label.pack(side=tk.TOP, anchor=tk.W)

clear_button = tk.Button(
    height= 3,
    width=10,
    text="Clear",
    command=lambda: clearWord()
)

clear_button.place(relx=1.0, y=15, anchor=tk.NE)

main_frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=5
)


main_frame.pack(expand=True, fill=tk.BOTH)

for i, row in enumerate(board):
    main_frame.rowconfigure(i, weight=1, minsize=100)
    for j in range(len(row)):
        main_frame.columnconfigure(j, weight=1, minsize=75)
        frame = tk.Frame(
            master=main_frame,
            borderwidth=1,
        )
        frame.grid(row=i, column=j)
        letter = board[i][j]

        button = tk.Button(
            master=frame,
            text=letter,
            font=("bold", 10),
            width=6,
            height=3,
            padx=15,
            pady=15,
            command=lambda l=letter: addLetter(l)
        )
        button.pack()

window.mainloop()

