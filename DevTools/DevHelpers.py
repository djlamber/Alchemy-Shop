import helpers
from constants import *
from helpers import *
from colorama import Fore, Style

# helper functions for dev tools

def IDFormat(ID):
    if ID == "":
        return ID
    ID = ID.lower()
    ID = ID.replace(" ", "_")
    ID = ID.replace(",", "_")
    ID = ID.replace("-", "_")
    lastID = ""
    while lastID != ID:
        lastID = ID
        ID = ID.replace("__", "_")
    if ID[-1] == "_":
        ID = ID[:-1]
    if ID == "":
        return ID
    if ID[0] == "_":
        ID = ID[1:]
    indexes = [i for i, ltr in enumerate(ID) if ltr == "_"]
    strIndex = 1
    formattedID = ID[0].upper()
    for i in indexes:
        formattedID = formattedID + ID[strIndex:i+1] + ID[i+1].upper()
        strIndex = i+2
    formattedID = formattedID + ID[strIndex:]
    return formattedID

def NameFormat(Name):
    if Name == "":
        return Name
    Name = Name.lower()
    Name = Name.replace("_", " ")
    Name = Name.replace(",", " ")
    lastName = ""
    while lastName != Name:
        lastName = Name
        Name = Name.replace("  ", " ")
    if Name[-1] == " ":
        Name = Name[:-1]
    if Name == "":
        return Name
    if Name[0] == " ":
        Name = Name[1:]
    indexes = [i for i, ltr in enumerate(Name) if ltr == " "]
    strIndex = 1
    formattedName = Name[0].upper()
    for i in indexes:
        formattedName = formattedName + Name[strIndex:i+1] + Name[i+1].upper()
        strIndex = i+2
    formattedName = formattedName + Name[strIndex:]
    return formattedName

def checkColor(color):
    if color == "":
        return None
    if color.upper() == "WHITE":
        return WHITE
    if color.upper() == "SILVER":
        return SILVER
    if color.upper() == "GOLD":
        return GOLD
    if color.upper() == "GRAY":
        return GRAY
    if color.upper() == "BLACK":
        return BLACK
    if color.upper() == "BROWN":
        return BROWN
    if color.upper() == "RED":
        return RED
    if color.upper() == "MAROON":
        return MAROON
    if color.upper() == "YELLOW":
        return YELLOW
    if color.upper() == "OLIVE":
        return OLIVE
    if color.upper() == "LIME":
        return LIME
    if color.upper() == "GREEN":
        return GREEN
    if color.upper() == "AQUA":
        return AQUA
    if color.upper() == "TEAL":
        return TEAL
    if color.upper() == "BLUE":
        return BLUE
    if color.upper() == "NAVY":
        return NAVY
    if color.upper() == "FUCHSIA":
        return FUCHSIA
    if color.upper() == "PURPLE":
        return PURPLE
    RGB = color.split(",")
    for i in range(len(RGB)):
        RGB[i] = int(RGB[i])
    print(RGB)
    if len(RGB) == 3:
        return RGB
    return None # color is not valid

def printIngredients(Ingredients):
    igList = ""
    x = 0
    for i in Ingredients:
        ingStr = "[" + str(i.getID()) + "], "
        ingStrLen = len(ingStr)

        #check to see if ingredient is fully valid
        if i.getImgLoc() == "sprites/ingredients/UnknownIngredientWhite.png" or i.getImgLoc() == "sprites/UnknownWhite.png" or i.getColor() == [255,255,255] or i.getValue() < 0:
            ingStr = Fore.RED + ingStr + Fore.RESET
        else:
            red = True
            for eff in helpers.InitEffects():
                if i.getEffect1() == eff.getID() or i.getEffect2() == eff.getID() or i.getEffect3() == eff.getID() :
                    red = False
                    break
            if red:
                ingStr = Fore.RED + ingStr + Fore.RESET
        # stop checking

        igList = igList + ingStr
        if x + ingStrLen > 120:
            igList = igList + "\n"
            x = 0
        x += ingStrLen
    print("\n" + igList + "\n")


def printEffects(Effects):
    effList = ""
    x = 0
    for i in Effects:
        effStr = "[" + str(i.getID()) + "], "
        effStrLen = len(effStr)
        effList = effList + effStr
        if x + effStrLen > 200:
            effList = effList + "\n"
            x = 0
        x += effStrLen
    print("\n" + effList + "\n")

def printLocations(Locations):
    locList = ""
    x = 0
    for i in Locations:
        locStr = "[" + str(i.getID()) + "], "
        locStrLen = len(locStr)
        locList = locList + locStr
        if x + locStrLen > 200:
            locList = locList + "\n"
            x = 0
        x += locStrLen
    print("\n" + locList + "\n")

def printTools(Tools, Use = None):
    toolList = ""
    x = 0
    for i in Tools:
        if Use != None:
            if i.getUse() != Use:
                continue
        toolStr = "[" + str(i.getID()) + "], "
        toolStrLen = len(toolStr)
        toolList = toolList + toolStr
        if x + toolStrLen > 200:
            toolList = toolList + "\n"
            x = 0
        x += toolStrLen
    print("\n" + toolList + "\n")


def printRecipes(Recipes):
    recipeList = ""
    x = 0
    for i in Recipes:
        recipeStr = "[" + str(i.getID()) + "], "
        recipeStrLen = len(recipeStr)
        recipeList = recipeList + recipeStr
        if x + recipeStrLen > 200:
            recipeList = recipeList + "\n"
            x = 0
        x += recipeStrLen
    print("\n" + recipeList + "\n")
