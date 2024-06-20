from tkinter import *
from tkinter.ttk import *
import random
import time
import csv

startTime = 0.0
width = [8, 16, 32]
distance = [64, 128, 256, 512]
reps = 7
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
        test = [widthNumber, disNumber]

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


def endTest():
    global c
    c.delete(rightRect)
    c.delete(leftRect)
    c.create_text(100, 100, text="End of Test", anchor="center", font="bold")


def resetTest():
    global testingIndexSet, startTime, totalSpan, leftMargin, rightMargin, width, distance
    testingIndexSet = getSpecs()
    if testFinished == False:
        
        totalSpan = getTotalSpan(testingIndexSet)
        leftMargin = (600 - totalSpan) / 2
        rightMargin = leftMargin + totalSpan
        c.coords(leftRect, leftMargin, 0, leftMargin + width[testingIndexSet[0]], 610)
        c.coords(rightRect, rightMargin - width[testingIndexSet[0]], 0, rightMargin, 610)
        startTime = time.time()
    else:
        endTest()


def handleClick(rectMain, otherRec):
    global numberOfReps, startTime, testingIndexSet, reps
    current_color = c.itemcget(rectMain, "fill")
    
    if current_color == "green":
        c.itemconfigure(rectMain, fill="blue")
        c.itemconfigure(otherRec, fill="green")
        total_time = (time.time() - startTime)
        save_to_csv(testingIndexSet, 8, total_time)
        startTime = 0.0
        if numberOfReps != reps:
            numberOfReps += 1
            startTime = time.time()
        else:
            numberOfReps = 0
            resetTest()


def save_to_csv(testingIndexSet, selectionNumber, total_time):
    formatted_total_time = "{:.2f}".format(total_time)
    with open("output.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "User",
                distance[testingIndexSet[1]],
                width[testingIndexSet[0]],
                selectionNumber,
                formatted_total_time,
            ]
        )


master = Tk()
c = Canvas(master, width=600, height=600)
c.pack()

leftRect = c.create_rectangle(leftMargin, 0, leftMargin + width[testingIndexSet[0]], 610)
rightRect = c.create_rectangle(rightMargin - width[testingIndexSet[0]], 0, rightMargin, 610)

c.tag_bind(leftRect, "<Button-1>", lambda event: handleClick(leftRect, rightRect))
c.tag_bind(rightRect, "<Button-1>", lambda event: handleClick(rightRect, leftRect))

c.itemconfigure(leftRect, fill="blue")
c.itemconfigure(rightRect, fill="green")
startTime = time.time()
master.mainloop()
