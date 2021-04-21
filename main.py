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

standardPady = 20 #the height of every box
standardPadx = 50 #the width of every box

#hot dog section
def dog_Add(num):  #Used to add dogs; can handle subtraction with negative numbers
    global hotdogs
    global dogStringVar
    hotdogs += num
    if hotdogs < 0:
        hotdogs = 0
    string = str(hotdogs),"Hotdogs"
    dogStringVar.set(string)

dogAdd = Button(window, text = "+1", padx = standardPadx, pady = standardPady, command = lambda: dog_Add(1))  #add dog
dogStringVar = StringVar()
string = str(hotdogs),"Hotdogs"
dogStringVar.set(string)
dogDisp = Label(window, textvariable = dogStringVar, padx = (standardPadx - 30), pady = standardPady)  #subtract from pacx, so it doesn't dilate as much in size in big numbers
dogSubtract = Button(window, text = "-1", padx = standardPadx, pady = standardPady, command = lambda: dog_Add(-1))
dogAdd.grid(column = 0, row = 1)
dogDisp.grid(column = 0, row = 2)
dogSubtract.grid(column = 0, row = 3)

#brat section
def brat_Add(num):  #Used to add dogs; can handle subtraction with negative numbers
    global brats
    global bratStringVar
    brats += num
    if brats < 0:
        brats = 0
    string = str(brats),"Brats"
    bratStringVar.set(string)

bratAdd = Button(window, text = "+1", padx = standardPadx, pady = standardPady, command = lambda: brat_Add(1))  #add brats
bratStringVar = StringVar()
string = str(brats),"Brats"
bratStringVar.set(string)
bratDisp = Label(window, textvariable = bratStringVar, padx = (standardPadx - 30), pady = standardPady)  #subtract from pacx, so it doesn't dilate as much in size in big numbers
bratSubtract = Button(window, text = "-1", padx = standardPadx, pady = standardPady, command = lambda: brat_Add(-1))
bratAdd.grid(column = 1, row = 1)
bratDisp.grid(column = 1, row = 2)
bratSubtract.grid(column = 1, row = 3)

#hamburger section
def burger_Add(num):  #Used to add dogs; can handle subtraction with negative numbers
    global hamburgers
    global burgerStringVar
    hamburgers += num
    if hamburgers < 0:
        hamburgers = 0
    string = str(hamburgers),"burger"
    burgerStringVar.set(string)

burgerAdd = Button(window, text = "+1", padx = standardPadx, pady = standardPady, command = lambda: burger_Add(1))  #add hamburgers
burgerStringVar = StringVar()
string = str(hamburgers),"burger"
burgerStringVar.set(string)
burgerDisp = Label(window, textvariable = burgerStringVar, padx = (standardPadx - 30), pady = standardPady)  #subtract from pacx, so it doesn't dilate as much in size in big numbers
burgerSubtract = Button(window, text = "-1", padx = standardPadx, pady = standardPady, command = lambda: burger_Add(-1))
burgerAdd.grid(column = 2, row = 1)
burgerDisp.grid(column = 2, row = 2)
burgerSubtract.grid(column = 2, row = 3)

#fries section
def fries_Add(num):  #Used to add dogs; can handle subtraction with negative numbers
    global fries
    global friesStringVar
    fries += num
    if fries < 0:
        fries = 0
    string = str(fries),"Fries"
    friesStringVar.set(string)

friesAdd = Button(window, text = "+1", padx = standardPadx, pady = standardPady, command = lambda: fries_Add(1))  #add fries
friesStringVar = StringVar()
string = str(fries),"Fries"
friesStringVar.set(string)
friesDisp = Label(window, textvariable = friesStringVar, padx = (standardPadx - 30), pady = standardPady)  #subtract from pacx, so it doesn't dilate as much in size in big numbers
friesSubtract = Button(window, text = "-1", padx = standardPadx, pady = standardPady, command = lambda: fries_Add(-1))
friesAdd.grid(column = 3, row = 1)
friesDisp.grid(column = 3, row = 2)
friesSubtract.grid(column = 3, row = 3)

#soda section
def soda_Add(num):  #Used to add dogs; can handle subtraction with negative numbers
    global sodas
    global sodaStringVar
    sodas += num
    if sodas < 0:
        sodas = 0
    string = str(sodas),"Sodas"
    sodaStringVar.set(string)

sodaAdd = Button(window, text = "+1", padx = standardPadx, pady = standardPady, command = lambda: soda_Add(1))  #add soda
sodaStringVar = StringVar()
string = str(sodas),"Sodas"
sodaStringVar.set(string)
sodaDisp = Label(window, textvariable = sodaStringVar, padx = (standardPadx - 30), pady = standardPady)  #subtract from pacx, so it doesn't dilate as much in size in big numbers
sodaSubtract = Button(window, text = "-1", padx = standardPadx, pady = standardPady, command = lambda: soda_Add(-1))
sodaAdd.grid(column = 4, row = 1)
sodaDisp.grid(column = 4, row = 2)
sodaSubtract.grid(column = 4, row = 3)

#water section
def water_Add(num):  #Used to add dogs; can handle subtraction with negative numbers
    global waters
    global waterStringVar
    waters += num
    if waters < 0:
        waters = 0
    string = str(waters),"water"
    waterStringVar.set(string)

waterAdd = Button(window, text = "+1", padx = standardPadx, pady = standardPady, command = lambda: water_Add(1))  #add dog
waterStringVar = StringVar()
string = str(waters),"water"
waterStringVar.set(string)
waterDisp = Label(window, textvariable = waterStringVar, padx = (standardPadx - 30), pady = standardPady)  #subtract from pacx, so it doesn't dilate as much in size in big numbers
waterSubtract = Button(window, text = "-1", padx = standardPadx, pady = standardPady, command = lambda: water_Add(-1))
waterAdd.grid(column = 5, row = 1)
waterDisp.grid(column = 5, row = 2)
waterSubtract.grid(column = 5, row = 3)

window.mainloop()