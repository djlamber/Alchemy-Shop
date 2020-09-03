import helpers
import sys
import os.path
from constants import *
from DevTools import DevHelpers

#This is a tool that uses the terminal to add new tool



def createTool():
    Tools = helpers.InitTools()
    Running = True
    print("=====Create Tool=====")
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
        for T in Tools:
            if T.getID() == ID:
                print("ID already taken")
                setContinue = True
                break
        if setContinue:
            continue

        # Select Name
        name = input("Input Name: ")
        name = DevHelpers.NameFormat(name)

        # Select Image Dir
        img = input("Input Image directory: ")
        if not os.path.exists(img):
            print("Path does not exist, setting default")
            img = "sprites/UnknownWhite.png"

        # Select Use
        while True:
            use = input("Input usage for tool (Extraction | Combination): ")
            if use.upper() == "EXTRACTION" or use.upper() == "Combination":
                use = DevHelpers.NameFormat(use)
                break
            if use.upper() == "E":
                use = "Extraction"
                break
            if use.upper() == "C":
                use = "Combination"
                break
            print("Invalid Input\n")

        # Select Inslots
        while True:
            inSlots = input("Input number of input slots (1-5): ")
            if inSlots == "":
                inSlots = 1
                break
            try:
                inSlots = int(inSlots)
            except ValueError:
                print("That is not a integer")
            if type(inSlots) == int:
                if inSlots < 0:
                    inSlots = 1
                if inSlots > 5:
                    inSlots = 5
                break

        # Select OutSlots
        while True:
            outSlots = input("Input number of output slots (1-5): ")
            if outSlots == "":
                outSlots = 1
                break
            try:
                outSlots = int(outSlots)
            except ValueError:
                print("That is not a integer")
            if type(outSlots) == int:
                if outSlots < 0:
                    outSlots = 1
                if outSlots > 5:
                    outSlots = 5
                break

        # Select Unlocked status
        while True:
            unlocked = input("Input unlocked status: ")
            if unlocked.upper() == "TRUE" or unlocked.upper() == "T":
                unlocked = True
                break
            if unlocked.upper() == "FALSE" or unlocked.upper() == "F":
                unlocked = False
                break
            print("Invalid input\n")


        # Create Tool
        newTool = helpers.Tool(ID, name, img, use, inSlots, outSlots, unlocked)
        Tools.append(newTool)
        ans = input("Sucessfully added to list, continue? (y/n): ")
        if ans.upper() != 'Y':
            Running = False
    helpers.saveTools(Tools)