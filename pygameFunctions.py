import pygame
import config
from pygame.locals import *
from constants import *

mouseRelease = 0

def draw_text(text, fon, color, surface, x, y):
    textobj = pygame.font.SysFont(None, fon).render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def draw_text_center(text, fon, color, surface, x, y):
    textobj = pygame.font.SysFont(None, fon).render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x,y)
    surface.blit(textobj, textrect)

def draw_image(x, y, width, height, imagePNG, surface, color = None):

    if color != None:
        img = pygame.image.load(imagePNG)
        colImg = pygame.Surface(img.get_size()).convert_alpha()
        colImg.fill([255,255,255])
        img.blit(colImg, (x,y), special_flags = pygame.BLEND_RGBA_MULT)
    else:
        img = pygame.transform.scale(pygame.image.load(imagePNG).convert_alpha(), (width, height))
        img.set_colorkey(BLACK, RLEACCEL)
        surface.blit(img, (x,y))

def draw_image_center(x, y, width, height, imagePNG, surface):
    img = pygame.transform.scale(pygame.image.load(imagePNG).convert_alpha(), (width, height))
    img.set_colorkey(BLACK, RLEACCEL)
    surface.blit(img, (x-width/2,y-height/2))

def button(Mbutton, action=None, param = None):
        #MInfo Format: ((X,Y,Z),(Boolean)) X,Y,Z = mouse click info, Boolean is MUP (MouseUP) info to prevent hold clicks
        click = pygame.mouse.get_pressed()
        if config.MUP is None or config.MUP:
            if Mbutton[0] == 1:
                if click[0] == Mbutton[0] and action != None and param == None:
                    if config.MUP is not None:
                        config.MUP = False
                    return action()
                elif click[0] == Mbutton[0] and action != None and param != None:
                    if config.MUP is not None:
                        config.MUP = False
                    return action(param)
            if Mbutton[1] == 1:
                if click[1] == Mbutton[1] and action != None and param == None :
                    if config.MUP is not None:
                        config.MUP = False
                    return action()
                elif click[1] == Mbutton[1] and action != None and param != None:
                    if config.MUP is not None:
                        config.MUP = False
                    return action(param)
            if Mbutton[2] == 1:
                if click[2] == Mbutton[2] and action != None and param == None:
                    if config.MUP is not None:
                        config.MUP = False
                    return action()
                elif click[2] == Mbutton[2] and action != None and param != None:
                    if config.MUP is not None:
                        config.MUP = False
                    return action(param)


def button_rect(x,y,width,height,surface, activeColor, inactiveColor, Mbutton, action=None, param = None):
    mouse = pygame.mouse.get_pos()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(surface, activeColor, (x, y, width, height))
        button(Mbutton, action, param)
    else:
        pygame.draw.rect(surface, inactiveColor, (x, y, width, height))

def button_rect_center(x,y,width,height,surface, activeColor, inactiveColor, Mbutton, action=None, param = None):
    mouse = pygame.mouse.get_pos()
    if x + width / 2 > mouse[0] > x - width / 2 and y + height / 2 > mouse[1] > y - height / 2:
        pygame.draw.rect(surface, activeColor, (x - width / 2, y - height / 2, width, height))
        button(Mbutton, action, param)
    else:
        pygame.draw.rect(surface, inactiveColor, (x - width / 2, y - height / 2, width, height))




def button_rect_text(x, y, width, height, inactiveColor, activeColor, text, font, color, surface, Mbutton, action=None, param = None):

    button_rect(x,y,width,height,surface,activeColor,inactiveColor,Mbutton,action, param)
    draw_text_center(text, font, color, surface, x+width/2, y+height/2)

def button_rect_text_center(x, y, width, height, inactiveColor, activeColor, text, font, color, surface, Mbutton, action=None, param = None):

    button_rect_center(x, y, width, height, surface, activeColor, inactiveColor, Mbutton, action, param)
    draw_text_center(text, font, color, surface, x, y)



def button_text(x, y, width, height, activeColor, text, font, color, surface, Mbutton, action=None, param = None):

    mouse = pygame.mouse.get_pos()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        draw_text(text, font, activeColor, surface, x, y)
        button(Mbutton, action, param)
    else:
        draw_text(text, font, color, surface, x, y)

def button_text_center(x, y, width, height, activeColor, text, font, color, surface, Mbutton, action=None, param = None):

    mouse = pygame.mouse.get_pos()

    if x + width / 2 > mouse[0] > x - width / 2 and y + height / 2 > mouse[1] > y - height / 2:
        draw_text_center(text, font, activeColor, surface, x, y)
        button(Mbutton, action, param)
    else:
        draw_text_center(text, font, color, surface, x, y)



def button_img(x, y, width, height, inactiveImage, activeImage, surface, Mbutton, action=None, param = None):
    mouse = pygame.mouse.get_pos()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        draw_image(x, y, width, height, activeImage, surface)
        #surface.blit(actImg, (x, y))
        button(Mbutton, action, param)
    else:
        draw_image(x, y, width, height, inactiveImage, surface)
        #surface.blit(inactImg, (x, y))

def button_img_center(x, y, width, height, inactiveImage, activeImage, surface, Mbutton, action=None, param = None):
    mouse = pygame.mouse.get_pos()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        draw_image_center(x, y, width, height, activeImage, surface)
        button(Mbutton, action, param)
    else:
        draw_image_center(x, y, width, height, inactiveImage, surface)

def button_img_img(x, y, width, height, inactiveImage, activeImage, displayImage, surface, Mbutton, action=None, param = None):
    mouse = pygame.mouse.get_pos()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        draw_image(x, y, width, height, activeImage, surface)
        button(Mbutton, action, param)
    else:
        draw_image(x, y, width, height, inactiveImage, surface)

    draw_image(x, y, width, height, displayImage, surface)

def button_img_text(x, y, width, height, inactiveImage, activeImage, text, font, color, surface, Mbutton, action=None, param = None):
    mouse = pygame.mouse.get_pos()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        draw_image(x, y, width, height, activeImage, surface)
        button(Mbutton, action, param)
    else:
        draw_image(x, y, width, height, inactiveImage, surface)

    draw_text_center(text, font, color, surface, x+width/2, y+height/2)

def hoverover_text(x,y,width,height,backgroundColor,surface,text,font,color, xDrawOffset=None, yDrawOffset = None, side = None, setWidth = None ):
    mouse = pygame.mouse.get_pos()
    if xDrawOffset == None:
        xDrawOffset = 0
    if yDrawOffset == None:
        yDrawOffset = 0

    txtlen = len(text)
    drawWidth = txtlen * 9
    if setWidth != None:
        drawWidth = setWidth
    drawHeight = 20

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        xMouse = mouse[0]
        yMouse = mouse[1]
        if side == "Left":
            pygame.draw.rect(surface, backgroundColor, (xMouse -drawWidth + xDrawOffset, yMouse + yDrawOffset, drawWidth, drawHeight))
            draw_text_center(text,font,color,surface,xMouse-drawWidth/2 + xDrawOffset,yMouse+drawHeight/2 + yDrawOffset)
        else:
            pygame.draw.rect(surface, backgroundColor, (xMouse + xDrawOffset, yMouse + yDrawOffset, drawWidth, drawHeight))
            draw_text_center(text, font, color, surface, xMouse + drawWidth / 2 + xDrawOffset, yMouse + drawHeight / 2 + yDrawOffset)



