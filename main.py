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


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            config.MUP = True
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainMenu()

def checkInputTextEvents(text):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            config.MUP = True
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainMenu()
            elif event.unicode.isalpha():
                text += event.unicode
            elif event.key == pygame.K_SPACE:
                text += " "
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_RETURN:
                text = ""

    return text


#################### MainMenu Screen ####################

def mainMenu():
    text = config.Player.getShopName()
    modifyingName = False
    lastTime = 0
    addToName = ""
    flip = True
    while True:

        # check events
        #checkEvents()
        text = checkInputTextEvents(text)

        if modifyingName:
            if time_ns() > lastTime + 50000000 :
                flip = not flip
                lastTime = time_ns()
            if flip:
                addToName = "|"
            else:
                addToName = ""

            config.Player.setShopName(text)

        # draw on screen
        Back_Color = SILVER
        config.screen.fill(Back_Color)

        draw_text_center(config.Player.getShopName() + addToName, font72, BLACK, config.screen, SCREEN_WIDTH / 2 -3, SCREEN_HEIGHT / 8 +3)
        draw_text_center(config.Player.getShopName() + addToName, font72, GOLD, config.screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8)

        button_text_center(SCREEN_WIDTH * 4 / 16, SCREEN_HEIGHT / 2.5, 210, 40, GREEN, 'Gather Ingredients', font32, BLACK, config.screen, LC, ingredientGather)
        button_text_center(SCREEN_WIDTH *  8 / 16, SCREEN_HEIGHT / 2.5, 160, 40, PURPLE, 'Create Potion', font32, BLACK, config.screen, LC, potionCreation)
        button_text_center(SCREEN_WIDTH * 12 / 16, SCREEN_HEIGHT / 2.5, 140, 40, YELLOW, 'Potion List', font32, BLACK, config.screen, LC, potionInventory)

        button_text_center(SCREEN_WIDTH *  4 / 16, SCREEN_HEIGHT / 2, 100, 40, TEAL, 'Market', font32, BLACK, config.screen, LC, ingredientShop)
        button_text_center(SCREEN_WIDTH *  8 / 16, SCREEN_HEIGHT / 2, 220, 40, BROWN, 'Modify Ingredients', font32, BLACK, config.screen, LC, modifyIngredients)
        button_text_center(SCREEN_WIDTH * 12 / 16, SCREEN_HEIGHT / 2, 100, 40, OLIVE, 'Ingredient Index', font32, BLACK, config.screen, LC, ingredientIndex)


        button_text_center(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 120, 100, 40, BLUE, 'Options', font32, BLACK, config.screen, LC, None)
        button_text_center(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 60, 60, 40, RED, 'Quit', font32, BLACK, config.screen, LC, exit)

        pygame.display.flip()  # update screen

##################################################

def addToEmptySlot(ingredient):

    if config.selectedIngredients[0] == ingredient or config.selectedIngredients[1] == ingredient or config.selectedIngredients[2] == ingredient:
        return
    elif config.selectedIngredients[0] == config.NoneIngredient:
        config.selectedIngredients[0] = ingredient
        ingredient.amount -= 1
        config.numSelectedIngredients += 1
        config.cauldronColor = getCaulColor()
    elif config.selectedIngredients[1] == config.NoneIngredient:
        config.selectedIngredients[1] = ingredient
        ingredient.amount -=1
        config.numSelectedIngredients += 1
        config.cauldronColor = getCaulColor()
    elif config.selectedIngredients[2] == config.NoneIngredient:
        config.selectedIngredients[2] = ingredient
        ingredient.amount -=1
        config.numSelectedIngredients += 1
        config.cauldronColor = getCaulColor()


def removeSlot(ingredient):
    for i in range(len(config.selectedIngredients)):
        if config.selectedIngredients[i] == ingredient:
            ingredient.amount +=1
            config.selectedIngredients[i] = config.NoneIngredient
            config.numSelectedIngredients -=1
            if config.numSelectedIngredients >0:
                config.cauldronColor = getCaulColor()
            else:
                config.cauldronColor = [90,90,90]

