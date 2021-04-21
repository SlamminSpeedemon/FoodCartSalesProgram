from tkinter import *

window = Tk()
window.title("Hotdog Calculator")

value = 0 #value of all products

global hotdogs
hotdogs = 0 #number of hotdogs orders
hotdogCost = 2.50

brats = 0 #number of brats orders
bratCost = 3.50

hamburgers = 0 #number of hamburgers orders
hamburgerCost = 5.00

fries = 0 #number of fries orders
friesCost = 2.00

sodas = 0 #number of sodas
sodaCost = 2.00

waters = 0 #number of waters; no cost because water is free

priceDisplayer = Label(window, text = str(value), padx = 40, pady = 20)   #displays value of products
priceDisplayer.grid(column = 0, row = 0)

#hot dog section
def dog_Add(num):  #Used to add dogs; can handle subtraction with negative numbers
    global hotdogs
    global dogStringVar
    hotdogs += num
    string = str(hotdogs),"Hotdogs"
    dogStringVar.set(string)
    return

standardPady = 20 #the height of every box
standardPadx = 50 #the width of every box

dogAdd = Button(window, text = "+1", padx = standardPadx, pady = standardPady, command = lambda: dog_Add(1))  #add dog
dogStringVar = StringVar()
dogDisp = Label(window, textvariable = dogStringVar, padx = (standardPadx - 30), pady = standardPady)  #subtract from pacx, so it doesn't dilate as much in size in big numbers
dogSubtract = Button(window, text = "-1", padx = standardPadx, pady = standardPady, command = lambda: dog_Add(-1))
dogAdd.grid(column = 0, row = 1)
dogDisp.grid(column = 0, row = 2)
dogSubtract.grid(column = 0, row = 3)






window.mainloop()