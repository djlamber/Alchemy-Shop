from helpers import *

import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def addToEmptySlot(ingredient):

    if config.selectedIngredients[0] == ingredient or config.selectedIngredients[1] == ingredient or config.selectedIngredients[2] == ingredient:
        return
    elif config.selectedIngredients[0] == config.NoneIngredient:
        config.selectedIngredients[0] = ingredient
        ingredient.amount -= 1
    elif config.selectedIngredients[1] == config.NoneIngredient:
        config.selectedIngredients[1] = ingredient
        ingredient.amount -=1
    elif config.selectedIngredients[2] == config.NoneIngredient:
        config.selectedIngredients[2] = ingredient
        ingredient.amount -=1

def removeSlot(ingredient):
    for i in range(len(config.selectedIngredients)):
        if config.selectedIngredients[i] == ingredient:
            ingredient.amount +=1
            config.selectedIngredients[i] = config.NoneIngredient


def brewPotion(startTime):
    # TODO: add variation in potion brewing based on ingredients
    # Idea: bad potions can be made that take up space in inventory and have to be sold
    if len(config.PotionList)<65:
        potVal = int((config.selectedIngredients[0].getValue() * 0.3 + config.selectedIngredients[1].getValue() * 0.6 + config.selectedIngredients[2].getValue() * 0.9) * (random()+1)  )
        effect = "None"
        color = [(config.selectedIngredients[0].getColor()[0] + config.selectedIngredients[0].getColor()[1] + config.selectedIngredients[0].getColor()[2])/3,
                 (config.selectedIngredients[1].getColor()[0] + config.selectedIngredients[1].getColor()[1] + config.selectedIngredients[1].getColor()[2]) / 3,
                 (config.selectedIngredients[2].getColor()[0] + config.selectedIngredients[2].getColor()[1] + config.selectedIngredients[2].getColor()[2]) / 3
                 ]
        newPotion = Potion(str(random()), "Potion Name", "sprites/potions/"+randomPotionColor(), config.selectedIngredients[0].getID(), config.selectedIngredients[1].getID(), config.selectedIngredients[2].getID(), effect, color, potVal)
        config.PotionList.append(newPotion)
        savePotions(config.PotionList)
        saveIngredients(config.Ingredients)
        clearPotionSlots()
        startTime[0] = time_ns()

def brewMultiPotion(info):
    n = info[1]
    ig1 = config.selectedIngredients[0]
    ig2 = config.selectedIngredients[1]
    ig3 = config.selectedIngredients[2]
    for m in range(n):
        print(m)
        addToEmptySlot(ig1)
        addToEmptySlot(ig2)
        addToEmptySlot(ig3)
        brewPotion(info[0])

def clearPotionSlots():
    config.selectedIngredients[0] = config.NoneIngredient
    config.selectedIngredients[1] = config.NoneIngredient
    config.selectedIngredients[2] = config.NoneIngredient

def sortListNext(l):
    first = l.pop(0)
    l.append(first)




#################### MainMenu Screen ####################

