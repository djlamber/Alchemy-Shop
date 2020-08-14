import helpers
import sys
import os.path
from constants import *
from DevTools import DevHelpers

#This is a tool that uses the terminal to add new ingredients



def createIngredient():
    Ingredients = helpers.InitIngredients()
    Running = True
    print("=====Create Ingredient=====")
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
        for I in Ingredients:
            if I.getID() == ID:
                print("ID already taken")
                setContinue = True
                break
        if setContinue:
            continue

        #Select Name
        name = input("Input Name: ")
        name = DevHelpers.NameFormat(name)

        #Select Image Dir
        img = input("Input Image directory: ")
        if not os.path.exists(img):
            print("Path does not exist, setting default")
            img = "sprites/UnknownWhite.png"

        #Select Categories
        category = input("Input Categories, separated by a comma: ")
        categoryList = category.split(",")
        for i in range(len(categoryList)):
            if categoryList[i] == " ":
                continue
            categoryList[i] = DevHelpers.NameFormat(categoryList[i])

        #Select Color
        color = input("Input Color: ")
        if DevHelpers.checkColor(color.upper()) == None:
            print("Color not recognized, setting to default")
            color = WHITE

        #Select Value
        while True:
            value = input("Input Value: ")
            if value == "":
                value = 10
                break
            try:
                value = int(value)
            except ValueError:
                print("That is not a integer")
            if type(value) == int:
                if value < 0:
                    value = 0
                break

        #Select Amount
        while True:
            amount = input("Input Amount: ")
            if amount == "":
                amount = 0
                break
            try:
                amount = int(amount)
            except ValueError:
                print("That is not a integer")
            if type(amount) == int:
                if amount < 0:
                    amount = 0
                break

        #Select Effects
        effects = []
        for i in range(3):
            effect = input("Input Effect "+str(i) + ": ")
            effect = DevHelpers.NameFormat(effect)
            if effect == "" or effect == " " or effect == "N":
                effect = "None"
            effects.append(effect)

        #Create Ingredient
        newIngre = helpers.Ingredient(ID, name, img, categoryList, color, int(value), int(amount), effects[0], effects[1], effects[2])
        Ingredients.append(newIngre)
        ans = input("Sucessfully added to list, continue? (y/n): ")
        if ans.upper() != 'Y':
            Running = False
    helpers.saveIngredients(Ingredients)