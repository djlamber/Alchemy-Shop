import helpers
import sys
import os.path

def editLocation():
    Locations = helpers.InitLocations()
    Ingredients = helpers.InitIngredients()
    Ingredients.sort(key=lambda k: k.getName())
    Running = True
    print("=====Edit Location=====")
    while Running:
        print("Type \'list\' to see all locations")
        print("Type q to quit")
        print("Select List to Edit:")
        entry = input()
        option = entry.upper()
        if option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END":
            Running = False
            break