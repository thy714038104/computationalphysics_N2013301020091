# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:31:21 2016

@author: thy
"""

# Simulates the two-dimensional Ising model using the Metropolis algorithm

import Tkinter, numpy, random, math

size = 50                           # number of sites in a lattice row 
squareWidth = 10                    # width of one site in pixels
canvasWidth = size * squareWidth    # full width of canvas in pixels
s = numpy.ones((size, size), int)   # 2D array of dipoles (1=up, -1=down)
running = False                     # will be true when simulation is running
M = []

theWindow = Tkinter.Tk()            # create the GUI window
theWindow.title("Ising Model")
theWindow.geometry('+50+50')       

theCanvas = Tkinter.Canvas(theWindow, width=canvasWidth, height=canvasWidth)
theCanvas.pack()
theImage = Tkinter.PhotoImage(width=canvasWidth, height=canvasWidth)
theCanvas.create_image((3, 3), image=theImage, anchor="nw", state="normal")
# The coordinates (3, 3) are a kludge to eliminate a mysterious offset that occurs otherwise.

# Function called when Start/Stop button is pressed:
def startStop():
    global running
    running = not running
    if running:
        goButton.config(text="Pause")
    else:
        goButton.config(text="Resume")

# Create the GUI controls:
controlFrame = Tkinter.Frame(theWindow)      
controlFrame.pack()                   
tLabel = Tkinter.Label(controlFrame, text="Temperature: ")
tLabel.pack(side="left")
tSlider = Tkinter.Scale(controlFrame, from_=0.01, to=10.0, resolution=0.01, length=120, orient="horizontal")
tSlider.pack(side="left")
tSlider.set(2.27)                              # set to critical temperature initially
spacer = Tkinter.Frame(controlFrame, width=40)
spacer.pack(side="left")
goButton = Tkinter.Button(controlFrame, text="Start", width=8, command=startStop)
goButton.pack(side="left")

# Function to color the square representing site (i,j):
def colorSquare(i, j):
    theColor = "#7000ff" if s[i,j]==1 else "#ffffff"    # purple and white
    theImage.put(theColor, to=(i*squareWidth,j*squareWidth,(i+1)*squareWidth,(j+1)*squareWidth))

# Function to calculate energy change upon hypothetical flip (with pbc):
def deltaE(i,j):
    leftS = s[size-1,j] if i==0 else s[i-1,j]
    rightS = s[0,j] if i==size-1 else s[i+1,j]
    topS = s[i,size-1] if j==0 else s[i,j-1]
    bottomS = s[i,0] if j==size-1 else s[i,j+1]
    return 2.0 * s[i,j] * (leftS + rightS + topS + bottomS)

# Main simulation "loop" schedules a call to itself upon completion:
def simulate():
    if running:
        T = tSlider.get()                    # get the current temperature
        for step in range(1000):             
            i = int(random.random()*size)    # choose a random row and column
            j = int(random.random()*size)
            eDiff = deltaE(i,j)
            if eDiff <= 0 or random.random() < math.exp(-eDiff/T):    # Metropolis!
                s[i,j] = -s[i,j]
                alls =0 + s[i,j]
                colorSquare(i, j)
                M.append(alls /250)
    theWindow.after(1,simulate)              # come back in one millisecond

# Initialize to a random array, and draw it as we go:
for i in range(size):
    for j in range(size):
        s[i,j] = 1 if random.random()<0.5 else -1
        colorSquare(i,j)

simulate()
theWindow.mainloop()


