import json

from DevTools import DevHelpers
from constants import *
from pygameFunctions import *
from random import *
from time import *
import config

#Stupid functions made to increment through file and function

def IncreaseVal(num):
    num[0] +=1
    return num
def DecreaseVal(num):
    num[0] -=1
    return num

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            config.MUP = True

class Player:
    def __init__(self, gold):
        self.Gold = gold

    def getGold(self):
        return self.Gold
    def setGold(self, newVal):
        self.Gold = newVal
    def addGold(self, addVal):
        self.Gold = self.Gold + addVal
    def subGold(self, subVal):
        self.Gold = self.Gold - subVal

def InitPlayer():
    player = []
    with open("playerData.json") as f:
        PlayerJson = json.load(f)  # load data as dict
        print(PlayerJson)
    for data in PlayerJson.items():
        player = Player(data[1])
    return player

def savePlayer(Player):
    prepareData = {}
    data = {"Gold": Player.getGold()}
    with open("playerData.json", "w") as f: #  write to json
        json.dump(data, f, indent=4)

class Ingredient:
    def __init__(self, ID, name, img, category, color, value, amount, effect1, effect2, effect3):
        self.ID = ID
        self.name = name
        self.imgLoc = img
        self.category = category
        self.color = color
        self.value = value
        self.amount = amount
        self.effect_1 = effect1
        self.effect_2 = effect2
        self.effect_3 = effect3

    def getID(self):
        return self.ID
    def getName(self):
        return self.name
    def getImgLoc(self):
        return self.imgLoc
    def getCategory(self):
        return self.category
    def getColor(self):
        return self.color
    def getValue(self):
        return self.value
    def getAmount(self):
        return self.amount
    def getEffect1(self):
        return self.effect_1
    def getEffect2(self):
        return self.effect_2
    def getEffect3(self):
        return self.effect_3

    def setAmount(self, newAmount):
        self.amount = newAmount
    def addAmount(self, addVal):
        self.amount = self.amount + addVal
    def subAmount(self, subVal):
        self.amount = self.amount - subVal

def InitIngredients():
    Ingredients = []
    with open("ingredientInventory.json") as f:
        IngredientJson = json.load(f)  # load data as dict
    for ingre in IngredientJson.items():
        newIngre = Ingredient(ingre[0],
                              ingre[1].get("Name"),
                              ingre[1].get("ImageLocation"),
                              ingre[1].get("Category"),
                              ingre[1].get("Color"),
                              ingre[1].get("Value"),
                              ingre[1].get("Amount"),
                              DevHelpers.NameFormat(ingre[1].get("Effect1")),
                              DevHelpers.NameFormat(ingre[1].get("Effect2")),
                              DevHelpers.NameFormat(ingre[1].get("Effect3")))

        Ingredients.append(newIngre) #add data to list
    return Ingredients

def saveIngredients(Ingredients):
    prepareData = {}
    for ingre in Ingredients:
        newData = {"Name": ingre.getName(),  # create list
                   "ImageLocation": ingre.getImgLoc(),
                   "Category": sorted(ingre.getCategory()),
                   "Color": ingre.getColor(),
                   "Value": ingre.getValue(),
                   "Amount": ingre.getAmount(),
                   "Effect1": ingre.getEffect1(),
                   "Effect2": ingre.getEffect2(),
                   "Effect3": ingre.getEffect3()
                   }
        prepareData[ingre.getID()] = newData  # Add list data to dict
    with open("ingredientInventory.json", "w") as f: #  write to json
        json.dump(prepareData, f, indent=4)

class Potion:
    def __init__(self, ID, name, img, ing1, ing2, ing3, value):
        self.ID = ID
        self.name = name
        self.imgLoc = img
        self.ingredient_1_ID = ing1
        self.ingredient_2_ID = ing2
        self.ingredient_3_ID = ing3
        self.value = value

    def getID(self):
        return self.ID
    def getName(self):
        return self.name
    def getImgLoc(self):
        return self.imgLoc
    def getIngredient_1_ID(self):
        return self.ingredient_1_ID
    def getIngredient_2_ID(self):
        return self.ingredient_2_ID
    def getIngredient_3_ID(self):
        return self.ingredient_3_ID
    def getValue(self):
        return self.value

    def setAmount(self, newAmount):
        self.amount = newAmount