def clearPotionSlots():
    config.selectedIngredients[0] = config.NoneIngredient
    config.selectedIngredients[1] = config.NoneIngredient
    config.selectedIngredients[2] = config.NoneIngredient
    config.cauldronColor = [90,90,90]
    config.numSelectedIngredients = 0

def brewPotion(startTime):
    # TODO: add variation in potion brewing based on ingredients
    # Idea: bad potions can be made that take up space in inventory and have to be sold
    if len(config.PotionList)<65:
        potVal = int((config.selectedIngredients[0].getValue() * 0.9 + config.selectedIngredients[1].getValue() * 0.9 + config.selectedIngredients[2].getValue() * 0.9) * (uniform(1,1.3))  )
        effect = "None"
        color = getCaulColor()
        newPotion = Potion(str(random()), "Potion Name", "sprites/EmptyPotion.png", config.selectedIngredients[0].getID(), config.selectedIngredients[1].getID(), config.selectedIngredients[2].getID(), effect, color, potVal)
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


def sortListNext(l):
    first = l.pop(0)
    l.append(first)

    if l[0] == "Name":
        config.Ingredients.sort(key=lambda k: k.getName())
    elif l[0] == "Name R":
        config.Ingredients.sort(reverse=True, key=lambda k: k.getName())
    elif l[0] == "Category":
        config.Ingredients.sort(key=lambda k: k.getCategory())
    elif l[0] == "Category R":
        config.Ingredients.sort(reverse=True, key=lambda k: k.getCategory())
    elif l[0] == "Amount":
        config.Ingredients.sort(key=lambda k: k.getAmount())
    elif l[0] == "Amount R":
        config.Ingredients.sort(reverse=True, key=lambda k: k.getAmount())
    elif l[0] == "Value":
        config.Ingredients.sort(key=lambda k: k.getValue())
    elif l[0] == "Value R":
        config.Ingredients.sort(reverse=True, key=lambda k: k.getValue())
    elif l[0] == "Index":
        config.Ingredients.sort(key=lambda k: k.getID())
    elif l[0] == "Index R":
        config.Ingredients.sort(reverse=True, key=lambda k: k.getID())


