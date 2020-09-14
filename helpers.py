import json
import math

from DevTools import DevHelpers
from constants import *
from pygameFunctions import *
from random import *
from time import *
import config
from pygame.locals import *

#Stupid functions made to increment through file and function

def IncreaseVal(num):
    num[0] +=1
    return num
def DecreaseVal(num):
    num[0] -=1
    return num

def randCol():
    col = [0,0,0]
    col[0] = int(randrange(0,255))
    col[1] = int(randrange(0,255))
    col[2] = int(randrange(0,255))
    print(col)
    return col

def addColor(col1, col2):
    col = [0,0,0]
    col[0] = col1[0] + col2[0]
    col[1] = col1[1] + col2[1]
    col[2] = col1[2] + col2[2]
    return col

def subColor(col1, col2):
    col = [0,0,0]
    col[0] = col1[0] - col2[0]
    col[1] = col1[1] - col2[1]
    col[2] = col1[2] - col2[2]
    return col

def multColor(col, value):
    col[0] *= value
    col[1] *= value
    col[2] *= value
    return col

def divColor(col, value):
    col[0] /= value
    col[1] /= value
    col[2] /= value
    return col

def squareCol(col, degree):
    sqCol = [0,0,0]
    sqCol[0] = col[0]**degree
    sqCol[1] = col[1]**degree
    sqCol[2] = col[2]**degree
    return sqCol


def getCaulColor():
    col = [0,0,0]
    for i in config.selectedIngredients:
        if i != None:
            col = addColor(col, squareCol(i.getColor(),2))
    col[0] = int(math.sqrt(col[0] / config.numSelectedIngredients))
    col[1] = int(math.sqrt(col[1] / config.numSelectedIngredients))
    col[2] = int(math.sqrt(col[2] / config.numSelectedIngredients))
    return col



#####################################

class Player:
    def __init__(self, gold, shopName, buyMarkup, sellMarkdown):
        self.Gold = gold
        self.ShopName = shopName
        self.BuyMarkup = buyMarkup
        self.SellMarkdown = sellMarkdown

    def getGold(self):
        return self.Gold
    def setGold(self, newVal):
        self.Gold = newVal
    def addGold(self, addVal):
        self.Gold = self.Gold + addVal
    def subGold(self, subVal):
        self.Gold = self.Gold - subVal

    def getShopName(self):
        return self.ShopName
    def setShopName(self,name):
        self.ShopName = name

    def getBuyMarkup(self):
        return self.BuyMarkup
    def setBuyMarkup(self, value):
        self.BuyMarkup = value

    def getSellMarkdown(self):
        return self.SellMarkdown
    def setSellMakrdown(self, value):
        self.SellMarkdown = value

def InitPlayer():
    player = []
    with open("Data/playerData.json") as f:
        PlayerJson = json.load(f)  # load data as dict
    print(PlayerJson)
    player = Player(PlayerJson.get("Gold"),
                    PlayerJson.get("Shop Name"),
                    PlayerJson.get("Buy Markup"),
                    PlayerJson.get("Sell Markdown")
                    )
    return player

def savePlayer(Player):
    prepareData = {}
    data = {"Gold": Player.getGold(),
            "Shop Name": Player.getShopName(),
            "Buy Markup": Player.getBuyMarkup(),
            "Sell Markdown": Player.getSellMarkdown()
            }
    with open("Data/playerData.json", "w") as f: #  write to json
        json.dump(data, f, indent=4)


################################

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
    with open("Data/ingredientInventory.json") as f:
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
    with open("Data/ingredientInventory.json", "w") as f: #  write to json
        json.dump(prepareData, f, indent=4)


############################################# Effects
class Effect:
    def __init__(self, ID, ingName, potName, upName):
        self.ID = ID
        self.IngredientName = ingName
        self.PotionName = potName
        self.UpgradeName = upName

    def getID(self):
        return self.ID
    def getIngName(self):
        return self.IngredientName
    def setIngName(self, newName):
        self.IngredientName = newName
    def getPotName(self):
        return self.PotionName
    def setPotName(self, newName):
        self.PotionName = newName
    def getUpName(self):
        return self.UpgradeName
    def setUpName(self, newName):
        self.UpgradeName = newName

