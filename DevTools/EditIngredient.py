import helpers
import sys
import os.path
from DevTools import DevHelpers

def editIngreName(ingre, name):
    print("Current name for ["+str(ingre.getID())+"] : " + str(name))
    newName = input("Input new name or null to go back: ")
    if newName == "":
        return name
    else:
        return DevHelpers.NameFormat(newName)

def editIngreImgLoc(ingre, img):
    while True:
        print("Current Image Location for [" + str(ingre.getID()) + "] : " + str(img))
        newImg = input("Input new Image location or null to go back: ")
        if newImg == "":
            return img
        else:
            if not os.path.exists(newImg):
                print("Path does not exist")
            else:
                return newImg

def editIngreCategory(ingre, categoryList):
    while(True):
        print("\nCurrent categories for [" + str(ingre.getID()) + "] : \n"+ str(categoryList))
        print("Type null to go back, select an option:")
        selection = input("Add | Remove\n").upper()
        if selection == "" or selection == "Q" or selection == "EXIT" or selection == "QUIT" or selection == "STOP" or selection == "END":
            return categoryList
        if selection == "ADD" or selection == "A":
            cat = DevHelpers.IDFormat(input("Type in new category:\n"))
            categoryList.append(cat)
        if selection == "REMOVE" or selection == "R" or selection == "DELETE" or selection == "D":
            cat = DevHelpers.IDFormat(input("Type in category to delete:\n"))
            try:
                categoryList.remove(cat)
            except:
                print("Category does not exist")

def editIngreColor(ingre, color):
    while True:
        print("Current Color for [" + str(ingre.getID()) + "] : " + str(color))
        newColor = input("Input new Color or null to go back: ")
        if newColor == "":
            return color
        else:
            colorCheck = DevHelpers.checkColor(newColor)
            if colorCheck == None:
                print("Color is not valid")
            else:
                return colorCheck

def editIngreValue(ingre, value):
    while True:
        print("Current value for [" + str(ingre.getID()) + "] : " + str(value))
        newValue = input("Input new Value or null to go back: ")
        if newValue == "":
            return value
        else:
            return int(newValue)

def editIngreEffect(ingre, effects):
    while True:
        print("Current effects for [" + str(ingre.getID()) + "] :")
        print("Effect 1: " + str(effects[0]) + " | Effect 2: " + str(effects[1]) + " | Effect 3: " + str(effects[2]) )
        selection = input("Select Effect to edit or null to go back: ").upper()
        if selection == "":
            return effects
        else:
            if selection == "1" or selection == "EFFECT1" or selection == "EFFECT 1":
                effects[0] = changeEffect(ingre, effects[0])
            if selection == "2" or selection == "EFFECT2" or selection == "EFFECT 2":
                effects[1] = changeEffect(ingre, effects[1])
            if selection == "3" or selection == "EFFECT3" or selection == "EFFECT 3":
                effects[2] = changeEffect(ingre, effects[2])

def changeEffect(ingre, effect):
    print("\nEnter new effect for [" + str(ingre.getID()) + "]")
    print("Type null to go back")
    print("Current effect: "+ str(effect))
    newEffect = input()
    if newEffect == "":
        return effect
    return newEffect





def editIngredient():
    Ingredients = helpers.InitIngredients()
    Running = True
    ingre = None
    while Running:
        print("=====Edit Ingredient=====")
        while(Running):
            print("Type \'list\' to see all ingredients")
            print("Type q to quit")
            print("Select Ingredient ID to Edit:")
            entry = input()
            option = entry.upper()
            if option == "" or option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END":
                Running = False
                break
            if option.upper() == "LIST":
                DevHelpers.printIngredients(Ingredients)
            else:
                setToBreak = False
                ingreID = DevHelpers.IDFormat(option)

                for i in Ingredients:
                    if i.getID() == ingreID:
                        ingre = i
                        setToBreak = True
                        break
                if setToBreak:
                    break
        if not Running:
            break

        #get vars ready
        name = ingre.getName()
        img = ingre.getImgLoc()
        categoryList = ingre.getCategory()
        color = ingre.getColor()
        value = ingre.getValue()
        effects = [ingre.getEffect1(), ingre.getEffect2(), ingre.getEffect3()]

        editingIngredient = True
        while(editingIngredient):
            print("\nSelect Attribute to Edit for ["+str(ingre.getID())+"]")
            print("Type s to save and continue, q save and quit")
            print("Name | ImageLocation | Category | Color | Value | Effect")
            attrib = input().upper()
            if attrib == "" or attrib == "Q" or attrib == "EXIT" or attrib == "QUIT" or attrib == "STOP" or attrib == "END":
                newIngre = helpers.Ingredient(ingre.getID(), name, img, categoryList, color, value, ingre.getAmount(), effects[0], effects[1], effects[2])
                Ingredients.append(newIngre)
                helpers.saveIngredients(Ingredients)
                Ingredients = helpers.InitIngredients()
                print("Successfully saved")
                editingIngredient = False
                break
            if attrib == "NAME" or attrib == "N":
                name = editIngreName(ingre, name)
            if attrib == "IMAGELOCATION" or attrib == "IMAGE" or attrib == "I" or attrib == "IMG":
                img = editIngreImgLoc(ingre, img)
            if attrib == "CATEGORY" or attrib == "CAT" or attrib == "CA":
                categoryList = editIngreCategory(ingre, categoryList)
            if attrib == "COLOR" or attrib == "CO":
                color = editIngreColor(ingre, color)
            if attrib == "VALUE" or attrib == "VAL":
                value = editIngreValue(ingre, value)
            if attrib == "EFFECT" or attrib == "E":
                effects = editIngreEffect(ingre, effects)
            if attrib == "SAVE" or attrib == "S":
                newIngre = helpers.Ingredient(ingre.getID(), name, img, categoryList, color, value, ingre.getAmount(), effects[0], effects[1], effects[2])
                Ingredients.append(newIngre)
                helpers.saveIngredients(Ingredients)
                Ingredients = helpers.InitIngredients()
                print("Successfully saved")