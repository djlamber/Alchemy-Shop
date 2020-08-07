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

def brewPotion():
    # TODO: add variation in potion brewing based on ingredients
    if(len(PotionList)<65):
        newPotion = Potion(str(random()), "Pot Name", "sprites/potions/"+randomPotionColor(), selectedIngredients[0].getID(), selectedIngredients[1].getID(), selectedIngredients[2].getID(), int(random() * 100) )
        PotionList.append(newPotion)
        savePotions(PotionList)
        saveIngredients(Ingredients)
        clearPotionSlots()
    else:
        print("Inventory full")

def clearPotionSlots():
    selectedIngredients[0] = NoneIngredient
    selectedIngredients[1] = NoneIngredient
    selectedIngredients[2] = NoneIngredient

def removeSlot(Ingredient):
    for i in range(len(selectedIngredients)):
        if selectedIngredients[i] == Ingredient:
            selectedIngredients[i] = NoneIngredient


def removeSlot1():
    selectedIngredients[0].amount +=1
    selectedIngredients[0] = NoneIngredient

def removeSlot2():
    selectedIngredients[1].amount +=1
    selectedIngredients[1] = NoneIngredient

def removeSlot3():
    selectedIngredients[2].amount +=1
    selectedIngredients[2] = NoneIngredient

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

def gatherIngredient():
    if Player.getGold() > 100:
        for i in Ingredients:
            i.addAmount(int(randrange(1,10)))
        Player.subGold(100)

