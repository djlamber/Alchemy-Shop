import helpers
import sys
import os.path

#This is a tool that uses the terminal to add new ingredients

def checkColor(color):
    if type(color) == str:
        if color == "WHITE":
            return True
        if color == "SILVER":
            return True
        if color == "GRAY":
            return True
        if color == "BLACK":
            return True
        if color == "RED":
            return True
        if color == "MAROON":
            return True
        if color == "YELLOW":
            return True
        if color == "OLIVE":
            return True
        if color == "LIME":
            return True
        if color == "GREEN":
            return True
        if color == "AQUA":
            return True
        if color == "TEAL":
            return True
        if color == "BLUE":
            return True
        if color == "NAVY":
            return True
        if color == "FUCHSIA":
            return True
        if color == "PURPLE":
            return True
    else:
        RGB = color.split(",")
    return True # color is equal

Locations = helpers.InitLocations()
Ingredients = helpers.InitIngredients()
Ingredients.sort(key=lambda k: k.getName())
Running = True
while(Running):
    ID = input("Input ID: ")
    ID = helpers.IDFormat(ID)
    setContinue = False
    for I in Locations:
        if I.getID() == ID:
            print("ID already taken")
            setContinue = True
            break
    if setContinue:
        continue
    name = input("Input Name:")
    name = helpers.NameFormat(name)
    img = input("Input Image directory: ")
    if not os.path.exists(img):
        print("Path does not exist, setting default")
        img = "sprites/UnknownWhite.png"
    color = input("Input Color: ")
    if not checkColor(color.upper()):
        print("Color not recognized, setting to default")
        color = "WHITE"
    while True:
        ingredients = input("Input Ingredients, separated by a comma - [ing1, ing2]\nType \"list\" for a list of ingredients: ")
        if ingredients == "list":
            igList = ""
            x = 0
            for i in Ingredients:
                ingStr = "["+str(i.getID())+"], "
                ingStrLen = len(ingStr)
                igList = igList + ingStr
                if x + ingStrLen > 200:
                    igList = igList + "\n"
                    x = 0
                x += ingStrLen
            print("\n"+igList+"\n")
        else:
            break

    dropRates = []
    ingreList = ingredients.split(",")
    for i in range(len(ingreList)):
        ingreList[i] = helpers.IDFormat(ingreList[i])
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
    prereqs = []
    for i in range(3):
        Type = input("Input prerequisite "+str(i+1)+" options:\n (Gold) (Potion) (None): ")
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

        elif Type.upper() == "POTION" or Type.upper() == "P" or Type.upper() == "POT":
            potName = input("Potion Name: ")
            potName = helpers.NameFormat(potName)
            potImg = input("Potion Color/directory: ")
            #if not checkColor()
            if not os.path.exists(potImg):
                print("Path does not exist, setting random color")
                potImg = "sprites/potions/" + str(helpers.randomPotionColor())
            prereqs.append({"Potion":{"Name":potName, "ImageLocation":potImg}})
        else:
            prereqs.append("None")
    newLoc = helpers.Location(ID, name, img, color, ingreList, dropRates, prereqs[0], prereqs[1], prereqs[2])
    Locations.append(newLoc)
    ans = input("Sucessfully added to list, continue? (y/n): ")
    if ans == 'n':
        Running = False
helpers.saveLocations(Locations)

