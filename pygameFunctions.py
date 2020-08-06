import pygame
from pygame.locals import *
from constants import *

mouseRelease = 0

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def draw_text_center(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x-textobj.get_width()/2, y-textobj.get_height()/2)
    surface.blit(textobj, textrect)


def button_rect_text(x, y, width, height, inactiveColor, activeColor, text, font, color, surface, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(surface, activeColor, (x,y,width,height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(surface, inactiveColor, (x, y, width, height))

    textsurf = font.render(text,1,color)
    textrect = textsurf.get_rect()
    textrect.center = (x+width/2, (y+height/2))
    surface.blit(textsurf, textrect)

def button_rect_text_center(x, y, width, height, inactiveColor, activeColor, text, font, color, surface, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width/2 > mouse[0] > x-width/2 and y+height/2 > mouse[1] > y-width/2:
        pygame.draw.rect(surface, activeColor, (x-width/2,y-height/2,width,height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(surface, inactiveColor, (x-width/2, y-height/2, width, height))

    textsurf = font.render(text,1,color)
    textrect = textsurf.get_rect()
    textrect.center = (x, y)
    surface.blit(textsurf, textrect)

def draw_image(x, y, width, height, imagePNG, surface):
    img = pygame.transform.scale(pygame.image.load(imagePNG).convert_alpha(), (width, height))
    img.set_colorkey(BLACK, RLEACCEL)
    surface.blit(img, (x,y))

def draw_image_center(x, y, width, height, imagePNG, surface):
    img = pygame.transform.scale(pygame.image.load(imagePNG).convert_alpha(), (width, height))
    img.set_colorkey(BLACK, RLEACCEL)
    surface.blit(img, (x-width/2,y-height/2))


def button_img(x, y, width, height, inactiveImage, activeImage, surface, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_rel()
    actImg = pygame.transform.scale(pygame.image.load(activeImage).convert_alpha(), (width, height))
    inactImg = pygame.transform.scale(pygame.image.load(inactiveImage).convert_alpha(), (width, height))

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        surface.blit(actImg, (x, y))
        if click[0] == 1 and action != None:
            action()
    else:
        surface.blit(inactImg, (x, y))

def button_img_center(x, y, width, height, inactiveImage, activeImage, surface, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    actImg = pygame.transform.scale(pygame.image.load(activeImage).convert_alpha(), (width, height))
    inactImg = pygame.transform.scale(pygame.image.load(inactiveImage).convert_alpha(), (width, height))

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        surface.blit(actImg, (x-width/2, y-height/2))
        if click[0] == 1 and action != None:
            action()
    else:
        surface.blit(inactImg, (x-width/2, y-height/2))

def button_img_img(x, y, width, height, inactiveImage, activeImage, displayImage, surface, action=None, param = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    actImg = pygame.transform.scale(pygame.image.load(activeImage).convert_alpha(), (width, height))
    inactImg = pygame.transform.scale(pygame.image.load(inactiveImage).convert_alpha(), (width, height))

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        surface.blit(actImg, (x, y))
        if click[0] == 1 and action != None and param == None:
            action()
        elif click[0] == 1 and action != None and param != None:
            action(param)


    else:
        surface.blit(inactImg, (x, y))

    disImg = pygame.transform.scale(pygame.image.load(displayImage).convert_alpha(), (width, height))
    surface.blit(disImg, (x, y))
