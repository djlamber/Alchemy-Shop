import helpers
import sys
import os.path

#This is a tool that uses the terminal to add new ingredients

Ingredients = helpers.InitIngredients()
Running = True
while(Running):
    ID = input("Input ID:")
    setContinue = False
    for I in Ingredients:
        if I.getID() == ID:
            print("ID already taken")
            setContinue = True
            break
    if setContinue:
        continue
    name = input("Input Name:")
    img = input("Input Image directory")
    if not os.path.exists(img):
        print("Path does not exist, setting default")
        img = "sprites/UnknownWhite.png"
    category = input("Input Categories, separated by a comma:")
    amount = input("Input Amount")
    if int(amount) < 0:
        amount = 1
    effect1 = input("Input Effect 1:")
    effect2 = input("Input Effect 2:")
    effect3 = input("Input Effect 3:")
    newIngre = helpers.Ingredient(ID, name, img, category, int(amount), effect1, effect2, effect3)
    Ingredients.append(newIngre)
    ans = input("Sucessfully added to list, continue? (y/n)")
    if ans == 'n':
        Running = False
helpers.saveIngredients(Ingredients)

