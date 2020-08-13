from DevTools.CreateLocation import createLocation
from DevTools.CreateIngredient import createIngredient



while(True):
    print("=====DEV TOOLS=====")
    print("Select an option, q to quit")
    print("CreateIngredient | CreateLocation")
    option = input().upper()
    if option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END":
        exit()
    if option == "CREATEINGREDIENT" or option == "INGREDIENT" or option == "CI":
        createIngredient()
        continue
    if option == "CREATELOCATION" or option == "LOCATION" or option == "CL":
        createLocation()
    #TODO: add edit options
        continue
