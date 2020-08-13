import helpers
import sys
import os.path

def editIngreName(ingre):


def editIngreImgLoc(ingre):
    True

def editIngreCategory(ingre):
    True

def editIngreColor(ingre):
    True

def editIngreValue(ingre):
    True

def editIngreEffect(ingre):
    True



def editIngredient():
    Ingredients = helpers.InitIngredients()
    Running = True
    ingre = None
    while Running:
        print("=====Edit Ingredient=====")
        while(Running):
            print("Type \'list\' to see all ingredients")
            print("Type q to quit")
            print("Select Ingredient ID to Edit:")
            entry = input()
            option = entry.upper()
            if option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END":
                Running = False
                break
            if option.upper() == "LIST":
                igList = ""
                x = 0
                for i in Ingredients:
                    ingStr = "[" + str(i.getID()) + "], "
                    ingStrLen = len(ingStr)
                    igList = igList + ingStr
                    if x + ingStrLen > 200:
                        igList = igList + "\n"
                        x = 0
                    x += ingStrLen
                print("\n" + igList + "\n")
            else:
                setToBreak = False
                ingreID = helpers.IDFormat(option)

                for i in Ingredients:
                    if i.getID() == ingreID:
                        ingre = i
                        setToBreak = True
                        break
                if setToBreak:
                    break
        if not Running:
            break

        #get vars ready
        name = ingre.getName()
        img = ingre.getImgLoc()
        categoryList = ingre.getCategory()
        #color = ingre.getColor()
        #value = ingre.getValue()
        effects = [ingre.getEffect1(), ingre.getEffect2(), ingre.getEffect3()]


        editingIngredient = True
        while(editingIngredient):
            print("\nSelect Attribute to Edit for ["+str(ingre.getID())+"]")
            print("Type s to save, q to quit")
            print("Name | ImageLocation | Category | Color | Value | Effect")
            attrib = input().upper()
            if attrib == "Q" or attrib == "EXIT" or attrib == "QUIT" or attrib == "STOP" or attrib == "END":
                editingIngredient = False
                break
            if attrib == "NAME" or attrib == "N":
                name = editIngreName(ingre)
            if attrib == "IMAGELOCATION" or attrib == "IMAGE" or attrib == "I" or attrib == "IMG":
                img = editIngreImgLoc(ingre)
            if attrib == "CATEGORY" or attrib == "CAT" or attrib == "CA":
                categoryList = editIngreCategory(ingre)
            if attrib == "COLOR" or attrib == "CO":
                color = editIngreColor(ingre)
            if attrib == "VALUE" or attrib == "VAL":
                amount = editIngreValue(ingre)
            if attrib == "EFFECT" or attrib == "E":
                effects = editIngreEffect(ingre)
            if attrib == "SAVE" or attrib == "S":
                newIngre = helpers.Ingredient(ingre.getID(), name, img, categoryList, ingre.getAmount(), effects[0], effects[1], effects[2])
                Ingredients.append(newIngre)
                helpers.saveIngredients(Ingredients)
                Ingredients = helpers.InitIngredients()