#################### potionCreation Screen ####################
def potionCreation():
    pageNum = [0]
    ingSortTypes = [ "Name", "Name R","Amount R", "Amount","Category", "Category R", "Value", "Value R", "Index", "Index R"]
    start_time = [0]
    while True:
        # check events
        checkEvents()

        # draw on screen
        Back_Color = BLACK
        config.screen.fill(Back_Color)

        button_text(SCREEN_WIDTH - 140, 0, 140, 40, GOLD, 'Shop Front', font32, WHITE, config.screen,LC, mainMenu)

        #  display player gold
        draw_text("Gold: " + str(config.Player.getGold()), font32, GOLD, config.screen, 10, 5)

        #  display cauldron
        pygame.draw.rect(config.screen, config.cauldronColor, (int((SCREEN_WIDTH - 160) * 6 / 8 + 160*(3/20)), int((SCREEN_HEIGHT - 160) / 2 + 160*(3/20)), int(160*(14/20)), int(160*(4/20)),))
        draw_image((SCREEN_WIDTH - 160) * 6 / 8, (SCREEN_HEIGHT - 160) / 2, 160, 160, "sprites/EmptyCauldron.png", config.screen)

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


        if time_ns() - start_time[0] < 2000000000:#display most recent potion

            draw_text_center(config.PotionList[-1].getName(), font48, WHITE, config.screen, (SCREEN_WIDTH - 130) * 6 / 8 + 60, (SCREEN_HEIGHT + 320) / 2 + 40)

            creatWidth = int(120 * (12 / 20))
            creatHeight = int(120 * (7 / 20))

            pygame.draw.rect(config.screen, config.PotionList[-1].getColor(), (int((SCREEN_WIDTH - 130) * 6 / 8 +60 - creatWidth/2), int((SCREEN_HEIGHT + 170) / 2 + 55 - creatHeight/2) , creatWidth, creatHeight))
            draw_image_center((SCREEN_WIDTH - 130) * 6 / 8 + 60, (SCREEN_HEIGHT + 170) / 2 + 40, 120,120, "sprites/EmptyPotion.png", config.screen)
        elif len(config.PotionList)==65: #display full inventory
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
        button_text(SCREEN_WIDTH * 3 / 16 - 24, 0, 170, 40, GRAY, 'Sort Ingredients', font32, WHITE, config.screen, LC, sortListNext, ingSortTypes)


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
                               ingredient.imgLoc, config.screen, LC, removeSlot, ingredient)
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
        button_text(SCREEN_WIDTH - 140, 0, 140, 40, GOLD, 'Shop Front', font32, WHITE, config.screen, LC, mainMenu)

        # select options
        button_rect_text(SCREEN_WIDTH * 4 / 16 - 24, 0, 140, 40, Back_Color, RED, 'Deselect all', font32, WHITE, config.screen, LC, deselectAllPots)
        button_rect_text(SCREEN_WIDTH * 6 / 16 - 24, 0, 140, 40, Back_Color, GREEN, 'Select all', font32, WHITE, config.screen, LC, selectAllPots)

        #  Sell button
        button_rect_text_center(SCREEN_WIDTH/2, SCREEN_HEIGHT - 40, 60, 40, Back_Color, GREEN, 'Sell', font32, WHITE, config.screen,LC, sellSelectedPotions)
        button_rect_text_center(SCREEN_WIDTH - 80, SCREEN_HEIGHT - 40, 120, 40, Back_Color, GREEN, 'Sell All', font32, WHITE, config.screen, LC, sellAllPotions)

        # Display Player Gold
        draw_text("Gold: "+ str(config.Player.getGold()), font32, GOLD, config.screen, 10, 5)
        draw_text_center("Value: " + str(config.runningTotal), font32, GOLD, config.screen, SCREEN_WIDTH/2, SCREEN_HEIGHT - 80,)

        entNum = 0
        row_x = 0
        row_y = 0

        for pot in config.PotionList:

            if entNum % 13 == 0:
                row_x = 0
                row_y += 1
            if pot in config.selectedPotions.keys(): # click to remove from selected list
                pygame.draw.rect(config.screen, pot.getColor(), (int(100 * row_x + 80*(4/20)), int(100 * row_y + 80*(9/20)), int(80*(12/20)), int(80*(7/20))))
                button_img_img(100 * row_x, 100 * row_y, 80, 80, "sprites/GreenBorder.png", "sprites/RedBorder.png",
                                   "sprites/EmptyPotion.png", config.screen, LC, deselectPotion, pot)
            else: # click to add to selected list
                pygame.draw.rect(config.screen, pot.getColor(), (int(100 * row_x + 80*(4/20)), int(100 * row_y + 80*(9/20)), int(80*(12/20)),int(80*(7/20))))
                button_img_img(100 * row_x, 100 * row_y, 80, 80, "sprites/Nothing.png", "sprites/YellowBorder.png",
                               "sprites/EmptyPotion.png", config.screen, LC, selectPotion, (pot, row_x, row_y))

            draw_text_center(pot.name, font16, WHITE, config.screen, 100 * row_x + 40, 100 * row_y - 10)
            draw_text(str(pot.value), font16, GOLD, config.screen, 100 * row_x + 5, 100 * row_y + 65)
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
        #print(str(ingre) + " " + str(dropRates))
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
        #TODO: expand upon prereqs
        Back_Color = TEAL
        config.screen.fill(Back_Color)

        #  buttons to change screens
        button_text(SCREEN_WIDTH - 140, 0, 140, 40, GOLD, 'Shop Front', font32, BLACK, config.screen, LC, mainMenu)

        #  display player gold
        draw_text("Gold: " + str(config.Player.getGold()), font32, GOLD, config.screen, 10, 5)

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
                draw_text_center(str(req.get("Gold"))+" Gold", font20, GOLD,config.screen, SCREEN_WIDTH/2 + x_off, SCREEN_HEIGHT/2 + 40 + y_off )
            elif req.get("Potion"):
                pygame.draw.rect(config.screen, req.get("Potion").get("Color"), (int(SCREEN_WIDTH / 2 + x_off - 80 * (12 / 20)/2), int(SCREEN_HEIGHT / 2 + y_off - (80 * (1 / 20))), int(80 * (12 / 20)), int(80 * (7 / 20))))

                draw_image_center(SCREEN_WIDTH / 2 + x_off, SCREEN_HEIGHT / 2 + y_off, 80, 80, "sprites/EmptyPotion.png", config.screen)
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
                button_img_text(0, x * 40 + 100, 280, 40, "sprites/GreenBorder.png", "sprites/RedBorder.png", location.getName(), font32, textColor, config.screen, LC, deselectLocation, [location, prereqs])

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
################### Market Functions #######################