#################### MainMenu Screen ####################
def mainMenu():
    running = True
    while running:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                running = False

        # draw on screen
        Back_Color = WHITE
        screen.fill(Back_Color)

        draw_text_center('Alchemy Shop', font48, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        button_rect_text_center(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5, 80, 40, Back_Color, GREEN, 'Start', font32, BLACK, screen,LC, potionCreation)
        button_rect_text_center(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 100, 40, Back_Color, BLUE, 'Options', font32, BLACK,screen,LC, None)
        button_rect_text_center(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.67, 60, 40, Back_Color, RED, 'Quit', font32, BLACK, screen,LC, exit)

        pygame.display.flip() # update screen
    pygame.quit()


#################### potionCreation Screen ####################
def potionCreation():
    running = True
    while running:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                running = False

        #TODO: create a way to inspect ingredients when hovering over them with mouse
        #TODO: buy and sell ingredients
        #TODO: create multiple potions at once (5x 10x 20x)
        #TODO: show created potion
        #TODO: Say when potion inventory is full
        #TODO: Ingredient menu overflow buttons/pages

        # draw on screen
        Back_Color = BLACK
        screen.fill(Back_Color)

        #  buttons to change screens
        button_rect_text(SCREEN_WIDTH - 140, 0, 120, 40, Back_Color, GREEN, 'Main Menu', font32, WHITE, screen,LC, mainMenu)
        button_rect_text((SCREEN_WIDTH) * 11/16 - 24, 0, 140, 40, Back_Color, PURPLE, 'Potion List', font32, WHITE, screen,LC, potionInventory)

        #  button to gather ingredients
        button_rect_text((SCREEN_WIDTH) * 6 / 16 - 24, 0, 280, 40, Back_Color, MAROON, 'Gather Ingredients (100G)', font32, WHITE, screen,LC, gatherIngredient)

        #  display player gold
        draw_text("Gold: " + str(Player.getGold()), font32, YELLOW, screen, 10, 5)

        #  display cauldron
        draw_image((SCREEN_WIDTH - 160) * 6 / 8, (SCREEN_HEIGHT - 160) / 2, 160, 160, "sprites/Cauldron.png", screen)

        # display ingredient slots
        button_img_img((SCREEN_WIDTH - 306) * 6 / 8, (SCREEN_HEIGHT - 220) / 2, 80, 80,
                       "sprites/BlueBorder.png", "sprites/YellowBorder.png", selectedIngredients[0].imgLoc, screen, LC,removeSlot1, None)
        button_img_img((SCREEN_WIDTH - 106) * 6 / 8, (SCREEN_HEIGHT - 340) / 2, 80, 80,
                       "sprites/BlueBorder.png", "sprites/YellowBorder.png", selectedIngredients[1].imgLoc, screen, LC,removeSlot2, None)
        button_img_img((SCREEN_WIDTH + 94) * 6 / 8, (SCREEN_HEIGHT - 220) / 2, 80, 80,
                       "sprites/BlueBorder.png", "sprites/YellowBorder.png", selectedIngredients[2].imgLoc, screen, LC,removeSlot3, None)
        if selectedIngredients[0] != NoneIngredient and selectedIngredients[1] != NoneIngredient and selectedIngredients[2] != NoneIngredient:
            button_rect_text((SCREEN_WIDTH - 130)  * 6 / 8, (SCREEN_HEIGHT + 220) / 2, 120, 80, Back_Color, GREEN, "Brew!", font48, WHITE, screen,LC, brewPotion)

        entNum = 0
        posX = 0
        posY = 0
        for Ingre in Ingredients:
            if Ingre.amount < 1:
                continue
            if entNum % 4 == 0:
                posX = 0
                posY += 1
            if Ingre in selectedIngredients:
                button_img_img(100 * posX, 100 * posY, 80, 80, "sprites/GreenBorder.png", "sprites/RedBorder.png",
                               Ingre.imgLoc, screen, RC, removeSlot, Ingre)
            else:
                button_img_img(100 * posX, 100 * posY, 80, 80, "sprites/Nothing.png", "sprites/GreenBorder.png",
                           Ingre.imgLoc, screen,LC, addToEmptySlot, Ingre)
            draw_text_center(Ingre.name, font16, WHITE, screen, 100 * posX + 40, 100 * posY - 10)
            draw_text(str(Ingre.amount), font16, WHITE, screen, 100 * posX + 5, 100 * posY + 65)
            posX += 1
            entNum += 1


        pygame.display.flip() # update screen

    pygame.quit()


#################### potion Inventory Screen ####################
def potionInventory():
    running = True
    selection = 0
    while running:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                running = False
        #TODO: allow deselect potions
        #TODO: Select all/select none options
        #TODO: sell all potions
        #TODO: running total for selling selected potions
        #TODO: look at potion stats/info when hovering over with mouse

        # draw on screen
        Back_Color = BLACK
        screen.fill(Back_Color)

        #  buttons to change screens
        button_rect_text(SCREEN_WIDTH - 140, 0, 120, 40, Back_Color, GREEN, 'Main Menu', font32, WHITE, screen,LC, mainMenu)
        button_rect_text((SCREEN_WIDTH) * 9 / 16 - 24, 0, 170, 40, Back_Color, PURPLE, 'Potion Creation', font32, WHITE, screen,LC, potionCreation)

        #  Sell button
        button_rect_text_center(SCREEN_WIDTH/2, SCREEN_HEIGHT - 40, 60, 40, Back_Color, GREEN, 'Sell', font32, WHITE, screen,LC, sellSelectedPotions)

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
            if pot in selectedPotions.keys():
                button_img_img(100 * row_x, 100 * row_y, 80, 80, "sprites/GreenBorder.png", "sprites/RedBorder.png",
                                   pot.imgLoc, screen, RC, deselectPotion, pot)
            else:
                button_img_img(100 * row_x, 100 * row_y, 80, 80, "sprites/Nothing.png", "sprites/YellowBorder.png",
                               pot.imgLoc, screen, LC, selectPotion, (pot, row_x, row_y))

            draw_text_center(pot.name, font16, WHITE, screen, 100 * row_x + 40, 100 * row_y - 10)
            draw_text(str(pot.value), font16, WHITE, screen, 100 * row_x + 5, 100 * row_y + 65)
            row_x += 1
            entNum += 1

        pygame.display.flip()  # update screen
    pygame.quit()


#################### Basic Screen ####################
def ingredientGather():

    running = True
    while running:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                running = False
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
NoneIngredient = Ingredient("NoneIngredient", "None", "sprites/Nothing.png", 0, "None", "None", "None" )
selectedIngredients = [NoneIngredient, NoneIngredient, NoneIngredient]

font = pygame.font.SysFont(None, 40)
font16 = pygame.font.SysFont(None, 16)
font24 = pygame.font.SysFont(None, 24)
font32 = pygame.font.SysFont(None, 32)
font48 = pygame.font.SysFont(None, 48)

mainMenu()  # start main menu Screen
exit()


#################### Basic Screen ####################
def Basic():
    running = True
    while running:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                running = False

        # draw on screen
        Back_Color = WHITE
        screen.fill(Back_Color)

        pygame.display.flip()  # update screen
    pygame.quit()