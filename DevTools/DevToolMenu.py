from DevTools.CreateLocation import createLocation
from DevTools.CreateIngredient import createIngredient
from DevTools.EditLocation import editLocation
from DevTools.EditIngredient import editIngredient




while(True):
    print("=====DEV TOOLS=====")
    print("Select an option, q to quit")
    print("CreateIngredient [CI] | CreateLocation [CL]| EditIngredient [EI] | EditLocation [EL]")
    option = input().upper()
    if option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END":
        exit()
    if option == "CREATEINGREDIENT"  or option == "CI":
        createIngredient()
        continue
    if option == "CREATELOCATION" or option == "CL":
        createLocation()
        continue
    if option == "EDITINGREDIENT" or option == "EI":
        editIngredient()
        continue
    if option == "EDITLOCATION" or option == "EL":
        editLocation()
        continue
