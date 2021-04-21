from tkinter import *

window = Tk()
window.title("Hotdog Calculator")

value = 0 #value of all products in current order
total = 0 #value of all products in all orders

#it would be nice to have these in a dictionary, but that would be less readable for another programmer
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

register = [] #2 dimensional list that stores all previous orders



standardPady = 20 #the height of every box
standardPadx = 50 #the width of every box
columnSpacer = 1 #to move the keypad left or right 1 spot
rowSpacer = 2 #to move the keypad up or down 1 box

#display price
def price():
    global hotdogs
    global brats
    global hamburgers
    global fries
    global sodas
    global hotdogCost
    global bratCost
    global hamburgerCost
    global friesCost
    global sodaCost
    global value
    global valueString
    value = (hotdogs * hotdogCost) + (brats * bratCost) + (hamburgerCost * hamburgers) + (friesCost * fries) + (sodaCost + sodas) - 2
    string = str(value)
    valueString.set(string)

valueString = StringVar()  #setting up display string that updates very time .set() is called
valueStr = "Previous order: " + str(value)
valueString.set(valueStr)
priceDisplayer = Label(window, textvariable = valueString, padx = 40, pady = 20)   #displays value of products
priceDisplayer.grid(column = 0, row = 0, columnspan = 2)

totalString = StringVar()
totalStr = "Total (all orders): " + str(total)
totalString.set(totalStr)
totalDisplayer = Label(window, textvariable = totalString, padx = 40, pady = 20)
totalDisplayer.grid(column = 2, row = 0, columnspan = 2)

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
dogStringVar = StringVar() #setting up display string that updates very time .set() is called
string = str(hotdogs),"Hotdogs"
dogStringVar.set(string)
dogDisp = Label(window, textvariable = dogStringVar, padx = (standardPadx - 30), pady = standardPady)  #subtract from pacx, so it doesn't dilate as much in size in big numbers
dogSubtract = Button(window, text = "-1", padx = standardPadx, pady = standardPady, command = lambda: dog_Add(-1))
dogAdd.grid(column = 0, row = rowSpacer + 1)
dogDisp.grid(column = 0, row = rowSpacer + 2)
dogSubtract.grid(column = 0, row = rowSpacer + 3)

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
bratAdd.grid(column = 1, row = rowSpacer + 1)
bratDisp.grid(column = 1, row = rowSpacer + 2)
bratSubtract.grid(column = 1, row = rowSpacer+ 3)

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
burgerAdd.grid(column = 2, row = rowSpacer + 1)
burgerDisp.grid(column = 2, row = rowSpacer + 2)
burgerSubtract.grid(column = 2, row = rowSpacer + 3)

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
friesAdd.grid(column = 3, row = rowSpacer + 1)
friesDisp.grid(column = 3, row = rowSpacer + 2)
friesSubtract.grid(column = 3, row = rowSpacer + 3)

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
sodaAdd.grid(column = 4, row = rowSpacer + 1)
sodaDisp.grid(column = 4, row = rowSpacer + 2)
sodaSubtract.grid(column = 4, row = rowSpacer + 3)

#water section
def water_Add(num):  #Used to add dogs; can handle subtraction with negative numbers
    global waters
    global waterStringVar
    waters += num
    if waters < 0:
        waters = 0
    string = str(waters),"water"
    waterStringVar.set(string)

waterAdd = Button(window, text = "+1", padx = standardPadx, pady = standardPady, command = lambda: water_Add(1))  #add water
waterStringVar = StringVar()
string = str(waters),"water"
waterStringVar.set(string)
waterDisp = Label(window, textvariable = waterStringVar, padx = (standardPadx - 30), pady = standardPady)  #subtract from pacx, so it doesn't dilate as much in size in big numbers
waterSubtract = Button(window, text = "-1", padx = standardPadx, pady = standardPady, command = lambda: water_Add(-1))
waterAdd.grid(column = 5, row = rowSpacer + 1)
waterDisp.grid(column = 5, row = rowSpacer + 2)
waterSubtract.grid(column = 5, row = rowSpacer + 3)

