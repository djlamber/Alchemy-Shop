import helpers
import sys
import os.path

#This is a tool that uses the terminal to add new ingredients

Ingredients = helpers.InitIngredients()
Running = True
while(Running):
    ID = input("Input ID: ")
    ID = helpers.IDFormat(ID)
    setContinue = False
    for I in Ingredients:
        if I.getID() == ID:
            print("ID already taken")
            setContinue = True
            break
    if setContinue:
        continue
    name = input("Input Name: ")
    name = helpers.NameFormat(name)
    img = input("Input Image directory: ")
    if not os.path.exists(img):
        print("Path does not exist, setting default")
        img = "sprites/UnknownWhite.png"
    category = input("Input Categories, separated by a comma: ")
    categoryList = category.split(",")
    for i in range(len(categoryList)):
        if categoryList[i] == " ":
            continue
        categoryList[i] = helpers.NameFormat(categoryList[i])
    while (True):
        amount = input("Input Amount: ")
        if amount == "":
            amount = 0
            break
        try:
            amount = int(amount)
        except ValueError:
            print("That is not a integer")
        if type(amount) == int:
            if amount < 0:
                amount = 0
            break;
    effects = []
    for i in range(3):
        effect = input("Input Effect "+str(i) + ": ")
        effect = helpers.NameFormat(effect)
        if effect == "" or effect == " " or effect == "N":
            effect = "None"
        effects.append(effect)
    newIngre = helpers.Ingredient(ID, name, img, categoryList, int(amount), effects[0], effects[1], effects[2])
    Ingredients.append(newIngre)
    ans = input("Sucessfully added to list, continue? (y/n): ")
    if ans == 'n':
        Running = False
helpers.saveIngredients(Ingredients)

