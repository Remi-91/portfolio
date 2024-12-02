# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:29:40 2023

@author: remil
"""

import pygame
pygame.font.init() 



class Cell:
    SIZE = 30 # 30
    BORDER_RADIUS = 3
    
    def __init__(self, hasBomb:bool):
        # Couleurs pour cellule cachée
        self.hideBackgroundColor = (50,50,50)
        # Couleurs pour cellule découverte
        self.shownBackgroundColor = (70,70,70)
        
        # Couleur pour cellule avec flag
        self.flagBackgroundColor = (238,185,0)
        
        # Couleur d'une cellule découverte avec bombe
        self.bombBackgroundColor = (0,0,0)
        
        # Infos relatives au jeu
        self.hasBomb = hasBomb
        self.hasFlag = False
        self.hide = True
        
    def show(self):
        if not(self.hasFlag):
            self.hide = False
        else:
            print("La cellule ne peut pas être découverte : elle a un drapeau.")
            
    def placeOrRemoveFlag(self):
        if not(self.hide):
            print("Impossible de mettre un drapeau sur une cellule découverte")
        else:
            self.hasFlag = not(self.hasFlag)
            
    
    def display(self, x, y, nbVoisins, surface):
        xCoord = x
        yCoord = y
        
        # Couleur de fond + eventuel texte
        my_font = pygame.font.SysFont('Comic Sans MS', 2*Cell.SIZE//3)
        if(self.hasFlag):
            pygame.draw.rect(surface, self.flagBackgroundColor, (xCoord, yCoord, Cell.SIZE, Cell.SIZE), border_radius=Cell.BORDER_RADIUS)
        elif(self.hide):
            pygame.draw.rect(surface, self.hideBackgroundColor, (xCoord, yCoord, Cell.SIZE, Cell.SIZE), border_radius=Cell.BORDER_RADIUS)
        elif(not(self.hide) and not(self.hasBomb)):
            pygame.draw.rect(surface, self.shownBackgroundColor, (xCoord, yCoord, Cell.SIZE, Cell.SIZE), border_radius=Cell.BORDER_RADIUS)
            if nbVoisins != 0:
                textColor = None
                if nbVoisins == 1:
                    textColor = (75,127,105)
                elif nbVoisins == 2:
                    textColor = (47,138,139)
                elif nbVoisins == 3:
                    textColor = (28,103,126)
                elif nbVoisins == 4:
                    textColor = (247,201,7)
                elif nbVoisins == 5:
                    textColor = (234,145,3)
                elif nbVoisins == 6:
                    textColor = (248,162,161)
                elif nbVoisins == 7:
                    textColor = (244,7,66)
                elif nbVoisins == 8:
                    textColor = (167,108,174)
                text_surface = my_font.render(str(nbVoisins), False, textColor)
                surface.blit(text_surface, (xCoord + ((Cell.SIZE - text_surface.get_width())//2), (yCoord + (Cell.SIZE - text_surface.get_height())//2)))
        elif(not(self.hide) and self.hasBomb):
            pygame.draw.rect(surface, self.bombBackgroundColor, (xCoord, yCoord, Cell.SIZE, Cell.SIZE), border_radius=Cell.BORDER_RADIUS)
            
             
             