def calculate_Current(): #calculate and add to list register
    global hotdogs
    global brats
    global hamburgers
    global fries
    global sodas
    global waters
    global register
    global value
    global total
    global totalString
    price()
    holder = [hotdogs, brats, hamburgers, fries, sodas, waters, str(value)]
    register.append(holder) #all values saved
    total += value
    string = "Total (all orders):",str(total)
    totalString.set(string)
    clear_Current()

calculate = Button(window, text = "Calculate and Add", padx = standardPadx * 2.9, pady = standardPady, command = lambda: calculate_Current())
calculate.grid(column = 3, columnspan = 3, row = rowSpacer + 4)

def clear_Current(): #set all current values to 0
    global hotdogs
    global brats
    global hamburgers
    global fries
    global sodas
    global waters
    hotdogs = 0
    brats = 0
    hamburgers = 0
    fries = 0
    sodas = 0
    waters = 0
    dog_Add(0) #call function to update the labels
    brat_Add(0)
    burger_Add(0)
    fries_Add(0)
    soda_Add(0)
    water_Add(0)

clear = Button(window, text = "Clear current", padx = standardPadx * 1.9, pady = standardPady, command = lambda: clear_Current())
clear.grid(column = 1, columnspan = 2, row = rowSpacer + 4)

def Exit(): #close
    window.destroy()
exit = Button(window, text = "Exit", padx = standardPadx * 0.9, pady = standardPady, command = lambda: Exit())
exit.grid(column = 0, row = rowSpacer + 4)

#display previous orders on register
def displayPrevious(): #open a new window and display results
    global register
    window2 = Tk()
    window2.title("Previous Orders")
    entry1 = Label(window2, text=textGen(register, 0), padx=standardPadx * 4, pady=standardPady)
    entry1.grid(column=0, row=0)
    entry2 = Label(window2, text=textGen(register, 1), padx=standardPadx * 4, pady=standardPady)
    entry2.grid(column=0, row=1)
    entry3 = Label(window2, text=textGen(register, 2), padx=standardPadx * 4, pady=standardPady)
    entry3.grid(column=0, row=2)
    entry4 = Label(window2, text=textGen(register, 3), padx=standardPadx * 4, pady=standardPady)
    entry4.grid(column=0, row=3)
    entry5 = Label(window2, text=textGen(register, 4), padx=standardPadx * 4, pady=standardPady)
    entry5.grid(column=0, row=4)
    entry6 = Label(window2, text=textGen(register, 5), padx=standardPadx * 4, pady=standardPady)
    entry6.grid(column=0, row=5)
    entry7 = Label(window2, text=textGen(register, 6), padx=standardPadx * 4, pady=standardPady)
    entry7.grid(column=0, row=6)
    entry8 = Label(window2, text=textGen(register, 7), padx=standardPadx * 4, pady=standardPady)
    entry8.grid(column=0, row=7)
    entry9 = Label(window2, text=textGen(register, 8), padx=standardPadx * 4, pady=standardPady)
    entry9.grid(column=0, row=8)
    entry0 = Label(window2, text=textGen(register, 9), padx=standardPadx * 4, pady=standardPady)
    entry0.grid(column=0, row=9)
    window2.mainloop()

def textGen(register, entryNum): #returns text in a nice manner from list
    if len(register) <= entryNum or len(register) == 0:
        return "No order"
    print(len(register))
    holder = register[entryNum]
    valOrder = ["Hotdogs;","Brats;","Hamburgers;","Fries;","Sodas;","Bottles;", "Total;"]
    formattedString = "Order",str(entryNum+1)
    for i in range(len(holder)):
        formattedString += holder[i],valOrder[i]
    return formattedString
previousOrders = Button(window, text = "View previous orders", padx = 35, pady = 18, command = lambda: displayPrevious())
previousOrders.grid(column = 4, row=0, columnspan =2)

window.mainloop()