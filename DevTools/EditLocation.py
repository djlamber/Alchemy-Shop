import helpers
import config
import sys
import os.path
from DevTools import DevHelpers

def editLocName(loc, name):
    print("Current name for ["+str(loc.getID())+"] : " + str(name))
    newName = input("Input new name or null to go back: ")
    if newName == "":
        return name
    else:
        return DevHelpers.NameFormat(newName)

def editLocImgLoc(loc, img):
    while True:
        print("Current Image Location for [" + str(loc.getID()) + "] : " + str(img))
        newImg = input("Input new Image location or null to go back: ")
        if newImg == "":
            return img
        else:
            if not os.path.exists(newImg):
                print("Path does not exist")
            else:
                return newImg

def editLocIngreAdd(loc, ingres, dropRates):
    while True:
        cont = False
        print("\nInput ingredient to add")
        print("Type \'list\' to list current ingredients | "
              "Type \'listAll\' to list all ingredients")
        print("Type null to go back")
        ingre = input().upper()
        if ingre == "":
            return
        if ingre == "LIST":
            lis = ""
            for i in ingres:
                lis = lis + "[" + str(i) + "]\n"
            print("\n" + lis)
            continue
        if ingre == "LISTALL" or ingre == "LIST ALL" or ingre == "LA":
            DevHelpers.printIngredients(config.Ingredients)
            continue
        ingre = DevHelpers.IDFormat(ingre)
        for i in ingres:
            if ingre == i:
                print("Ingredient already exists\n")
                cont = True
                break
        if cont:
            continue
        ingres.append(ingre)

        while True:
            dropRate = input(str(ingre) + "\'s drop rate (0-1): ")
            if dropRate == "":
                dropRate = 0.5
            try:
                dropRate = float(dropRate)
            except ValueError:
                print("That is not a float")
            if type(dropRate) == float:
                if dropRate < 0:
                    dropRate = 0.5
                break
        # Select Drop Amounts for Ingredients
        while True:
            dropAmount = input(str(ingre) + "\'s drop amount: ")
            if dropAmount == "":
                dropAmount = 1
            try:
                dropAmount = int(dropAmount)
            except ValueError:
                print("That is not a int")
            if type(dropAmount) == int:
                if dropAmount < 0:
                    dropAmount = 1
                break
        dropRates.append([dropRate, dropAmount])
        print("Added " + str(ingre) +" to [" + str(loc.getID()) +"]\n")


def editLocIngreRemove(loc, ingres, dropRates):
    while True:
        cont = True
        print("\nInput ingredient to remove")
        print("Type \'list\' to list current ingredients")
        print("Type null to go back")
        ingre = input().upper()
        if ingre == "":
            return
        if ingre == "LIST":
            lis = ""
            for i in ingres:
                lis = lis + "[" + str(i) + "]\n"
            print("\n" + lis)
            continue
        ingre = DevHelpers.IDFormat(ingre)
        for i in range(len(ingres)):
            if ingre == loc.getIngredients()[i]:
                choice = input ("Are you sure you want to delete [" + ingre +"]? (y/n) :")
                if choice.upper() == "Y":
                    ingres.pop(i)
                    dropRates.pop(i)

                cont = False
                break
        if cont :
            print("Ingredient could not be found")


def editLocIngre(loc, ingres, dropRates):
    while True:
        print("Select option for editing [" + loc.getID() +"]'s ingredients")
        print("Add | remove | list | back")
        option = input().upper()
        if option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END" or option == "BACK" or option == "B" or option == "":
            return ingres
        if option == "LIST" or option == "L":
            lis = ""
            for i in ingres:
                lis = lis + "[" + str(i) + "]\n"
            print("\n" + lis)
        if option == "ADD" or option == "A":
            editLocIngreAdd(loc, ingres, dropRates)
        if option == "REMOVE" or option == "R":
            editLocIngreRemove(loc, ingres, dropRates)

def editLocColor(loc, color):
    while True:
        print("Current Color for [" + str(loc.getID()) + "] : " + str(color))
        newColor = input("Input new Color or null to go back: ")
        if newColor == "":
            return color
        else:
            colorCheck = DevHelpers.checkColor(newColor)
            if colorCheck == None:
                print("Color is not valid")
            else:
                return colorCheck

def editLocDropRates(loc, value):
    print(value)
    while True:
        leaveFirst = True
        locIngs = loc.getIngredients()
        locDrops = loc.getDropRates()
        rate = None
        index = -1
        while leaveFirst:
            print("Current Drop rates for for [" + str(loc.getID()) + "]")
            for i in range(len(loc.getIngredients())):
                rate = locDrops[i]
                print("[" + str(locIngs[i])+ "] : [" + str(value[i][0]) + "|" + str(value[i][1]) + "]" )
            ingre = input("Select ingredient to edit or null to go back: ")
            if ingre == "":
                return value
            for i in range(len(loc.getIngredients())):
                if DevHelpers.IDFormat(ingre) == loc.getIngredients()[i]:
                    leaveFirst = False
                    index = i
                    break
        print("Select \'rate\' dropped or \'amount\' dropped for [" + str(locIngs[index])+ "] : [" + str(value[index][0]) + "|" + str(value[index][1]) + "]")
        print("Type null to go back: ")
        opt = input().upper()
        if opt == "":
            continue
        #TODO add int and float checks
        if opt == "RATE" or opt == "R":
            r = float(input("Input new rate: "))
            if r < 0:
                r = 0
            value[index][0] = r
        if opt == "AMOUNT" or opt == "A":
            a = int(input("Input new amount: "))
            if a < 0:
                a = 0
            value[index][1] = a





