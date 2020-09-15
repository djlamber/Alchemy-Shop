import helpers
import sys
import os.path
from constants import *
from DevTools import DevHelpers

#This is a tool that uses the terminal to add new location


def createLocation():
    Locations = helpers.InitLocations()
    Ingredients = helpers.InitIngredients()
    Ingredients.sort(key=lambda k: k.getName())
    Running = True
    print("=====Create Location=====")
    while Running:
        print("Type q to quit")

        # Select ID
        ID = input("Input ID: ")
        ID = DevHelpers.IDFormat(ID)
        option = ID.upper()
        if option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END":
            Running = False
            break
        setContinue = False
        for I in Locations:
            if I.getID() == ID:
                print("ID already taken")
                setContinue = True
                break
        if setContinue:
            continue

        # Select Name
        name = input("Input Name:")
        name = DevHelpers.NameFormat(name)

        # Select ImgDir
        img = input("Input Image directory: ")
        if not os.path.exists(img):
            print("Path does not exist, setting default")
            img = "sprites/UnknownWhite.png"

        # Select Color
        color = input("Input Color: ")
        if DevHelpers.checkColor(color) == None:
            print("Color not recognized, setting to random")
            color = helpers.randCol()
        else:
            color = DevHelpers.checkColor(color)

        # Select Ingredients
        while True:
            ingredients = input("Input Ingredients, separated by a comma - [ing1, ing2]\nType \"list\" for a list of ingredients: ")
            if ingredients.upper() == "LIST":
                DevHelpers.printIngredients(Ingredients)
            else:
                break

        # Select Drop Rates for Ingredients
        dropRates = []
        ingreList = ingredients.split(",")
        for i in range(len(ingreList)):
            ingreList[i] = DevHelpers.IDFormat(ingreList[i])
            if ingreList[i] == "_":
                continue
            while True:
                dropRate = input(str(ingreList[i]) + "\'s drop rate (0-1): ")
                if dropRate == "":
                    dropRate = 0.5
                try:
                    dropRate = float(dropRate)
                except ValueError:
                    print("That is not a float")
                if type(dropRate) == float:
                    if dropRate < 0:
                        dropRate = 0.5
                    break;
            # Select Drop Amounts for Ingredients
            while True:
                dropAmount = input(str(ingreList[i]) + "\'s drop amount: ")
                if dropAmount == "":
                    dropAmount = 1
                try:
                    dropAmount = int(dropAmount)
                except ValueError:
                    print("That is not a int")
                if type(dropAmount) == int:
                    if dropAmount < 0:
                        dropAmount = 1
                    break;
            dropRates.append([dropRate, dropAmount])

        # Select Prereqs
        prereqs = []
        for i in range(3):
            Type = input("Input prerequisite "+str(i+1)+" options:\n (Gold) (Potion) (None): ")

            # If prereq is gold
            if Type.upper() == "GOLD" or Type.upper() == "G":
                while(True):
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
                prereqs.append({"Gold":Value})

            # If prereq is Potion
            elif Type.upper() == "POTION" or Type.upper() == "P" or Type.upper() == "POT":
                potName = input("Potion Name: ")
                potName = DevHelpers.NameFormat(potName)
                potCol = input("Potion Color: ")
                potCol = DevHelpers.checkColor(potCol)
                potEff = input("Potion Effect: ")
                # potEff = DevHelpers.checkEffect(potEff)
                prereq = {"Potion": {"Name": potName, "Color": potCol, "Effect": potEff}}
            else:
                prereqs.append("None")

        # Create Location
        newLoc = helpers.Location(ID, name, img, color, ingreList, dropRates, prereqs[0], prereqs[1], prereqs[2])
        Locations.append(newLoc)
        ans = input("Sucessfully added to list, continue? (y/n): ")
        if ans.upper() != 'Y':
            Running = False
    helpers.saveLocations(Locations)