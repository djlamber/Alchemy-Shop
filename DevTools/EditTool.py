import helpers
import config
import sys
import os.path
from DevTools import DevHelpers



def editToolName(tool, name):
    print("Current name for ["+str(tool.getID())+"] : " + str(name))
    newName = input("Input new name or null to go back: ")
    if newName == "":
        return name
    else:
        return DevHelpers.NameFormat(newName)

def editToolImgLoc(tool, img):
    while True:
        print("Current Image Location for [" + str(tool.getID()) + "] : " + str(img))
        newImg = input("Input new Image location or null to go back: ")
        if newImg == "":
            return img
        else:
            if not os.path.exists(newImg):
                print("Path does not exist")
            else:
                return newImg

def editToolUse(tool, use):
    otherUse = None
    if use == "Combination":
        otherUse = "Extraction"
    else:
        otherUse = "Combination"
    print("WARNING! Changing the tool use can effect how ingredient recipes are handled")
    option = input("Would you like to change the tool use from "+ use +" to "+ otherUse +"? (Y|N)")
    if option == "YES" or option == "Y":
        use = otherUse
        return otherUse
    else:
        return use


def editToolInSlots(tool, inSlots):
    return inSlots




def editToolOutSlots(tool, outSlots):
    return outSlots



def editToolUnlocked(tool, unlocked):
    otherUnlocked = None
    if unlocked == True:
        otherUnlocked = False
    else:
        otherUnlocked = True
    option = input("Would you like to change the unlocked status from " + str(unlocked) + " to " + str(otherUnlocked) + "? (Y|N)").upper()
    if option == "YES" or option == "Y":
        unlocked = otherUnlocked
        return otherUnlocked
    else:
        return unlocked



def editTool():
    Tools = helpers.InitTools()
    Ingredients = helpers.InitIngredients()
    Ingredients.sort(key=lambda k: k.getName())

    Running = True
    tool = None
    while Running:
        print("=====Edit Tools=====")
        print("Type \'list\' to see all tools")
        print("Type q to quit")
        while (Running):
            print("Select Tool ID to Edit:")
            entry = input()
            option = entry.upper()
            if option == "" or option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END":
                Running = False
                break
            if option.upper() == "LIST":
                DevHelpers.printTools(Tools)
            else:
                setToBreak = False
                toolID = DevHelpers.IDFormat(option)

                for i in Tools:
                    if i.getID() == toolID:
                        tool = i
                        setToBreak = True
                        break
                if setToBreak:
                    break
                print("Invalid Tool ID [" + toolID + "]\n")
                print("Type \'list\' to see all tools")
        if not Running:
            break

        # get vars ready
        name = tool.getName()
        img = tool.getImgLoc()
        use = tool.getUse()
        inSlots = tool.getInSlots()
        outSlots = tool.getOutSlots()
        unlocked = tool.getUnlocked()

        editingIngredient = True
        while (editingIngredient):
            print("\nSelect Attribute to Edit for [" + str(tool.getID()) + "]")
            print("Type s to save and continue, q save and quit")
            print("Name | ImageLocation | Use | InSlots | OutSlots | Unlocked")
            attrib = input().upper()
            if attrib == "" or attrib == "Q" or attrib == "EXIT" or attrib == "QUIT" or attrib == "STOP" or attrib == "END":
                newTool = helpers.Tool(tool.getID(), name, img, use, inSlots, outSlots, unlocked)
                Tools.append(newTool)
                helpers.saveTools(Tools)
                Tools = helpers.InitTools()
                print("Successfully saved")
                editingIngredient = False
                break
            if attrib == "NAME" or attrib == "N":
                name = editToolName(tool, name)
            if attrib == "IMAGELOCATION" or attrib == "IMAGE" or attrib == "IM" or attrib == "IMG":
                img = editToolImgLoc(tool, img)
            if attrib == "USE":
                use = editToolUse(tool, use)
            if attrib == "INSLOTS" or attrib == "IN" or attrib == "I":
                inSlots = editToolInSlots(tool, inSlots)
            if attrib == "OUTSLOTS" or attrib == "OUT" or attrib == "O":
                outSlots = editToolOutSlots(tool, inSlots)
            if attrib == "UNLOCKED" or attrib == "U":
                unlocked = editToolUnlocked(tool, unlocked)

                newTool = helpers.Tool(tool.getID(), name, img, use, inSlots, outSlots, unlocked)
                Tools.append(newTool)
                helpers.saveTools(Tools)
                Tools = helpers.InitTools()
                print("Successfully saved")