def mainMenu():
    while True:
        #TODO: move each screen to separate files, send important info through call
        
        # check events
        checkEvents()
        # draw on screen
        Back_Color = WHITE
        config.screen.fill(Back_Color)


        draw_text_center('Alchemy Shop', font48, BLACK, config.screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        button_rect_text_center(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5, 80, 40, Back_Color, GREEN, 'Start', font32, BLACK, config.screen,LC, potionCreation)
        button_rect_text_center(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 100, 40, Back_Color, BLUE, 'Options', font32, BLACK,config.screen,LC, None)
        button_rect_text_center(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.67, 60, 40, Back_Color, RED, 'Quit', font32, BLACK, config.screen,LC, exit)

        pygame.display.flip() # update screen

#################### potionCreation Screen ####################
def potionCreation():
    pageNum = [0]
    ingSortTypes = [ "Category", "Category R","Amount R", "Amount", "Name", "Name R", "Index", "Index R"]
    start_time = [0]
    while True:
        # check events
        checkEvents()

        #TODO: buy and sell ingredients

        # draw on screen
        Back_Color = BLACK
        config.screen.fill(Back_Color)

        #  buttons to change screens
        button_rect_text(SCREEN_WIDTH - 140, 0, 120, 40, Back_Color, GREEN, 'Main Menu', font32, WHITE, config.screen,LC, mainMenu)
        button_rect_text(SCREEN_WIDTH * 11 / 16 - 24, 0, 140, 40, Back_Color, PURPLE, 'Potion List', font32, WHITE, config.screen, LC, potionInventory)
        button_rect_text(SCREEN_WIDTH * 6 / 16 - 24, 0, 280, 40, Back_Color, MAROON, 'Gather Ingredients', font32, WHITE, config.screen, LC, ingredientGather)

        #  display player gold
        draw_text("Gold: " + str(config.Player.getGold()), font32, YELLOW, config.screen, 10, 5)

        #  display cauldron
        draw_image((SCREEN_WIDTH - 160) * 6 / 8, (SCREEN_HEIGHT - 160) / 2, 160, 160, "sprites/Cauldron.png", config.screen)

        # display ingredient slots
        button_img_img((SCREEN_WIDTH - 306) * 6 / 8, (SCREEN_HEIGHT - 220) / 2, 80, 80,
                       "sprites/BlueBorder.png", "sprites/YellowBorder.png", config.selectedIngredients[0].imgLoc, config.screen, LC,removeSlot, config.selectedIngredients[0])
        button_img_img((SCREEN_WIDTH - 106) * 6 / 8, (SCREEN_HEIGHT - 340) / 2, 80, 80,
                       "sprites/BlueBorder.png", "sprites/YellowBorder.png", config.selectedIngredients[1].imgLoc, config.screen, LC,removeSlot, config.selectedIngredients[1])
        button_img_img((SCREEN_WIDTH + 94) * 6 / 8, (SCREEN_HEIGHT - 220) / 2, 80, 80,
                       "sprites/BlueBorder.png", "sprites/YellowBorder.png", config.selectedIngredients[2].imgLoc, config.screen, LC,removeSlot, config.selectedIngredients[2])
        #display brew button
        if config.selectedIngredients[0] != config.NoneIngredient and config.selectedIngredients[1] != config.NoneIngredient and config.selectedIngredients[2] != config.NoneIngredient and len(config.PotionList)<65:
            button_rect_text((SCREEN_WIDTH - 130)  * 6 / 8, (SCREEN_HEIGHT + 220) / 2, 120, 80, Back_Color, GREEN, "Brew!", font48, WHITE, config.screen, LC, brewPotion, start_time)
            if len(config.PotionList) < 61 and config.selectedIngredients[0].getAmount() > 4 and config.selectedIngredients[1].getAmount() > 4 and config.selectedIngredients[2].getAmount() > 4:
                button_rect_text((SCREEN_WIDTH - 130) * 6 / 8 + 00, (SCREEN_HEIGHT + 380) / 2, 30, 20, Back_Color, GREEN, " 5x", font20, WHITE, config.screen, LC, brewMultiPotion, (start_time,5))
            if len(config.PotionList) < 56 and config.selectedIngredients[0].getAmount() > 9 and config.selectedIngredients[1].getAmount() > 9 and config.selectedIngredients[2].getAmount() > 9:
                button_rect_text((SCREEN_WIDTH - 130) * 6 / 8 + 30, (SCREEN_HEIGHT + 380) / 2, 30, 20, Back_Color, GREEN, "10x", font20, WHITE, config.screen, LC, brewMultiPotion, (start_time,10))
            if len(config.PotionList) < 46 and config.selectedIngredients[0].getAmount() > 19 and config.selectedIngredients[1].getAmount() > 19 and config.selectedIngredients[2].getAmount() > 19:
                button_rect_text((SCREEN_WIDTH - 130) * 6 / 8 + 60, (SCREEN_HEIGHT + 380) / 2, 30, 20, Back_Color, GREEN, "20x", font20, WHITE, config.screen, LC, brewMultiPotion, (start_time,20))
            if len(config.PotionList) < 64 :
                smallIng = min(config.selectedIngredients[0].getAmount(),config.selectedIngredients[1].getAmount(),config.selectedIngredients[2].getAmount())
                button_rect_text((SCREEN_WIDTH - 130) * 6 / 8 + 90, (SCREEN_HEIGHT + 380) / 2, 30, 20, Back_Color, GREEN, "Max", font20, WHITE, config.screen, LC, brewMultiPotion, (start_time,smallIng+1))


        if time_ns() - start_time[0] < 2000000000: #display full inventory
            draw_text_center(config.PotionList[-1].getName(), font48, WHITE, config.screen, (SCREEN_WIDTH - 130) * 6 / 8 + 60, (SCREEN_HEIGHT + 320) / 2 + 40)
            draw_image_center((SCREEN_WIDTH - 130) * 6 / 8 + 60, (SCREEN_HEIGHT + 170) / 2 + 40, 120,120, config.PotionList[-1].getImgLoc(), config.screen)
        elif len(config.PotionList)==65: #display most recent potion
            draw_text_center("Inventory Full", font48, WHITE, config.screen, (SCREEN_WIDTH - 130) * 6 / 8 + 60, (SCREEN_HEIGHT + 220) / 2 + 40)


        entNum = 0
        posX = 0
        posY = 0
        displayIngredientNum = 0

        amountIngredients = 0
        for ingredient in config.Ingredients: # get num of usable ingredients
            if ingredient.amount > 0:
                amountIngredients +=1
        numPages = int((amountIngredients-1)/24) #get num of pages
        if pageNum[0] > numPages: #only allow visit pages with something in it
            pageNum[0] = numPages
        if pageNum[0] > 0:
            button_img(100, 40, 160, 40, "sprites/WideArrowUP.png", "sprites/WideArrowUp.png",config.screen, LC, DecreaseVal, pageNum)
        if pageNum[0] < numPages:
            button_img(100, 675, 160, 40, "sprites/WideArrowDown.png", "sprites/WideArrowDown.png", config.screen, LC, IncreaseVal, pageNum)


        #Sorting ingredients
        button_rect_text(SCREEN_WIDTH * 3 / 16 - 24, 0, 170, 40, Back_Color, GRAY, 'Sort Ingredients', font32, WHITE, config.screen, LC, sortListNext, ingSortTypes)

        if ingSortTypes[0] == "Name":
            config.Ingredients.sort(key=lambda k: k.getName())
        elif ingSortTypes[0] == "Name R":
            config.Ingredients.sort(reverse = True, key=lambda k: k.getName())
        elif ingSortTypes[0] == "Category":
            config.Ingredients.sort(key=lambda k: k.getCategory())
        elif ingSortTypes[0] == "Category R":
            config.Ingredients.sort(reverse = True, key=lambda k: k.getCategory())
        elif ingSortTypes[0] == "Amount":
            config.Ingredients.sort(key=lambda k: k.getAmount())
        elif ingSortTypes[0] == "Amount R":
            config.Ingredients.sort(reverse = True, key=lambda k: k.getAmount())
        elif ingSortTypes[0] == "Index":
            config.Ingredients.sort(key=lambda k: k.getID())
        elif ingSortTypes[0] == "Index R":
            config.Ingredients.sort(reverse=True, key=lambda k: k.getID())


        for ingredient in config.Ingredients: # display ingredients
            if ingredient.amount < 1:
                continue
            displayIngredientNum +=1
            if displayIngredientNum < pageNum[0] * 24 +1:
                continue
            if displayIngredientNum > pageNum[0] * 24 + 24:
                continue
            if entNum % 4 == 0:
                posX = 0
                posY += 1
            if ingredient in config.selectedIngredients:
                button_img_img(100 * posX, 100 * posY - 20, 80, 80, "sprites/GreenBorder.png", "sprites/RedBorder.png",
                               ingredient.imgLoc, config.screen, RC, removeSlot, ingredient)
            else:
                button_img_img(100 * posX, 100 * posY - 20, 80, 80, "sprites/Nothing.png", "sprites/GreenBorder.png",
                           ingredient.imgLoc, config.screen, LC, addToEmptySlot, ingredient)
            draw_text_center(ingredient.name, font16, WHITE, config.screen, 100 * posX + 40, 100 * posY + 70)
            draw_text(str(ingredient.amount), font16, WHITE, config.screen, 100 * posX + 5, 100 * posY + 45)


            posX += 1
            entNum += 1
        #display ingredient effects
        entNum = 0
        posX = 0
        posY = 0
        displayIngredientNum = 0
        for ingredient in config.Ingredients:
            if ingredient.amount < 1:
                continue
            displayIngredientNum += 1
            if displayIngredientNum < pageNum[0] * 24 + 1:
                continue
            if displayIngredientNum > pageNum[0] * 24 + 24:
                continue
            if entNum % 4 == 0:
                posX = 0
                posY += 1

            textlen = max(len(ingredient.effect_1) * 12, len(ingredient.effect_2) * 12, len(ingredient.effect_3) * 12)
            if ingredient.effect_1 != "None":
                hoverover_text(100 * posX, 100 * posY - 20, 80, 80, SILVER, config.screen, ingredient.effect_1, font20, BLACK, 10, 0, setWidth=textlen)
            if ingredient.effect_2 != "None":
                hoverover_text(100 * posX, 100 * posY - 20, 80, 80, SILVER, config.screen, ingredient.effect_2, font20, BLACK, 10, 20, setWidth=textlen)
            if ingredient.effect_3 != "None":
                hoverover_text(100 * posX, 100 * posY - 20, 80, 80, SILVER, config.screen, ingredient.effect_3, font20, BLACK, 10, 40, setWidth=textlen)
            posX += 1
            entNum += 1
        pygame.display.flip() # update screen

#########################################################

def selectPotion(data):
    potionID = data[0]
    posX = data[1]
    posY = data[2]
    config.selectedPotions[potionID] = (posX, posY)
    config.runningTotal += potionID.getValue()


def deselectPotion(data):
    config.runningTotal -= data.getValue()
    config.selectedPotions.pop(data)


def selectAllPots():
    i = 0
    row_x = 0
    row_y = 0
    for pot in config.PotionList:
        if i % 13 == 0:
            row_x = 0
            row_y += 1
        selectPotion((pot, row_x, row_y))
        row_x += 1
        i += 1


def deselectAllPots():
    config.selectedPotions.clear()
    config.runningTotal = 0


def sellSelectedPotions():
    for i in config.selectedPotions:
        config.Player.addGold(i.getValue())
        config.PotionList.remove(i)
    config.selectedPotions.clear()
    savePotions(config.PotionList)
    savePlayer(config.Player)
    config.runningTotal = 0


def sellAllPotions():
    for i in config.PotionList:
        config.Player.addGold(i.getValue())
    config.PotionList.clear()
    config.selectedPotions.clear()
    savePotions(config.PotionList)
    savePlayer(config.Player)
    config.runningTotal = 0


#################### potion Inventory Screen ####################
def potionInventory():

    while True:
        # check events
        checkEvents()
        #TODO: look at potion stats/info when hovering over with mouse

        # draw on screen
        Back_Color = BLACK
        config.screen.fill(Back_Color)

        #  buttons to change screens
        button_rect_text(SCREEN_WIDTH - 140, 0, 120, 40, Back_Color, GREEN, 'Main Menu', font32, WHITE, config.screen, LC, mainMenu)
        button_rect_text(SCREEN_WIDTH * 11 / 16 - 24, 0, 170, 40, Back_Color, PURPLE, 'Potion Creation', font32, WHITE, config.screen, LC, potionCreation)

        # select options
        button_rect_text(SCREEN_WIDTH * 4 / 16 - 24, 0, 170, 40, Back_Color, RED, 'Deselect all', font32, WHITE, config.screen, LC, deselectAllPots)
        button_rect_text(SCREEN_WIDTH * 6 / 16 - 24, 0, 170, 40, Back_Color, GREEN, 'Select all', font32, WHITE, config.screen, LC, selectAllPots)

        #  Sell button
        button_rect_text_center(SCREEN_WIDTH/2, SCREEN_HEIGHT - 40, 60, 40, Back_Color, GREEN, 'Sell', font32, WHITE, config.screen,LC, sellSelectedPotions)
        button_rect_text_center(SCREEN_WIDTH - 80, SCREEN_HEIGHT - 40, 120, 40, Back_Color, GREEN, 'Sell All', font32, WHITE, config.screen, LC, sellAllPotions)

        # Display Player Gold
        draw_text("Gold: "+ str(config.Player.getGold()), font32, YELLOW, config.screen, 10, 5)
        draw_text_center("Value: " + str(config.runningTotal), font32, YELLOW, config.screen, SCREEN_WIDTH/2, SCREEN_HEIGHT - 80,)

        entNum = 0
        row_x = 0
        row_y = 0

        for pot in config.PotionList:

            if entNum % 13 == 0:
                row_x = 0
                row_y += 1
            if pot in config.selectedPotions.keys(): # click to remove from selected list
                button_img_img(100 * row_x, 100 * row_y, 80, 80, "sprites/GreenBorder.png", "sprites/RedBorder.png",
                                   pot.imgLoc, config.screen, RC, deselectPotion, pot)
            else: # click to add to selected list
                button_img_img(100 * row_x, 100 * row_y, 80, 80, "sprites/Nothing.png", "sprites/YellowBorder.png",
                               pot.imgLoc, config.screen, LC, selectPotion, (pot, row_x, row_y))

            draw_text_center(pot.name, font16, WHITE, config.screen, 100 * row_x + 40, 100 * row_y - 10)
            draw_text(str(pot.value), font16, WHITE, config.screen, 100 * row_x + 5, 100 * row_y + 65)
            row_x += 1
            entNum += 1


        row_x = 0
        row_y = 0
        entNum = 0
        for pot in config.PotionList:
            if entNum % 13 == 0:
                row_x = 0
                row_y += 1
            if pot.effect != "None":
                if row_x > 6:
                    hoverover_text(100 * row_x, 100 * row_y - 20, 80, 80, SILVER, config.screen, pot.effect, font20, BLACK, 0, 0, "Left")
                else:
                    hoverover_text(100 * row_x, 100 * row_y - 20, 80, 80, SILVER, config.screen, pot.effect, font20, BLACK, 10, 0)

            row_x += 1
            entNum += 1

        pygame.display.flip()  # update screen

###########################################################

def checkPrereqs():
    #TODO: expand upon showing what reqs are not met
    if config.CurrentLocation is None:
        return False
    prereqs = [None, None, None]
    prereqs[0] = config.CurrentLocation.getPrereq1()
    prereqs[1] = config.CurrentLocation.getPrereq2()
    prereqs[2] = config.CurrentLocation.getPrereq3()
    for i in range(3):

        req = prereqs[i]
        if req == "None": # prereq = none
            continue
        if list(req.keys())[0] == "Gold": # prereq = gold
            if config.Player.getGold() < req.get(list(req.keys())[0]):
                return False
        if list(req.keys())[0] == "Potion":  # prereq = potion
            #TODO: Add how potions are checked
            continue
    return True


def gatherIngredient():
    #remove prereqs from player
    prereqs = [None, None, None]
    prereqs[0] = config.CurrentLocation.getPrereq1()
    prereqs[1] = config.CurrentLocation.getPrereq2()
    prereqs[2] = config.CurrentLocation.getPrereq3()
    for i in range(3):
        req = prereqs[i]
        if req == "None":  # prereq = none
            continue
        if list(req.keys())[0] == "Gold":  # prereq = gold
            config.Player.subGold(req.get(list(req.keys())[0]))
        if list(req.keys())[0] == "Potion":  # prereq = potion
            continue


    for i in range(len(config.CurrentLocation.getIngredients())):
        ingre = config.CurrentLocation.getIngredients()[i]
        dropRates = config.CurrentLocation.getDropRates()[i]
        print(str(ingre) + " " + str(dropRates))
        found = 0
        for ing in config.Ingredients:
            if ing.getID() == ingre:
                for i in range(dropRates[1]):
                    if random() < dropRates[0]:
                        found +=1
                ing.addAmount(found)
                break
            continue
    saveIngredients(config.Ingredients)
    savePlayer(config.Player)
    savePotions(config.PotionList)


def selectLocation(data):
    location = data[0]
    config.CurrentLocation = location
    reqs = data[1] #add location prereqs to prereqs list
    reqs[0] = location.getPrereq1()
    reqs[1] = location.getPrereq2()
    reqs[2] = location.getPrereq3()
    catIngres = []
    for locIngre in location.getIngredients():
        for ingre in config.Ingredients:
            if ingre.getID() == locIngre:
                catIngres.append(ingre)
    config.gatherDisplayList = catIngres

def deselectLocation(data):
    config.location = None
    config.CurrentLocation = None
    data[1] = [None,None,None]
    config.gatherDisplayList = []
    reqs = data[1]
    reqs[0] = None
    reqs[1] = None
    reqs[2] = None


#################### Basic Screen ####################
def ingredientGather():
    prereqs = [None, None, None] #[Prereq1, Prereq2, Prereq3]
    pageNum = [0]
    config.gatherDisplayList = []
    config.CurrentLocation = None

    while True:
        # check events
        checkEvents()
        #TODO: show screen of all gathered Ingredients
        #TODO: expand upon areas that require specific prereqs
        Back_Color = GRAY
        config.screen.fill(Back_Color)

        #  buttons to change screens
        button_rect_text(SCREEN_WIDTH - 140, 0, 120, 40, Back_Color, GREEN, 'Main Menu', font32, WHITE, config.screen, LC, mainMenu)
        button_rect_text(SCREEN_WIDTH * 11 / 16 - 24, 0, 170, 40, Back_Color, PURPLE, 'Potion Creation', font32, WHITE, config.screen, LC, potionCreation)

        #  display player gold
        draw_text("Gold: " + str(config.Player.getGold()), font32, YELLOW, config.screen, 10, 5)

        #display gather button
        #print(config.CurrentLocation)
        if checkPrereqs():
            button_rect_text_center(SCREEN_WIDTH/2, SCREEN_HEIGHT-40, 280, 40, Back_Color, MAROON, 'Gather Ingredients', font32, WHITE, config.screen, LC, gatherIngredient)

        x = 0

        #display prereqs
        i = 0
        x_off = 0
        y_off = 0
        for req in prereqs:
            if i == 0:
                x_off = -80
                y_off = 80
            elif i == 1:
                x_off = 0
                y_off = 0
            elif i == 2:
                x_off = 80
                y_off = 80
            if req is None:
                continue
            elif req == "None":
                draw_image_center(SCREEN_WIDTH / 2 + x_off, SCREEN_HEIGHT / 2 + y_off, 80, 80, "sprites/Nothing.png", config.screen)
                draw_text_center("Nothing", font20, BLACK, config.screen, SCREEN_WIDTH / 2 + x_off, SCREEN_HEIGHT / 2 + 40 + y_off)
            elif req.get("Gold"):
                draw_image_center(SCREEN_WIDTH/2 + x_off, SCREEN_HEIGHT/2 + y_off, 80, 80, "sprites/UnknownBlack.png", config.screen)
                draw_text_center(str(req.get("Gold"))+" Gold", font20, BLACK,config.screen, SCREEN_WIDTH/2 + x_off, SCREEN_HEIGHT/2 + 40 + y_off )
            elif req.get("Potion"):
                draw_image_center(SCREEN_WIDTH / 2 + x_off, SCREEN_HEIGHT / 2 + y_off, 80, 80, req.get("Potion").get("ImageLocation"), config.screen)
                draw_text_center(req.get("Potion").get("Name"), font20, BLACK, config.screen, SCREEN_WIDTH / 2 + x_off, SCREEN_HEIGHT / 2 + 40 + y_off)
            i +=1

        #display locations
        for location in config.Locations:
            locColor = location.getColor()
            textColor = [0,0,0]
            pygame.draw.rect(config.screen, locColor, (0, x * 40 + 100, 280, 40))
            if locColor == [0,0,0]:
                textColor = [255, 255, 255]

            if location == config.CurrentLocation:
                button_img_text(0, x * 40 + 100, 280, 40, "sprites/GreenBorder.png", "sprites/RedBorder.png", location.getName(), font32, textColor, config.screen, RC, deselectLocation, [location, prereqs])

            else:
                button_img_text(0, x*40 +100, 280, 40, "sprites/Nothing.png", "sprites/GreenBorder.png", location.getName(), font32, textColor, config.screen, LC, selectLocation, [location,prereqs])
            x+=1
        entNum = 0
        posX = 0
        posY = 0
        itemNum = 0

        #up and down arrows
        amountItems = len(config.gatherDisplayList)
        numPages = int((amountItems - 1) / 24)  # get num of pages
        if pageNum[0] > numPages:  # only allow visit pages with something in it
            pageNum[0] = numPages
        if pageNum[0] > 0:
            button_img(SCREEN_WIDTH - 260, 40, 160, 40, "sprites/WideArrowUP.png", "sprites/WideArrowUp.png", config.screen, LC, DecreaseVal, pageNum)
        if pageNum[0] < numPages:
            button_img(SCREEN_WIDTH - 260, 675, 160, 40, "sprites/WideArrowDown.png", "sprites/WideArrowDown.png", config.screen, LC, IncreaseVal, pageNum)

        # Displays Display list of ingredients
        for item in config.gatherDisplayList:
            itemDropRate = config.CurrentLocation.getDropRates()[entNum]
            itemNum +=1
            if itemNum < pageNum[0] * 20 +1:
                continue
            if itemNum > pageNum[0] * 20 + 20:
                continue
            if entNum % 4 == 0:
                posX = 0
                posY += 1.2
            draw_image(SCREEN_WIDTH - 400 + (100 * posX), 100 * posY - 20, 80, 80, item.imgLoc, config.screen)
            draw_text_center(item.name, font16, WHITE, config.screen,SCREEN_WIDTH - 400 + (100 * posX) + 40, 100 * posY + 70)
            draw_text(str(item.amount), font16, WHITE, config.screen,SCREEN_WIDTH - 400 +  (100 * posX)+ 5, 100 * posY + 45)
            draw_text_center("(" + str(itemDropRate[0]*100) + "%|" + str(itemDropRate[1]) + ")", font16, WHITE, config.screen, SCREEN_WIDTH - 400 + (100 * posX) + 40, 100 * posY + 83)
            #hoverover text
            textlen = max(len(item.effect_1) * 12, len(item.effect_2) * 12, len(item.effect_3) * 12)
            if item.effect_1 != "None":
                hoverover_text(SCREEN_WIDTH - 400 + (100 * posX), 100 * posY - 20, 80, 80, SILVER, config.screen, item.effect_1, font20, BLACK,10,0, "Left", textlen)
            if item.effect_2 != "None":
                hoverover_text(SCREEN_WIDTH - 400 + (100 * posX), 100 * posY - 20, 80, 80, SILVER, config.screen, item.effect_2, font20, BLACK,10,20, "Left",textlen)
            if item.effect_3 != "None":
                hoverover_text(SCREEN_WIDTH - 400 + (100 * posX), 100 * posY - 20, 80, 80, SILVER, config.screen, item.effect_3, font20, BLACK,10,40, "Left",textlen)
            posX += 1
            entNum += 1

        pygame.display.flip()  # update screen

#################### game init ####################
pygame.init()
pygame.display.set_caption("Alchemy Shop")
icon = pygame.image.load('sprites/CauldronWhiteBk.png')
pygame.display.set_icon(icon)
config.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

config.Ingredients = InitIngredients()  # initialize ingredients
config.PotionList = InitPotionList()  # initialize potions
config.Player = InitPlayer()  # initialize player
config.Locations = InitLocations() #initalize locations

saveLocations(config.Locations)

config.NoneIngredient = Ingredient("NoneIngredient", "None", "sprites/Nothing.png",["None"], WHITE, 0, 0, "None", "None", "None" )
config.selectedIngredients = [config.NoneIngredient, config.NoneIngredient, config.NoneIngredient]

mainMenu()  # start main menu Screen
exit()


#################### Basic Screen ####################
def Basic():
    while True:
        # check events
        checkEvents()
        # draw on screen
        Back_Color = WHITE
        config.screen.fill(Back_Color)

        pygame.display.flip()  # update screen