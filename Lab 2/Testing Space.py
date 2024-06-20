from tkinter import *
from tkinter.ttk import *
import random  
import time
import csv

board = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

TargetLetters = [
    ['a','z','r','f','g','q'],
    ['h','g','g','c','a','s'],
    ['y','u','i','j','n','b'],
    ['s','j','h','g','f','d'],
    ['w','e','r','d','s','d'],
    ['g','f','d','x','a','s']
]
Blocks = 6

word = ""

startTime = 0.0

window = Tk()
window.title("Keyboard")

letterSub = ""

name = ''
got_name = False

version = "Static"

startTest = False

main_frame = None 

def getTargetLetter():
    global letterSub, TargetLetters, Blocks     
    if got_name == False:
        getName("")

    elif Blocks==0:
        return "Test is completed!!!!"
    else:
        if len(TargetLetters[Blocks-1]) != 0:
            random.shuffle(TargetLetters[Blocks-1])
            letter = TargetLetters[Blocks-1][0]
            TargetLetters[Blocks-1] = TargetLetters[Blocks-1][1:]
            letterSub = letter
            return "Click: " + letter
        else:
            Blocks -= 1
            return getTargetLetter()


def addLetter(letter):
    global word, letterSub, startTime
    if got_name == False:
        getName(letter)

    if letter == " " or letter==letterSub:
        word = letter
        if version == "Dynamic":
            updateKeyboard()
        updateLabel()
        label.config(text = "Correct")
        updateTitle()
    else:
        if startTest == True:
            label.config(text = "Incorrect")


def clearWord():
    global word
    word = ""
    updateLabel()

def save_to_csv(name, condition, letter, total_time):
    with open('output.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, condition, letter,total_time])

def updateLabel():
    global letterSub, name   
    total_time = (time.time() - startTime) * 1000 
    save_to_csv(name, version, letterSub, total_time) 

def updateTitle():
    global startTime
    startTime = time.time()
    Title.config(text = getTargetLetter())

def updateEnterName():
    global name
    enterName.config(text = "Enter Your Name " + name)

def getName(letter):
    global name, startTest, got_name
    if startTest == False:
        name += letter
        updateEnterName()
    else:
        got_name = True

def start_test():
    global startTest, got_name, name
    if startTest == False:
        if len(name) == 0:
            name = "default User"
        startTest = True
        got_name = True
        enterName.config(text = "User: " + name)
        updateKeyboard()
        updateTitle()
    
def change_version(selectedVersion):
    global version
    if selectedVersion == "Static":
        version = "Static"
        versionLabel.config(text = "Version: " + version)
        
    else:
        version = "Dynamic"
        versionLabel.config(text = "Version: " + version)
        
def updateKeyboard():
    global main_frame, got_name
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    if got_name != False:
        random.shuffle(board)

    ammount = 10
    offset = 0
    for i in range(3):
        main_frame.rowconfigure(i, weight=1)
        for j in range(ammount):
            main_frame.columnconfigure(j, weight=1)            
            frame = Frame(main_frame, height=64, width=64)
            frame.pack_propagate(0) 
            frame.grid(row=i, column=j)
            
            letter = board[offset + j]
            
            button = Button(master=frame,
                            text=letter,
                            command=lambda l=letter: addLetter(l))
            button.pack(fill=BOTH, expand=1)
        
        if ammount==10:
            ammount=9
        elif ammount==9:
            ammount=7

        if offset==0:
            offset=10
        elif offset==10:
            offset=19

enterName = Label(text="Enter Your Name ", font=("bold", 20))
enterName.pack(side=TOP)

Title = Label(text=getTargetLetter(), font=("bold", 20))
Title.pack(side=TOP)

label = Label(font=("bold", 20))
label.pack(side=TOP)

clear_button = Button(text="Clear", command=lambda: clearWord())
clear_button.place(relx=1.0, y=1, anchor=NE)

Start_button = Button(text="Start", command=lambda: start_test())
Start_button.place(relx=1.0, y=25, anchor=NE)

Dynamic_version_button = Button(text="Dynamic", command=lambda: change_version("Dynamic"))
Dynamic_version_button.place(relx=1.0, y=50, anchor=NE)

static_version_button = Button(text="Static", command=lambda: change_version("Static"))
static_version_button.place(relx=1.0, y=75, anchor=NE)

versionLabel = Label(text = "Version: " + version)
versionLabel.place(y=80, anchor=NW)

main_frame = Frame(
    master=window,
    relief=RAISED,
    borderwidth=5
)
main_frame.pack(expand=True, fill=BOTH)

updateKeyboard()

window.mainloop()

