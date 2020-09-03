import helpers
import config
import sys
import os.path
from DevTools import DevHelpers

def editRecipeName(recipe, name):
    print("Current name for ["+str(recipe.getID())+"] : " + str(name))
    newName = input("Input new name or null to go back: ")
    if newName == "":
        return name
    else:
        return DevHelpers.NameFormat(newName)

def editRecipeTool(recipe, tool):
    return tool

def editRecipeRequirements(recipe, reqs):
    return reqs

def editRecipeResults(recipe, results):
    return results

def editRecipeUnlocked(recipe, unlocked):
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




def editRecipe():
    Tools = helpers.InitTools()
    Ingredients = helpers.InitIngredients()
    Ingredients.sort(key=lambda k: k.getName())
    Combinations = helpers.InitCreateRecipes()
    Extractions = helpers.InitExtractRecipes()
    Running = True
    RecipeType = None
    recipe = None
    while Running:
        print("=====Edit Recipes=====")
        print("Type q to quit")
        while True:
            option = input("Select type of recipe to edit (Combination|Extraction): ").upper()
            if option == "" or option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END":
                Running = False
                break
            if option == "COMBINATION" or option == "C":
                RecipeType = "Combination"
                break
            if option == "EXTRACTION" or option == "E":
                RecipeType = "Extraction"
                break
            print("Invalid option\n")

        while (Running):
            print("Type \'list\' to see all recipes")
            print("Select Recipe ID to Edit:")
            entry = input()
            option = entry.upper()

            if option.upper() == "LIST":
                if RecipeType == "Combination":
                    DevHelpers.printRecipes(Combinations)
                elif RecipeType == "Extraction":
                    DevHelpers.printRecipes(Extractions)
                else:
                    print('How did you get here?')
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
                print("Invalid Recipe ID [" + toolID + "]\n")
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
                name = editRecipeName(tool, name)
            if attrib == "TOOL":
                use = editRecipeTool(tool, use)
            if attrib == "INSLOTS" or attrib == "IN" or attrib == "I":
                inSlots = editRecipeRequirements(tool, inSlots)
            if attrib == "OUTSLOTS" or attrib == "OUT" or attrib == "O":
                outSlots = editRecipeResults(tool, inSlots)
            if attrib == "UNLOCKED" or attrib == "U":
                unlocked = editRecipeUnlocked(tool, unlocked)

                newTool = helpers.Tool(tool.getID(), name, img, use, inSlots, outSlots, unlocked)
                Tools.append(newTool)
                helpers.saveTools(Tools)
                Tools = helpers.InitTools()
                print("Successfully saved")