def setMode(mode):
    config.marketMode = mode

def selectMarketIng(ing):
    if config.marketMode == "buy":
        ing.addAmount(1)
        config.Player.subGold(int(ing.getValue() * config.Player.getBuyMarkup()))
        savePlayer(config.Player)
        saveIngredients(config.Ingredients)
    if config.marketMode == "sell":
        ing.subAmount(1)
        config.Player.addGold(int(ing.getValue() * config.Player.getSellMarkdown()))
        savePlayer(config.Player)
        saveIngredients(config.Ingredients)




#################### Buy/Sell Ingredients ####################
def ingredientShop():
    pageNum = [0]
    ingSortTypes = [ "Name", "Name R","Amount R", "Amount","Category", "Category R", "Value", "Value R","Index", "Index R"]
    start_time = [0]
    config.marketMode = ""

    while True:
        # check events
        checkEvents()

        # draw on screen
        Back_Color = BLACK
        config.screen.fill(Back_Color)

        #  buttons to change screens
        button_text(SCREEN_WIDTH - 140, 0, 140, 40, GOLD, 'Shop Front', font32, WHITE, config.screen,LC, mainMenu)



        #  display player gold
        draw_text("Gold: " + str(config.Player.getGold()), font32, GOLD, config.screen, 10, 5)

        if config.marketMode == "buy":
            button_text(SCREEN_WIDTH * 8 / 16 - 100, 10, 100, 40, RED, 'Buy', font48, GREEN, config.screen, LC, setMode, "")
            button_text(SCREEN_WIDTH * 8 / 16, 10, 100, 40, YELLOW, 'Sell', font48, WHITE, config.screen, LC, setMode, "sell")
        elif config.marketMode == "sell":
            button_text(SCREEN_WIDTH * 8 / 16 - 100, 10, 100, 40, GREEN, 'Buy', font48, WHITE, config.screen, LC, setMode, "buy")
            button_text(SCREEN_WIDTH * 8 / 16, 10, 100, 40, RED, 'Sell', font48, YELLOW, config.screen, LC, setMode, "")
        else:
            button_text(SCREEN_WIDTH * 8 / 16 - 100, 10, 100, 40, GREEN, 'Buy', font48, WHITE, config.screen, LC, setMode, "buy")
            button_text(SCREEN_WIDTH * 8 / 16, 10, 100, 40, YELLOW, 'Sell', font48, WHITE, config.screen, LC, setMode, "sell")

        entNum = 0
        posX = 0
        posY = 0
        displayIngredientNum = 0

        amountIngredients = 0
        for ingredient in config.Ingredients:  # get num of usable ingredients
            if config.marketMode == "sell":
                if ingredient.amount > 0:
                    amountIngredients += 1
            else:
                amountIngredients += 1
        numPages = int((amountIngredients - 1) / 48)  # get num of pages
        if pageNum[0] > numPages:  # only allow visit pages with something in it
            pageNum[0] = numPages
        if pageNum[0] > 0:
            button_img(100, 625, 160, 40, "sprites/WideArrowUP.png", "sprites/WideArrowUp.png", config.screen, LC, DecreaseVal, pageNum)
        if pageNum[0] < numPages:
            button_img(100, 675, 160, 40, "sprites/WideArrowDown.png", "sprites/WideArrowDown.png", config.screen, LC, IncreaseVal, pageNum)

        # Sorting ingredients
        button_text(SCREEN_WIDTH * 3 / 16 - 24, 5 , 170, 40, GRAY, 'Sort Ingredients', font32, WHITE, config.screen, LC, sortListNext, ingSortTypes)

        for ingredient in config.Ingredients:  # display ingredients
            if ingredient.amount < 1 and config.marketMode == "sell":
                continue
            displayIngredientNum += 1
            if displayIngredientNum < pageNum[0] * 48 + 1:
                continue
            if displayIngredientNum > (pageNum[0] + 1) * 48:
                continue
            if entNum % 12 == 0:
                posX = 0
                posY += 1
            button_img_img(100 * posX, 110 * posY - 20, 80, 80, "sprites/Nothing.png", "sprites/GreenBorder.png",
                               ingredient.imgLoc, config.screen, LC, selectMarketIng, ingredient)

            draw_text_center(ingredient.name, font16, WHITE, config.screen, 100 * posX + 40, 110 * posY + 70)
            draw_text(str(ingredient.amount), font16, WHITE, config.screen, 100 * posX + 5, 110 * posY + 45)
            if config.marketMode == "buy":
                draw_text_center(str(int(ingredient.value * config.Player.getBuyMarkup())) + " Gold", font16, GOLD, config.screen, 100 * posX + 40, 110 * posY + 85)
            elif config.marketMode == "sell":
                draw_text_center(str(int(ingredient.value * config.Player.getSellMarkdown())) + " Gold", font16, GOLD, config.screen, 100 * posX + 40, 110 * posY + 85)
            else:
                draw_text_center(str(ingredient.value) + " Gold", font16, GOLD, config.screen, 100 * posX + 40, 110 * posY + 85)

            posX += 1
            entNum += 1
        pygame.display.flip()  # update screen


