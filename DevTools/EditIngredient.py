from colorama import Fore

import helpers
import sys
import os.path
from DevTools import DevHelpers
from DevTools.CreateEffect import createEffect


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
    print("Type \'list\' to list out effects, null to go back")
    while True:
        print("Current effects for [" + str(ingre.getID()) + "] :")
        strE1 = Fore.RED + str(effects[0]) + Fore.RESET
        strE2 = Fore.RED + str(effects[1]) + Fore.RESET
        strE3 = Fore.RED + str(effects[2]) + Fore.RESET
        for eff in helpers.InitEffects():
            if eff.getID() == effects[0]:
                strE1 = str(effects[0])
            if eff.getID() == effects[1]:
                strE2 = str(effects[1])
            if eff.getID() == effects[2]:
                strE3 = str(effects[2])
        print("Effect 1: " + strE1 + " | Effect 2: " + strE2 + " | Effect 3: " + strE3 )
        selection = input("Select Effect to edit: ").upper()
        if selection == "":
            return effects
        if selection == "LIST":
            DevHelpers.printEffects(helpers.InitEffects())
        else:
            if selection == "1" or selection == "EFFECT1" or selection == "EFFECT 1":
                effects[0] = changeEffect(ingre, effects[0])
            if selection == "2" or selection == "EFFECT2" or selection == "EFFECT 2":
                effects[1] = changeEffect(ingre, effects[1])
            if selection == "3" or selection == "EFFECT3" or selection == "EFFECT 3":
                effects[2] = changeEffect(ingre, effects[2])
        print("Type \'list\' to list out effects, null to go back")

def changeEffect(ingre, effect):
    while True:
        print("\nEnter new effect for [" + str(ingre.getID()) + "]")
        print("Type \'list\' to print out list of effects, type null to go back")
        print("Current effect: "+ str(effect))
        newEffect = input()
        if newEffect.upper() == "LIST" or newEffect.upper() == "L":
            DevHelpers.printEffects(helpers.InitEffects())
            continue
        if newEffect == "":
            return effect
        newEffect = DevHelpers.IDFormat(newEffect)
        for i in helpers.InitEffects():
            if i.getID() == newEffect:
                return newEffect
        opt = input("This effect is not an existing effect, would you like to create a new one? (y|n)").upper()
        if opt == "Y" or opt == "YES":
            createEffect()
            continue
        return newEffect





def editIngredient():
    Ingredients = helpers.InitIngredients()
    Ingredients.sort(key=lambda k: k.getName())
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
            if attrib == "VALUE" or attrib == "VAL" or attrib == "V":
                value = editIngreValue(ingre, value)
            if attrib == "EFFECT" or attrib == "E":
                effects = editIngreEffect(ingre, effects)
            if attrib == "SAVE" or attrib == "S":
                newIngre = helpers.Ingredient(ingre.getID(), name, img, categoryList, color, value, ingre.getAmount(), effects[0], effects[1], effects[2])
                Ingredients.append(newIngre)
                helpers.saveIngredients(Ingredients)
                Ingredients = helpers.InitIngredients()
                print("Successfully saved")