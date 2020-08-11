from helpers import *

def addToEmptySlot(ingredient):

    if selectedIngredients[0] == ingredient or selectedIngredients[1] == ingredient or selectedIngredients[2] == ingredient:
        return
    elif selectedIngredients[0] == NoneIngredient:
        selectedIngredients[0] = ingredient
        ingredient.amount -= 1
    elif selectedIngredients[1] == NoneIngredient:
        selectedIngredients[1] = ingredient
        ingredient.amount -=1
    elif selectedIngredients[2] == NoneIngredient:
        selectedIngredients[2] = ingredient
        ingredient.amount -=1

def removeSlot(Ingredient):
    for i in range(len(selectedIngredients)):
        if selectedIngredients[i] == Ingredient:
            Ingredient.amount +=1
            selectedIngredients[i] = NoneIngredient


def brewPotion(startTime):
    # TODO: add variation in potion brewing based on ingredients
    if(len(PotionList)<65):
        newPotion = Potion(str(random()), "Potion Name", "sprites/potions/"+randomPotionColor(), selectedIngredients[0].getID(), selectedIngredients[1].getID(), selectedIngredients[2].getID(), int(random() * 100) )
        PotionList.append(newPotion)
        savePotions(PotionList)
        saveIngredients(Ingredients)
        clearPotionSlots()
        startTime[0] = time_ns()

def brewMultiPotion(info):
    n = info[1]
    ig1 = selectedIngredients[0]
    ig2 = selectedIngredients[1]
    ig3 = selectedIngredients[2]
    for m in range(n):
        print(m)
        addToEmptySlot(ig1)
        addToEmptySlot(ig2)
        addToEmptySlot(ig3)
        brewPotion(info[0])

def clearPotionSlots():
    selectedIngredients[0] = NoneIngredient
    selectedIngredients[1] = NoneIngredient
    selectedIngredients[2] = NoneIngredient

def sortListNext(l):
    first = l.pop(0)
    l.append(first)


def selectPotion(data):
    click = pygame.mouse.get_pressed()

    potionID = data[0]
    posX = data[1]
    posY = data[2]
    selectedPotions[potionID] = (posX, posY)

def deselectPotion(data):

    selectedPotions.pop(data)

def sellSelectedPotions():
    for i in selectedPotions:
        Player.addGold(i.getValue())
        PotionList.remove(i)
    selectedPotions.clear()
    savePotions(PotionList)
    savePlayer(Player)

def sellAllPotions():
    for i in PotionList:
        Player.addGold(i.getValue())
    PotionList.clear()
    selectedPotions.clear()
    savePotions(PotionList)
    savePlayer(Player)


def gatherIngredient():
    if Player.getGold() > 100:
        for i in Ingredients:
            i.addAmount(int(randrange(1,10)))
        Player.subGold(100)


def checkEvents(MUP):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            MUP[0] = True

