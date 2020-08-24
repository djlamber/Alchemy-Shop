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
    if color.upper() == "GRAY":
        return GRAY
    if color.upper() == "BLACK":
        return BLACK
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
        if i.getImgLoc() == "sprites/ingredients/UnknownIngredientWhite.png" or i.getImgLoc() == "sprites/UnknownWhite.png":
            ingStr = Fore.RED + ingStr + Fore.RESET
        igList = igList + ingStr
        if x + ingStrLen > 120:
            igList = igList + "\n"
            x = 0
        x += ingStrLen
    print("\n" + igList + "\n")

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