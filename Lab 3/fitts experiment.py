from tkinter import *
from tkinter.ttk import *
import random
import time
import csv

startTime = 0.0
width = [25, 100, 125, 90, 70, 50, 150, 175, 80, 30, 90, 25]
distance = [
    480,
    450,
    425,
    400,
    350,
    325,
    300,
    250,
    200,
    175,
    150,
    30,
]
reps = [1, 3, 5]
testComplete = []
testFinished = False
numberOfReps = 0


def getSpecs():
    global testComplete, testFinished

    if len(testComplete) == 12:
        testFinished = True
    else:
        number = random.randint(0, 11)
        while number in testComplete:
            number = random.randint(0, 11)
        testComplete.append(number)
        return number


def getTotalSpan(testingNumber):
    global distance, width
    return distance[testingNumber] + width[testingNumber]


testingNumber = getSpecs()
totalSpan = getTotalSpan(testingNumber)
leftMargin = (500 - totalSpan) / 2
rightMargin = leftMargin + totalSpan


def endTest():
    global c
    c.delete(rightRect)
    c.delete(leftRect)
    c.create_text(100, 100, text="End of Test", anchor="center", font="bold")


def resetTest():
    global testingNumber, totalSpan, leftMargin, rightMargin, width, distance
    testingNumber = getSpecs()
    if testFinished == False:
        totalSpan = getTotalSpan(testingNumber)
        leftMargin = (500 - totalSpan) / 2
        rightMargin = leftMargin + totalSpan
        c.coords(leftRect, leftMargin, 0, leftMargin + width[testingNumber], 510)
        c.coords(rightRect, rightMargin - width[testingNumber], 0, rightMargin, 510)
    else:
        endTest()


def handleClick(rectMain, otherRec):
    global numberOfReps, startTime, testingNumber, reps
    current_color = c.itemcget(rectMain, "fill")
    if current_color == "green":
        if startTime == 0.0:
            startTime = time.time()
        c.itemconfigure(rectMain, fill="blue")
        c.itemconfigure(otherRec, fill="green")
        if numberOfReps != reps[testingNumber % 3]:
            numberOfReps += 1
        else:
            total_time = (time.time() - startTime) * 1000
            save_to_csv(testingNumber, reps[testingNumber % 3] + 1, total_time)
            numberOfReps = 0
            startTime = 0.0
            resetTest()


def save_to_csv(testingNumber, selectionNumber, total_time):
    formatted_total_time = "{:.2f}".format(total_time)
    with open("output.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "User",
                distance[testingNumber],
                width[testingNumber],
                selectionNumber,
                formatted_total_time,
            ]
        )


master = Tk()
c = Canvas(master, width=500, height=500)
c.pack()

leftRect = c.create_rectangle(leftMargin, 0, leftMargin + width[testingNumber], 510)
rightRect = c.create_rectangle(rightMargin - width[testingNumber], 0, rightMargin, 510)

c.tag_bind(leftRect, "<Button-1>", lambda event: handleClick(leftRect, rightRect))
c.tag_bind(rightRect, "<Button-1>", lambda event: handleClick(rightRect, leftRect))

c.itemconfigure(leftRect, fill="blue")
c.itemconfigure(rightRect, fill="green")
master.mainloop()