def InitEffects():
    Effects = []
    with open("Data/effectsInfo.json") as f:
        locJson = json.load(f)  # load data as dict
    for data in locJson.items():
        jdataEntry = Effect(data[0],
                            data[1].get("Ingredient Name"),
                            data[1].get("Potion Name"),
                            data[1].get("Upgrade Name")
                            )
        Effects.append(jdataEntry)
    return Effects

def saveEffects(Effects):
    prepareData = {}
    for dat in Effects:
        newData = {"Ingredient Name": dat.getIngName(),
                   "Potion Name": dat.getPotName(),
                   "Upgrade Name": dat.getUpName()
                    }
        prepareData[dat.getID()] = newData  # Add list data to dict
    with open("Data/effectsInfo.json", "w") as f:  # write to json
        json.dump(prepareData, f, indent=4)

#################################

class Potion:
    def __init__(self, ID, name, img, ing1, ing2, ing3, effect, color, value):
        self.ID = ID
        self.name = name
        self.imgLoc = img
        self.ingredient_1_ID = ing1
        self.ingredient_2_ID = ing2
        self.ingredient_3_ID = ing3
        self.effect = effect
        self.color = color
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
    def getEffect(self):
        return self.effect
    def getColor(self):
        return self.color
    def getValue(self):
        return self.value

    def setAmount(self, newAmount):
        self.amount = newAmount

def InitPotionList():
    PotionList = []
    with open("Data/potionInventory.json") as f:
        PotionJson = json.load(f)  # load data as dict
    for pot in PotionJson.items():
        newPotion = Potion(pot[0],
                            pot[1].get("Name"),
                            pot[1].get("ImageLocation"),
                            DevHelpers.NameFormat(pot[1].get("Ingredient_1_ID")),
                            DevHelpers.NameFormat(pot[1].get("Ingredient_2_ID")),
                            DevHelpers.NameFormat(pot[1].get("Ingredient_3_ID")),
                            pot[1].get("Effect"),
                            pot[1].get("Color"),
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
                   "Effect": pot.getEffect(),
                   "Color": pot.getColor(),
                   "Value" : pot.getValue()}
        prepareData[pot.getID()] = newData  # Add list data to dict
    with open("Data/potionInventory.json", "w") as f: #  write to json
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
    with open("Data/locationData.json") as f:
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
    with open("Data/locationData.json", "w") as f:  # write to json
        json.dump(prepareData, f, indent=4)


#Tool info
class Tool:
    def __init__(self, ID, Name, ImgLoc, Use, InSlots, OutSlots, Unlocked):
        self.ID = ID
        self.Name = Name
        self.ImgLoc = ImgLoc
        self.Use = Use
        self.InSlots = InSlots
        self.OutSlots = OutSlots
        self.Unlocked = Unlocked

    def getID(self):
        return self.ID
    def getName(self):
        return self.Name
    def setName(self, newName):
        self.Name = newName
    def getImgLoc(self):
        return self.ImgLoc
    def getUse(self):
        return self.Use
    def getInSlots(self):
        return self.InSlots
    def getOutSlots(self):
        return self.OutSlots
    def getUnlocked(self):
        if self.Unlocked == 0:
            return False
        else:
            return True

def InitTools():
    Tools = []
    with open("Data/toolInfo.json") as f:
        toolsJson = json.load(f)  # load data as dict
    for data in toolsJson.items():
        toolData = Tool(data[0],
                            data[1].get("Name"),
                            data[1].get("ImgLoc"),
                            data[1].get("Use"),
                            data[1].get("InSlots"),
                            data[1].get("OutSlots"),
                            data[1].get("Unlocked")
                            )
        Tools.append(toolData)
    return Tools

def saveTools(Tools):
    prepareData = {}
    for tool in Tools:
        newData = {"Name": tool.getName(),
                   "ImgLoc": tool.getImgLoc(),
                   "Use": tool.getUse(),
                   "InSlots": tool.getInSlots(),
                   "OutSlots": tool.getOutSlots(),
                   "Unlocked": tool.getUnlocked(),
                    }
        prepareData[tool.getID()] = newData  # Add list data to dict
    with open("Data/toolInfo.json", "w") as f:  # write to json
        json.dump(prepareData, f, indent=4)

