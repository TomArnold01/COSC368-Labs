from tkinter import *
from tkinter.ttk import *
import random
import time
import csv

startTime = 0.0
width = [8, 16, 32]
distance = [64, 128, 256, 512]
reps = 8
testComplete = []
testFinished = False
numberOfReps = 0


def getSpecs():
    global testComplete, testFinished

    if len(testComplete) == 12:
        testFinished = True
    else:
        widthNumber = random.randint(0, 2)
        disNumber = random.randint(0, 3)
        test = [2, 0]

        while test in testComplete:
            widthNumber = random.randint(0, 2)
            disNumber = random.randint(0, 3)
            test = [widthNumber, disNumber]
        
        testComplete.append(test)
        return test


def getTotalSpan(testingNumber):
    global distance, width
    return distance[testingNumber[1]] + width[testingNumber[0]]


testingIndexSet = getSpecs()
totalSpan = getTotalSpan(testingIndexSet)
leftMargin = (600 - totalSpan) / 2  # change 1000 to the correct canvas size
rightMargin = leftMargin + totalSpan



master = Tk()
c = Canvas(master, width=600, height=600)
c.pack()

leftRect = c.create_rectangle(leftMargin, 0, leftMargin + width[testingIndexSet[0]], 610)
rightRect = c.create_rectangle(rightMargin - width[testingIndexSet[0]], 0, rightMargin, 610)

c.itemconfigure(leftRect, fill="blue")
c.itemconfigure(rightRect, fill="green")
master.mainloop()
