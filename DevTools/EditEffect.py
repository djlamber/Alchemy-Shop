import helpers
import sys
import os.path
from DevTools import DevHelpers


def editEffectIngName(effect, name):
    print("Current Ingredient name for ["+str(effect.getID())+"] : " + str(name))
    newName = input("Input new name or null to go back: ")
    if newName == "":
        return name
    else:
        return DevHelpers.NameFormat(newName)

def editEffectPotName(effect, name):
    print("Current Potion name for ["+str(effect.getID())+"] : " + str(name))
    newName = input("Input new name or null to go back: ")
    if newName == "":
        return name
    else:
        return DevHelpers.NameFormat(newName)

def editEffectUpName(effect, name):
    print("Current Upgrade name for ["+str(effect.getID())+"] : " + str(name))
    newName = input("Input new name or null to go back: ")
    if newName == "":
        return name
    else:
        return DevHelpers.NameFormat(newName)



def editEffect():
    Effects = helpers.InitEffects()
    Effects.sort(key=lambda k: k.getID())
    Running = True
    effect = None
    while Running:
        print("=====Edit Effects=====")
        while(Running):
            print("Type \'list\' to see all effects")
            print("Type q to quit")
            print("Select Effect ID to Edit:")
            entry = input()
            option = entry.upper()
            if option == "" or option == "Q" or option == "EXIT" or option == "QUIT" or option == "STOP" or option == "END":
                Running = False
                break
            if option.upper() == "LIST":
                DevHelpers.printEffects(Effects)
            else:
                setToBreak = False
                effectID = DevHelpers.IDFormat(option)

                for i in Effects:
                    if i.getID() == effectID:
                        effect = i
                        setToBreak = True
                        break
                if setToBreak:
                    break
        if not Running:
            break

        #get vars ready
        ingName = effect.getIngName()
        potName = effect.getPotName()
        upName = effect.getUpName()


        editingIngredient = True
        while(editingIngredient):
            print("\nSelect Attribute to Edit for ["+str(effect.getID())+"]")
            print("Type s to save and continue, q save and quit")
            print("Ingredient Name | Potion Name | Upgrade Name")
            attrib = input().upper()
            if attrib == "" or attrib == "Q" or attrib == "EXIT" or attrib == "QUIT" or attrib == "STOP" or attrib == "END":
                newEffect = helpers.Effect(effect.getID(), ingName, potName, upName)
                Effects.append(newEffect)
                helpers.saveEffects(Effects)
                Effects = helpers.InitEffects()
                print("Successfully saved")
                editingIngredient = False
                break
            if attrib == "INGREDIENTNAME" or attrib == "INGREDIENT NAME" or attrib == "IN":
                ingName = editEffectIngName(effect, ingName)

            if attrib == "POTIONNAME" or attrib == "POTION NAME" or attrib == "PN":
                potName = editEffectIngName(effect, potName)

            if attrib == "UPGRADENAME" or attrib == "UPGRADE NAME" or attrib == "UN":
                upName = editEffectIngName(effect, upName)

            if attrib == "SAVE" or attrib == "S":
                newEffect = helpers.Effect(effect.getID(), ingName, potName, upName)
                Effects.append(newEffect)
                helpers.saveEffects(Effects)
                Effects = helpers.InitEffects()
                print("Successfully saved")