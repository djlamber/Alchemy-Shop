import helpers
import sys
import os.path
from constants import *
from DevTools import DevHelpers

#This is a tool that uses the terminal to add new recipe



def createRecipe():
    Tools = helpers.InitTools()
    Ingredients = helpers.InitIngredients()
    Ingredients.sort(key=lambda k: k.getName())
    Combinations = helpers.InitCreateRecipes()
    Extractions = helpers.InitExtractRecipes()
    Running = True
    print("=====Create Recipe=====")
    RecipeType = None
    while Running:
        while True:
            print("Type Q to quit")
            option = input("Select Type of Recipe (Combination | Extraction): ").upper()
            option = option.upper()
            if option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END":
                Running = False
                break
            if option == "COMBINATION" or option == "C":
                RecipeType = "Combination"
                break
            if option == "EXTRACTION" or option == "E":
                RecipeType = "Extraction"
                break
            print("Invalid option\n")

        if RecipeType == None:
            print("How did you get here?")

        while True:
            # Select ID
            ID = input("Input ID: ")
            ID = DevHelpers.IDFormat(ID)

            for T in Tools:
                if T.getID() == ID:
                    print("ID already taken")
                    continue
            break

        # Select Name
        name = input("Input Name: ")
        name = DevHelpers.NameFormat(name)

        #Select Tool
        selectedTool = None
        while True:
            leave = False
            tool = input("Select Tool, Type \'List\' to list tools:")
            if tool.upper() == "LIST" or tool.upper() == "L":
                DevHelpers.printTools(Tools, RecipeType)
                continue
            tool = DevHelpers.IDFormat(tool)
            for i in Tools:
                if i.getID() == tool:
                    if i.getUse() == RecipeType:
                        leave = True
                        selectedTool = i
                        break
                    else:
                        break
            if leave == True:
                break
            print("Invalid Tool ["+ str(tool) +"]\n")

        #Select Requrement(s)
        reqs = []
        print("\nType \'List\' to list out ingredients")
        for i in range(selectedTool.getInSlots()):
            while True:
                leave = False
                ingre = input("Input Ingredient requirement #"+ str(i+1) + ": ")
                if ingre.upper() == "LIST" or ingre.upper() == "L":
                    DevHelpers.printIngredients(Ingredients)
                    continue
                ingre = DevHelpers.IDFormat(ingre)
                for ing in Ingredients:
                    if ing.getID() == ingre:
                        reqs.append(ingre)
                        leave = True
                        break
                if leave:
                    break
                print("Invalid Ingredient: ["+ ingre +"]\n")
                print("Type \'List\' to list out ingredients")

        # Select Results(s)
        results = []
        print("\nType \'List\' to list out ingredients")
        for i in range(selectedTool.getOutSlots()):
            while True:
                leave = False

                ingre = input("Input Ingredient results #" + str(i+1) + ": ")
                if ingre.upper() == "LIST" or ingre.upper() == "L":
                    DevHelpers.printIngredients(Ingredients)
                    continue
                ingre = DevHelpers.IDFormat(ingre)
                for ing in Ingredients:
                    if ing.getID() == ingre:
                        results.append(ingre)
                        leave = True
                        break
                if leave:
                    break
                print("Invalid Ingredient: ["+ ingre +"]\n")
                print("Type \'List\' to list out ingredients")

        # Select Unlocked status
        unlocked = input("Select unlocked status (True | False): ").upper()
        if unlocked == "TRUE" or unlocked == "T":
            unlocked = True
        elif unlocked == "FALSE" or unlocked == "F":
            unlocked = False
        else:
            print("Invalid input, setting to True")
            unlocked = True

        # Create Recipe
        if RecipeType == "Extraction":
            newRecipe = helpers.ExtractRecipe(ID, name, tool, reqs, results, unlocked)
            Extractions.append(newRecipe)
        elif RecipeType == "Combination":
            newRecipe = helpers.CombineRecipe(ID, name, tool, reqs, results, unlocked)
            Combinations.append(newRecipe)
        ans = input("Sucessfully added to list, continue? (y/n): ")
        if ans.upper() != 'Y':
            Running = False
    helpers.saveExtractRecipes(Extractions)
    helpers.saveCreateRecipes(Combinations)