######################################################

#################### Basic Screen ####################
def modifyIngredients():
    while True:
        # check events
        checkEvents()
        # draw on screen
        Back_Color = BLACK
        config.screen.fill(Back_Color)

        button_text(SCREEN_WIDTH - 140, 0, 140, 40, GOLD, 'Shop Front', font32, WHITE, config.screen, LC, mainMenu)

        pygame.display.flip()  # update screen

######################################################

def selectIndexIng(ing):
    config.selectedIndexIngredient = ing

def deselectIndexIng():
    config.selectedIndexIngredient = None

#################### Basic Screen ####################
def ingredientIndex():
    pageNum = [0]
    ingSortTypes = [ "Name", "Name R","Amount R", "Amount","Category", "Category R", "Value", "Value R", "Index", "Index R"]
    start_time = [0]
    while True:
        # check events
        checkEvents()
        # draw on screen
        Back_Color = BLACK
        config.screen.fill(Back_Color)

        button_text(SCREEN_WIDTH - 140, 0, 140, 40, GOLD, 'Shop Front', font32, WHITE, config.screen, LC, mainMenu)

        #display selected ingredient info
        indIng = config.selectedIndexIngredient
        if indIng != None:
            draw_image_center(SCREEN_WIDTH-480, 220 , 240, 240, indIng.getImgLoc(), config.screen)
            draw_text_center(indIng.getName(), font72, WHITE, config.screen, SCREEN_WIDTH-480, 40)

            draw_text_center("Active Color", font32, WHITE, config.screen, SCREEN_WIDTH - 180, 120)
            pygame.draw.rect(config.screen, indIng.getColor(), (SCREEN_WIDTH - 220, 160, 80,80))

            draw_text_center("Value: " + str(indIng.getValue()), font48, WHITE, config.screen, SCREEN_WIDTH - 480, SCREEN_HEIGHT/2)
            if indIng.getEffect1() != "None":
                draw_text("Effect 1: " + str(indIng.getEffect1()), font, WHITE, config.screen, SCREEN_WIDTH/2, SCREEN_HEIGHT - 260)
            if indIng.getEffect2() != "None":
                draw_text("Effect 2: " + str(indIng.getEffect2()), font, WHITE, config.screen, SCREEN_WIDTH/2, SCREEN_HEIGHT - 220)
            if indIng.getEffect3() != "None":
                draw_text("Effect 3: " + str(indIng.getEffect3()), font, WHITE, config.screen, SCREEN_WIDTH/2, SCREEN_HEIGHT - 180)

            draw_text("Categories: " + str(indIng.getCategory()), font32, WHITE, config.screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)

        entNum = 0
        posX = 0
        posY = 0
        displayIngredientNum = 0
        amountIngredients = 0

        for ingredient in config.Ingredients: # get num of usable ingredients
            #if ingredient.amount > 0:
                amountIngredients +=1
        numPages = int((amountIngredients-1)/24) #get num of pages
        if pageNum[0] > numPages: #only allow visit pages with something in it
            pageNum[0] = numPages
        if pageNum[0] > 0:
            button_img(100, 40, 160, 40, "sprites/WideArrowUP.png", "sprites/WideArrowUp.png",config.screen, LC, DecreaseVal, pageNum)
        if pageNum[0] < numPages:
            button_img(100, 675, 160, 40, "sprites/WideArrowDown.png", "sprites/WideArrowDown.png", config.screen, LC, IncreaseVal, pageNum)


        #Sorting ingredients
        button_text(100, 5, 170, 40, GRAY, 'Sort Ingredients', font32, WHITE, config.screen, LC, sortListNext, ingSortTypes)

        # display ingredients
        for ingredient in config.Ingredients:
            #if ingredient.amount < 1:
                #continue
            displayIngredientNum +=1
            if displayIngredientNum < pageNum[0] * 24 +1:
                continue
            if displayIngredientNum > (pageNum[0] + 1) * 24 :
                continue
            if entNum % 4 == 0:
                posX = 0
                posY += 1
            if ingredient == config.selectedIndexIngredient:
                button_img_img(100 * posX, 100 * posY - 20, 80, 80, "sprites/GreenBorder.png", "sprites/RedBorder.png",
                               ingredient.imgLoc, config.screen, LC, deselectIndexIng)
            else:
                button_img_img(100 * posX, 100 * posY - 20, 80, 80, "sprites/Nothing.png", "sprites/GreenBorder.png",
                           ingredient.imgLoc, config.screen, LC, selectIndexIng, ingredient)
            draw_text_center(ingredient.name, font16, WHITE, config.screen, 100 * posX + 40, 100 * posY + 70)
            #draw_text(str(ingredient.amount), font16, WHITE, config.screen, 100 * posX + 5, 100 * posY + 45)
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

config.NoneIngredient = Ingredient("NoneIngredient", "None", "sprites/Nothing.png",["None"], BLACK, 0, 0, "None", "None", "None" )
config.selectedIngredients = [config.NoneIngredient, config.NoneIngredient, config.NoneIngredient]

mainMenu()  # start mainMenu Screen
exit()

######################################################

#################### Basic Screen ####################
def Basic():
    while True:
        # check events
        checkEvents()
        # draw on screen
        Back_Color = WHITE
        config.screen.fill(Back_Color)

        button_text(SCREEN_WIDTH - 140, 0, 140, 40, GOLD, 'Shop Front', font32, WHITE, config.screen, LC, mainMenu)

        pygame.display.flip()  # update screen