#Create Ingredient Recipes info
class CreateRecipe:
    def __init__(self, ID, Name, tool, Requirements, Result, Unlocked):
        self.ID = ID
        self.Name = Name
        self.Tool = tool
        self.Requirements = Requirements
        self.Result = Result
        self.Unlocked = Unlocked

    def getID(self):
        return self.ID
    def getName(self):
        return self.Name
    def setName(self, newName):
        self.Name = newName
    def getTool(self):
        return self.Tool
    def getRequirements(self):
        return self.Requirements
    def getResult(self):
        return self.Result
    def getUnlocked(self):
        return self.Unlocked


def InitCreateRecipes():
    Recipes = []
    with open("Data/combineIngredientRecipies.json") as f:
        dataJson = json.load(f)  # load data as dict
    for data in dataJson.items():
        recipeData = CreateRecipe(data[0],
                        data[1].get("Name"),
                        data[1].get("Tool"),
                        data[1].get("Requirements"),
                        data[1].get("Result"),
                        data[1].get("Unlocked")
                        )
        Recipes.append(recipeData)
    return Recipes

def saveCreateRecipes(Recipes):
    prepareData = {}
    for recipe in Recipes:
        newData = {"Name": recipe.getName(),
                   "Tool": recipe.getTool(),
                   "Requirements": recipe.getRequirements(),
                   "Result": recipe.getResult(),
                   "Unlocked": recipe.getUnlocked(),
                    }
        prepareData[recipe.getID()] = newData  # Add list data to dict
    with open("Data/combineIngredientRecipies.json", "w") as f:  # write to json
        json.dump(prepareData, f, indent=4)




#Extract Ingredient Recipes info
class ExtractRecipe:
    def __init__(self, ID, Name, Tool, Requirement, Results, Unlocked):
        self.ID = ID
        self.Name = Name
        self.Tool = Tool
        self.Requirement = Requirement
        self.Results = Results
        self.Unlocked = Unlocked

    def getID(self):
        return self.ID
    def getName(self):
        return self.Name
    def setName(self, newName):
        self.Name = newName
    def getTool(self):
        return self.Tool
    def getRequirement(self):
        return self.Requirement
    def getResults(self):
        return self.Results
    def getUnlocked(self):
        return self.Unlocked

def InitExtractRecipes():
    Recipes = []
    with open("Data/extractIngredientRecipies.json") as f:
        dataJson = json.load(f)  # load data as dict
    for data in dataJson.items():
        recipeData = ExtractRecipe(data[0],
                        data[1].get("Name"),
                        data[1].get("Tool"),
                        data[1].get("Requirement"),
                        data[1].get("Results"),
                        data[1].get("Unlocked")
                        )
        Recipes.append(recipeData)
    return Recipes

def saveExtractRecipes(Recipes):
    prepareData = {}
    for recipe in Recipes:
        newData = {"Name": recipe.getName(),
                   "Tool": recipe.getTool(),
                   "Requirement": recipe.getRequirement(),
                   "Results": recipe.getResults(),
                   "Unlocked": recipe.getUnlocked(),
                    }
        prepareData[recipe.getID()] = newData  # Add list data to dict
    with open("Data/extractIngredientRecipies.json", "w") as f:  # write to json
        json.dump(prepareData, f, indent=4)



#New object file
class jdata:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name

    def getID(self):
        return self.ID
    def getName(self):
        return self.Name
    def setName(self, newName):
        self.Name = newName

def InitJdata():
    Jdata = []
    with open("Data/Jdata.json") as f:
        locJson = json.load(f)  # load data as dict
    for data in locJson.items():
        jdataEntry = jdata(data[0],
                            data[1].get("Name")
                            )
        Jdata.append(jdataEntry)
    return Jdata

def saveJdata(Jdata):
    prepareData = {}
    for dat in Jdata:
        newData = {"Name": dat.getName()
                    }
        prepareData[dat.getID()] = newData  # Add list data to dict
    with open("Data/Jdata.json", "w") as f:  # write to json
        json.dump(prepareData, f, indent=4)






