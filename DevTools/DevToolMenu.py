from DevTools.CreateLocation import createLocation
from DevTools.CreateIngredient import createIngredient
from DevTools.CreateEffect import createEffect
from DevTools.CreateRecipe import createRecipe
from DevTools.CreateTool import createTool

from DevTools.EditLocation import editLocation
from DevTools.EditIngredient import editIngredient
from DevTools.EditEffect import editEffect
from DevTools.EditRecipe import editRecipe
from DevTools.EditTool import editTool




while(True):
    print("=====DEV TOOLS=====")
    print("Select an option, q to quit")
    print("CreateIngredient [CI] | CreateEffect [CE] | CreateLocation [CL]| CreateRecipe [CR] | CreateTool [CT]")
    print("EditIngredient   [EI] | EditEffect   [EE] | EditLocation   [EL]| EditRecipe   [ER] | EditTool   [ET]")
    option = input().upper()
    if option == "" or option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END":
        exit()
    if option == "CREATEINGREDIENT"  or option == "CI":
        createIngredient()
        continue
    if option == "CREATEEFFECT" or option == "CE":
        createEffect()
        continue
    if option == "CREATELOCATION" or option == "CL":
        createLocation()
        continue
    if option == "CREATERECIPE" or option == "CR":
        createRecipe()
        continue
    if option == "CREATETOOL" or option == "CT":
        createTool()
        continue

    if option == "EDITINGREDIENT" or option == "EI":
        editIngredient()
        continue
    if option == "EDITEFFECT" or option == "EE":
        editEffect()
        continue
    if option == "EDITLOCATION" or option == "EL":
        editLocation()
        continue
    if option == "EDITRECIPE" or option == "ER":
        editRecipe()
        continue
    if option == "EDITTOOL" or option == "ET":
        editTool()
        continue
