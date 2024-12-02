# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:48:32 2023

@author: remil
"""


import Cell
import random
import pygame


class Board:
    BOARD_WIDTH = 20 # Nombre de cellules en largeur - 20
    BOARD_HEIGHT = 20 # Nombre de cellules en hauteur - 20
    BOMB_NUMBER = 70 # Nombre de bombes à placer - 70
    
    MARGIN_CELL = 3
    
    BACKGROUND_COLOR = "#4f4f4f"
    
    def __init__(self):
        # Création d'une variable locale pour compter le nombre de bombes restantes
        self.bombs = Board.BOMB_NUMBER
        
        # Initialisation du plateau
        self.board = []
        for y in range(0, Board.BOARD_HEIGHT):
            line = []
            for x in range(0, Board.BOARD_WIDTH):
                cell = Cell.Cell(False)
                line.append(cell)
            self.board.append(line)
            
        # Ajout de bombes aléatoirement
        nbBombToPlace = Board.BOMB_NUMBER
        while nbBombToPlace != 0:
            x = random.randint(0, Board.BOARD_WIDTH - 1)
            y = random.randint(0, Board.BOARD_HEIGHT - 1)
            cell = self.board[y][x]
            if(not(cell.hasBomb)):
                cell.hasBomb = True
                nbBombToPlace -= 1
                
                
    # A n'appeler qu'une fois à l'initialisation
    def display(self, surface):
        surface.fill(Board.BACKGROUND_COLOR)
        
        # Affichage des cellules
        for y in range(0, Board.BOARD_HEIGHT):
            for x in range(0, Board.BOARD_WIDTH):
                Cellule = self.board[y][x]
                Cellule.display(x * (Board.MARGIN_CELL + Cell.Cell.SIZE), y * (Board.MARGIN_CELL + Cell.Cell.SIZE), 0, surface)
        

    
    
    
    # Donne le nombre de bombes au voisinage de la cellule de coordonnées (x,y)
    def getBombNumber(self, x, y):
        # Compter le nombre de bombes voisines
        bombs = 0
        for j in range(-1,2):
            for i in range(-1,2):
                if (x+i) >= 0 and (x+i) < Board.BOARD_WIDTH and (y+j) >= 0 and (y+j) < Board.BOARD_HEIGHT and (i!=0 or j!=0):
                    cellTmp = self.board[y+j][x+i]
                    if(cellTmp.hasBomb):
                        bombs+=1
        return bombs
    
    
    # Propage la découverte des cellules de façon récursive
    def propagateDiscover(self, x, y, surface):
        # Trouver la cellule courante
        cell = self.board[y][x]
        cell.show()
        
        bombs = self.getBombNumber(x, y)
        cell.display(x * (Board.MARGIN_CELL + Cell.Cell.SIZE), y * (Board.MARGIN_CELL + Cell.Cell.SIZE), bombs, surface)
        #cell.display(x, y, bombs, surface)
        
        
        # Propager récursivement au cellules voisines si la courante a 0 bombes (et pas déjà découverte)
        if bombs == 0:
            for j in range(-1,2):
                for i in range(-1,2):
                    if (x+i) >= 0 and (x+i) < Board.BOARD_WIDTH and (y+j) >= 0 and (y+j) < Board.BOARD_HEIGHT and (i!=0 or j!=0):
                        cellTmp = self.board[y+j][x+i]
                        if cellTmp.hide == True:
                            self.propagateDiscover(x+i, y+j, surface)
        
        
        