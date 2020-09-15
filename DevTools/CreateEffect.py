import helpers
import sys
import os.path
from constants import *
from DevTools import DevHelpers

#This is a tool that uses the terminal to add new ingredients



def createEffect():
    Effects = helpers.InitEffects()
    Running = True
    print("=====Create Effect=====")
    while Running:
        print("Type \'list\' to list out effects, q to quit")

        # Select ID
        ID = input("Input ID: ")
        ID = DevHelpers.IDFormat(ID)
        option = ID.upper()
        if option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END" or option == "":
            Running = False
            break
        if option == "LIST" or option == "L":
            setContinue = True
            DevHelpers.printEffects(Effects)
            continue
        setContinue = False
        for I in Effects:
            if I.getID() == ID:
                print("ID already taken")
                setContinue = True
                break
        if setContinue:
            continue

        #Select Ingredient Name
        ingName = input("Input Name Stylized for Ingredient Effect: ")
        if ingName == "":
            ingName = ID
        else:
            ingName = DevHelpers.NameFormat(ingName)

        # Select Potion Name
        potName = input("Input Name Stylized for Potion Effect: ")
        if potName == "":
            potName = ID
        else:
            potName = DevHelpers.NameFormat(potName)

        # Select Upgrade Name
        upName = input("Input Name Stylized for Upgrade Effect: ")
        if upName == "":
            upName = ID
        else:
            upName = DevHelpers.NameFormat(upName)

        #Create Ingredient
        newEffect = helpers.Effect(ID, ingName, potName, upName)
        Effects.append(newEffect)
        Effects.sort(key=lambda k: k.getID())
        ans = input("Sucessfully added to list, continue? (y/n): ")
        if ans.upper() != 'Y':
            Running = False
    helpers.saveEffects(Effects)