def InitPotionList():
    PotionList = []
    with open("potionInventory.json") as f:
        PotionJson = json.load(f)  # load data as dict
    for pot in PotionJson.items():
        newPotion = Potion(pot[0],
                            pot[1].get("Name"),
                            pot[1].get("ImageLocation"),
                            DevHelpers.NameFormat(pot[1].get("Ingredient_1_ID")),
                            DevHelpers.NameFormat(pot[1].get("Ingredient_2_ID")),
                            DevHelpers.NameFormat(pot[1].get("Ingredient_3_ID")),
                            pot[1].get("Value"))
        PotionList.append(newPotion)
    return PotionList

def savePotions(PotionList):
    prepareData = {}
    for pot in PotionList:
        newData = {"Name": pot.getName(),  # create list
                   "ImageLocation": pot.getImgLoc(),
                   "Ingredient_1_ID": pot.getIngredient_1_ID(),
                   "Ingredient_2_ID": pot.getIngredient_2_ID(),
                   "Ingredient_3_ID": pot.getIngredient_3_ID(),
                   "Value" : pot.getValue()}
        prepareData[pot.getID()] = newData  # Add list data to dict
    with open("potionInventory.json", "w") as f: #  write to json
        json.dump(prepareData, f, indent=4)


#Location Objects
class Location:
    def __init__(self,ID, name, imgLoc, color, ingredients, dropRates, pre1, pre2, pre3):
        self.ID = ID
        self.Name = name
        self.imgLoc = imgLoc
        self.color = color
        self.ingredients = ingredients #IngredientID
        self.dropRates = dropRates
        self.Prerequisite1 = pre1
        self.Prerequisite2 = pre2
        self.Prerequisite3 = pre3

    def getID(self):
        return self.ID
    def getName(self):
        return self.Name
    def getImgLoc(self):
        return self.imgLoc
    def getColor(self):
        return self.color
    def getIngredients(self):
        return self.ingredients
    def getDropRates(self):
        return self.dropRates
    def getPrereq1(self):
        return self.Prerequisite1
    def getPrereq2(self):
        return self.Prerequisite2
    def getPrereq3(self):
        return self.Prerequisite3


def InitLocations():
    Locations = []
    with open("locationData.json") as f:
        locJson = json.load(f)  # load data as dict
    for data in locJson.items():
        location = Location(data[0],
                            data[1].get("Name"),
                            data[1].get("ImageLocation"),
                            data[1].get("Color"),
                            data[1].get("Ingredients"),
                            data[1].get("DropRates"),
                            data[1].get("Prereq1"),
                            data[1].get("Prereq2"),
                            data[1].get("Prereq3"),
                            )
        Locations.append(location)
    return Locations

def saveLocations(Locations):
    prepareData = {}
    for loc in Locations:
        newData = {"Name": loc.getName(),  # create list
                   "ImageLocation": loc.getImgLoc(),
                   "Color": loc.getColor(),
                   "Ingredients": loc.getIngredients(),
                   "DropRates": loc.getDropRates(),
                   "Prereq1": loc.getPrereq1(),
                   "Prereq2": loc.getPrereq2(),
                   "Prereq3": loc.getPrereq3()
                    }
        prepareData[loc.getID()] = newData  # Add list data to dict
    with open("locationData.json", "w") as f:  # write to json
        json.dump(prepareData, f, indent=4)

def randomPotionColor():
    listOfSprites = ["BlackPotion.png",
                    "BluePotion.png",
                    "BrownPotion.png",
                    "CyanPotion.png",
                    "GreenPotion.png",
                    "GreyPotion.png",
                    "MagentaPotion.png",
                    "NavyPotion.png",
                    "OlivePotion.png",
                    "OrangePotion.png",
                    "PinkPotion.png",
                    "PurplePotion.png",
                    "RedPotion.png",
                    "WhitePotion.png",
                    "YellowPotion.png"]
    return listOfSprites[randrange(0,len(listOfSprites))]