#################### MainMenu Screen ####################
def mainMenu():
    MUP = [True] # only one that starts true
    while True:
        # check events
        checkEvents(MUP)

        # draw on screen
        Back_Color = WHITE
        screen.fill(Back_Color)


        draw_text_center('Alchemy Shop', font48, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        button_rect_text_center(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5, 80, 40, Back_Color, GREEN, 'Start', font32, BLACK, screen,(LC, MUP), potionCreation)
        button_rect_text_center(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 100, 40, Back_Color, BLUE, 'Options', font32, BLACK,screen,(LC, MUP), None)
        button_rect_text_center(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.67, 60, 40, Back_Color, RED, 'Quit', font32, BLACK, screen,(LC, MUP), exit)

        pygame.display.flip() # update screen
    pygame.quit()


#################### potionCreation Screen ####################
def potionCreation():
    MUP = [False]
    pageNum = [0]
    ingSortTypes = [ "Category", "Category R","Amount R", "Amount", "Name", "Name R"]
    start_time = [0]
    while True:
        # check events
        checkEvents(MUP)

        #TODO: buy and sell ingredients

        # draw on screen
        Back_Color = BLACK
        screen.fill(Back_Color)

        #  buttons to change screens
        button_rect_text(SCREEN_WIDTH - 140, 0, 120, 40, Back_Color, GREEN, 'Main Menu', font32, WHITE, screen,(LC, MUP), mainMenu)
        button_rect_text((SCREEN_WIDTH) * 11/16 - 24, 0, 140, 40, Back_Color, PURPLE, 'Potion List', font32, WHITE, screen,(LC, MUP), potionInventory)

        #  button to gather ingredients
        button_rect_text((SCREEN_WIDTH) * 6 / 16 - 24, 0, 280, 40, Back_Color, MAROON, 'Gather Ingredients (100G)', font32, WHITE, screen,(LC, MUP), gatherIngredient)

        #  display player gold
        draw_text("Gold: " + str(Player.getGold()), font32, YELLOW, screen, 10, 5)

        #  display cauldron
        draw_image((SCREEN_WIDTH - 160) * 6 / 8, (SCREEN_HEIGHT - 160) / 2, 160, 160, "sprites/Cauldron.png", screen)

        # display ingredient slots
        button_img_img((SCREEN_WIDTH - 306) * 6 / 8, (SCREEN_HEIGHT - 220) / 2, 80, 80,
                       "sprites/BlueBorder.png", "sprites/YellowBorder.png", selectedIngredients[0].imgLoc, screen, (LC, MUP),removeSlot, selectedIngredients[0])
        button_img_img((SCREEN_WIDTH - 106) * 6 / 8, (SCREEN_HEIGHT - 340) / 2, 80, 80,
                       "sprites/BlueBorder.png", "sprites/YellowBorder.png", selectedIngredients[1].imgLoc, screen, (LC, MUP),removeSlot, selectedIngredients[1])
        button_img_img((SCREEN_WIDTH + 94) * 6 / 8, (SCREEN_HEIGHT - 220) / 2, 80, 80,
                       "sprites/BlueBorder.png", "sprites/YellowBorder.png", selectedIngredients[2].imgLoc, screen, (LC, MUP),removeSlot, selectedIngredients[2])
        #display brew button
        if selectedIngredients[0] != NoneIngredient and selectedIngredients[1] != NoneIngredient and selectedIngredients[2] != NoneIngredient and len(PotionList)<65:
            button_rect_text((SCREEN_WIDTH - 130)  * 6 / 8, (SCREEN_HEIGHT + 220) / 2, 120, 80, Back_Color, GREEN, "Brew!", font48, WHITE, screen,(LC,MUP), brewPotion, start_time)
            if len(PotionList) < 61 and selectedIngredients[0].getAmount() > 4 and selectedIngredients[1].getAmount() > 4 and selectedIngredients[2].getAmount() > 4:
                button_rect_text((SCREEN_WIDTH - 130) * 6 / 8 + 00, (SCREEN_HEIGHT + 380) / 2, 30, 20, Back_Color, GREEN, " 5x", font20, WHITE, screen, (LC, MUP), brewMultiPotion, (start_time,5))
            if len(PotionList) < 56 and selectedIngredients[0].getAmount() > 9 and selectedIngredients[1].getAmount() > 9 and selectedIngredients[2].getAmount() > 9:
                button_rect_text((SCREEN_WIDTH - 130) * 6 / 8 + 30, (SCREEN_HEIGHT + 380) / 2, 30, 20, Back_Color, GREEN, "10x", font20, WHITE, screen, (LC, MUP), brewMultiPotion, (start_time,10))
            if len(PotionList) < 46 and selectedIngredients[0].getAmount() > 19 and selectedIngredients[1].getAmount() > 19 and selectedIngredients[2].getAmount() > 19:
                button_rect_text((SCREEN_WIDTH - 130) * 6 / 8 + 60, (SCREEN_HEIGHT + 380) / 2, 30, 20, Back_Color, GREEN, "20x", font20, WHITE, screen, (LC, MUP), brewMultiPotion, (start_time,20))
            if len(PotionList) < 64 :
                smallIng = min(selectedIngredients[0].getAmount(),selectedIngredients[1].getAmount(),selectedIngredients[2].getAmount())
                button_rect_text((SCREEN_WIDTH - 130) * 6 / 8 + 90, (SCREEN_HEIGHT + 380) / 2, 30, 20, Back_Color, GREEN, "Max", font20, WHITE, screen, (LC, MUP), brewMultiPotion, (start_time,smallIng+1))


        if time_ns() - start_time[0] < 2000000000: #display full inventory
            draw_text_center(PotionList[-1].getName(), font48, WHITE, screen, (SCREEN_WIDTH - 130) * 6 / 8 + 60, (SCREEN_HEIGHT + 320) / 2 + 40)
            draw_image_center((SCREEN_WIDTH - 130) * 6 / 8 + 60, (SCREEN_HEIGHT + 170) / 2 + 40, 120,120, PotionList[-1].getImgLoc(), screen)
        elif len(PotionList)==65: #display most recent potion
            draw_text_center("Inventory Full", font48, WHITE, screen, (SCREEN_WIDTH - 130) * 6 / 8 + 60, (SCREEN_HEIGHT + 220) / 2 + 40)


        entNum = 0
        posX = 0
        posY = 0
        displayIngreNum = 0
        numIngre = len(Ingredients)
        amountIngre = 0
        for ingre in Ingredients: # get num of usable ingredients
            if ingre.amount > 0:
                amountIngre +=1
        numPages = int((amountIngre-1)/24) #get num of pages
        if pageNum[0] > numPages: #only allow visit pages with something in it
            pageNum[0] = numPages

        #print("numIngre:"+ str(amountIngre) + "/" + str(numIngre) + " numPages:" +str(pageNum[0]) + "/"+ str(numPages))

        if pageNum[0] > 0:
            button_img(100, 40, 160, 40, "sprites/WideArrowUP.png", "sprites/WideArrowUp.png",screen, (LC, MUP), DecreaseVal, pageNum)
        if pageNum[0] < numPages:
            button_img(100, 675, 160, 40, "sprites/WideArrowDown.png", "sprites/WideArrowDown.png", screen, (LC, MUP), IncreaseVal, pageNum)


        #Sorting ingredients
        button_rect_text((SCREEN_WIDTH) * 3 / 16 - 24, 0, 170, 40, Back_Color, GRAY, 'Sort Ingredients', font32, WHITE, screen, (LC, MUP), sortListNext, ingSortTypes )

        if ingSortTypes[0] == "Name":
            Ingredients.sort(key=lambda k: k.getName())
        elif ingSortTypes[0] == "Name R":
            Ingredients.sort(reverse = True, key=lambda k: k.getName())
        elif ingSortTypes[0] == "Category":
            Ingredients.sort(key=lambda k: k.getCategory())
        elif ingSortTypes[0] == "Category R":
            Ingredients.sort(reverse = True, key=lambda k: k.getCategory())
        elif ingSortTypes[0] == "Amount":
            Ingredients.sort(key=lambda k: k.getAmount())
        elif ingSortTypes[0] == "Amount R":
            Ingredients.sort(reverse = True, key=lambda k: k.getAmount())
        elif ingSortTypes[0] == "Index": #Not implemented
            Ingredients.sort(key=lambda k: k.getCategory())
        elif ingSortTypes[0] == "Index R": #Not implemented
            Ingredients.sort(reverse=True, key=lambda k: k.getCategory())


        for Ingre in Ingredients: # display ingredients
            if Ingre.amount < 1:
                continue
            displayIngreNum +=1
            if displayIngreNum < pageNum[0] * 24 +1:
                continue
            if displayIngreNum > pageNum[0] * 24 + 24:
                continue
            if entNum % 4 == 0:
                posX = 0
                posY += 1
            if Ingre in selectedIngredients:
                button_img_img(100 * posX, 100 * posY - 20, 80, 80, "sprites/GreenBorder.png", "sprites/RedBorder.png",
                               Ingre.imgLoc, screen, (RC, None), removeSlot, Ingre)
            else:
                button_img_img(100 * posX, 100 * posY - 20, 80, 80, "sprites/Nothing.png", "sprites/GreenBorder.png",
                           Ingre.imgLoc, screen,(LC, None), addToEmptySlot, Ingre)
            draw_text_center(Ingre.name, font16, WHITE, screen, 100 * posX + 40, 100 * posY + 70)
            draw_text(str(Ingre.amount), font16, WHITE, screen, 100 * posX + 5, 100 * posY + 45)
            hoverover_text(100 * posX, 100 * posY - 20, 80, 80, SILVER, screen, Ingre.effect_1, font20, BLACK,10,0)
            hoverover_text(100 * posX, 100 * posY - 20, 80, 80, SILVER, screen, Ingre.effect_2, font20, BLACK,10,20)
            hoverover_text(100 * posX, 100 * posY - 20, 80, 80, SILVER, screen, Ingre.effect_3, font20, BLACK,10,40)
            posX += 1
            entNum += 1

        pygame.display.flip() # update screen

    pygame.quit()


#################### potion Inventory Screen ####################
def potionInventory():
    selection = 0
    MUP = [False]
    while True:
        # check events
        checkEvents(MUP)
        #TODO: Select all/select none options
        #TODO: sell all potions
        #TODO: running total for selling selected potions
        #TODO: look at potion stats/info when hovering over with mouse

        # draw on screen
        Back_Color = BLACK
        screen.fill(Back_Color)

        #  buttons to change screens
        button_rect_text(SCREEN_WIDTH - 140, 0, 120, 40, Back_Color, GREEN, 'Main Menu', font32, WHITE, screen, (LC, MUP), mainMenu)
        button_rect_text((SCREEN_WIDTH) * 11/16 - 24, 0, 170, 40, Back_Color, PURPLE, 'Potion Creation', font32, WHITE, screen,(LC, MUP), potionCreation)

        #  Sell button
        button_rect_text_center(SCREEN_WIDTH/2, SCREEN_HEIGHT - 40, 60, 40, Back_Color, GREEN, 'Sell', font32, WHITE, screen,(LC, MUP), sellSelectedPotions)
        button_rect_text_center(SCREEN_WIDTH - 80, SCREEN_HEIGHT - 40, 120, 40, Back_Color, GREEN, 'Sell All', font32, WHITE, screen, (LC, MUP), sellAllPotions)

        # Display Player Gold
        draw_text("Gold: "+ str(Player.getGold()), font32, YELLOW, screen, 10, 5)

        entNum = 0
        row_x = 0
        row_y = 0

        click = pygame.mouse.get_pressed()
        for pot in PotionList:

            if entNum % 13 == 0:
                row_x = 0
                row_y += 1
            if pot in selectedPotions.keys(): # click to remove from selected list
                button_img_img(100 * row_x, 100 * row_y, 80, 80, "sprites/GreenBorder.png", "sprites/RedBorder.png",
                                   pot.imgLoc, screen, (RC, None), deselectPotion, pot)
            else: # click to add to selected list
                button_img_img(100 * row_x, 100 * row_y, 80, 80, "sprites/Nothing.png", "sprites/YellowBorder.png",
                               pot.imgLoc, screen, (LC, None), selectPotion, (pot, row_x, row_y))

            draw_text_center(pot.name, font16, WHITE, screen, 100 * row_x + 40, 100 * row_y - 10)
            draw_text(str(pot.value), font16, WHITE, screen, 100 * row_x + 5, 100 * row_y + 65)
            row_x += 1
            entNum += 1

        pygame.display.flip()  # update screen
    pygame.quit()


#################### Basic Screen ####################
def ingredientGather():
    MUP = [False]
    while True:
        # check events
        checkEvents(MUP)
        #TODO: expand upon function to gather ingredients
        #TODO: add specific areas to gather specific ingredients
        #TODO: show screen of all gathered Ingredients
        #TODO: create areas that require specific types of potions
        screen.fill(WHITE)

        pygame.display.flip()  # update screen
    pygame.quit()



#################### game init ####################
pygame.init()
pygame.display.set_caption("Alchemy Shop")
icon = pygame.image.load('sprites/CauldronWhiteBk.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

Ingredients = InitIngredients()  # initalize ingredients
PotionList = InitPotionList()  # initalize potions
Player = InitPlayer()  # initalize player


savePlayer(Player)

selectedPotions = {}
NoneIngredient = Ingredient("NoneIngredient", "None", "sprites/Nothing.png",["None"], 0, "None", "None", "None" )
selectedIngredients = [NoneIngredient, NoneIngredient, NoneIngredient]

font = pygame.font.SysFont(None, 40)
font16 = pygame.font.SysFont(None, 16)
font20 = pygame.font.SysFont(None, 20)
font24 = pygame.font.SysFont(None, 24)
font32 = pygame.font.SysFont(None, 32)
font48 = pygame.font.SysFont(None, 48)

mainMenu()  # start main menu Screen
exit()


#################### Basic Screen ####################
def Basic():
    MUP = [False]
    while True:
        # check events
        checkEvents(MUP)

        # draw on screen
        Back_Color = WHITE
        screen.fill(Back_Color)

        pygame.display.flip()  # update screen
    pygame.quit()