def editLocPrereq(loc, prereq):
    while True:
        print("Current prerequisites for [" + str(loc.getID()) + "] :")
        print("Prereq 1: " + str(prereq[0]) + " | Prereq 2: " + str(prereq[1]) + " | Prereq 3: " + str(prereq[2]) )
        selection = input("Select Effect to edit or null to go back: ").upper()
        if selection == "":
            return prereq
        else:
            if selection == "1" or selection == "PREREQ1" or selection == "PREERQ 1":
                prereq[0] = changePrereq(loc, prereq[0])
            if selection == "2" or selection == "PREREQ2" or selection == "PREREQ 2":
                prereq[1] = changePrereq(loc, prereq[1])
            if selection == "3" or selection == "PREREQ3" or selection == "PREREQ 3":
                prereq[2] = changePrereq(loc, prereq[2])

def changePrereq(ingre, prereq):
    print("\nSelect what to change the prerequisite to [" + str(ingre.getID()) + "]")
    print("Gold | Potion | None | Current prereq: "+ str(prereq))
    print("Type null to go back")
    newReq = input().upper()
    if newReq == "":
        return prereq
    if newReq == "G" or newReq == "GOLD":
        while (True):
            Value = input("Value: ")
            if Value == "":
                Value = 1
            try:
                Value = int(Value)
            except ValueError:
                print("That is not a integer")
            if type(Value) == int:
                if Value < 0:
                    Value = 1
                break;
        prereq = {"Gold": Value}
    if newReq == "P" or newReq == "POTION":
        potName = input("Potion Name: ")
        potName = DevHelpers.NameFormat(potName)
        potCol = input("Potion Color: ")
        potCol = DevHelpers.checkColor(potCol)
        prereq = {"Potion": {"Name": potName, "Color": potCol}}

    if newReq == "N" or newReq == "NONE":
        prereq = "None"
    print(prereq)
    return prereq





def editLocation():
    Locations = helpers.InitLocations()
    config.Ingredients = helpers.InitIngredients()
    config.Ingredients.sort(key=lambda k: k.getName())
    Running = True
    while Running:
        print("\n=====Edit Location=====")
        while(Running):
            print("Type q to quit")
            print("Select Location ID to Edit:")
            DevHelpers.printLocations(Locations)
            entry = input()
            option = entry.upper()
            if option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END" or option == "":
                Running = False
                break

            setToBreak = False
            locID = DevHelpers.IDFormat(option)
            for i in Locations:
                if i.getID() == locID:
                    loc = i
                    setToBreak = True
                    break
            if setToBreak:
                break
            print("Location not found")
        if not Running:
            break

        #get vars ready
        name = loc.getName()
        img = loc.getImgLoc()
        color = loc.getColor()
        locIngre = loc.getIngredients()
        dropRates = loc.getDropRates()
        prereq = [loc.getPrereq1(), loc.getPrereq2(), loc.getPrereq3()]
        editingLoc = True
        while(editingLoc):
            print("\nSelect Attribute to Edit for [" + str(loc.getID()) + "]")
            print("Type s to save and continue, q to save and quit")
            print("Name | ImageLocation | Color | Ingredients | Drop Rate | Prerequisite")
            attrib = input().upper()
            if attrib == "" or attrib == "Q" or attrib == "EXIT" or attrib == "QUIT" or attrib == "STOP" or attrib == "END":
                newLoc = helpers.Location(loc.getID(), name, img, color, locIngre, dropRates, prereq[0], prereq[1],prereq[2])
                Locations.append(newLoc)
                helpers.saveLocations(Locations)
                Locations = helpers.InitLocations()
                print("Successfully saved")
                editingLoc = False
                break
            if attrib == "NAME" or attrib == "N":
                name = editLocName(loc, name)
            if attrib == "IMAGELOCATION" or attrib == "IMAGE" or attrib == "IMG":
                img = editLocImgLoc(loc, img)
            if attrib == "COLOR" or attrib == "C":
                color = editLocColor(loc, color)
            if attrib == "INGREDIENTS" or attrib == "INGRE" or attrib == "ING":
                locIngre = editLocIngre(loc, locIngre, dropRates)
            if attrib == "DROPRATE" or attrib == "DROP RATE" or attrib == "DROP" or attrib == "D":
                dropRates = editLocDropRates(loc, dropRates)
            if attrib == "PREREQUISITE" or attrib == "PREREQ" or attrib == "PRE" or attrib == "P":
                prereq = editLocPrereq(loc, prereq)
                print(prereq)
            if attrib == "SAVE" or attrib == "S":
                newLoc = helpers.Location(loc.getID(), name, img, color, locIngre, dropRates, prereq[0], prereq[1], prereq[2])
                Locations.append(newLoc)
                helpers.saveLocations(Locations)
                Locations = helpers.InitLocations()
                print("Successfully saved")
