# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:25:47 2023

@author: remil
"""




import Board
import Cell
import pygame
pygame.init()
import datetime
import random
from pygame import mixer
mixer.init()


def main():
    #random.seed(2) #­1
    # Variables globales
    board = Board.Board()
    
    # Création de la fenêtre graphique
    cellSize = Cell.Cell.SIZE
    boardWidth = Board.Board.BOARD_WIDTH
    boardHeight = Board.Board.BOARD_HEIGHT
    margin = Board.Board.MARGIN_CELL
    screen = pygame.display.set_mode((boardWidth * (cellSize + margin), boardHeight * (cellSize + margin)))
    pygame.display.set_caption("Démineur")
   
    # Initialisation de l'UI avec le plateau aux cellules toutes cachées
    board.display(screen)
    
    
    
    while True:    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                return
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Coordonnées de la souris
                mousePosition = pygame.mouse.get_pos()
                mouseX = mousePosition[0]
                mouseY = mousePosition[1]
                # Conversion en coordonnées du tableau de cellules
                X = mouseX // (Cell.Cell.SIZE + Board.Board.MARGIN_CELL)
                Y = mouseY // (Cell.Cell.SIZE + Board.Board.MARGIN_CELL)
                cell = board.board[Y][X]
                
                
                # Clique gauche -> révéler une cellule
                if event.button == 1:
                    board.propagateDiscover(X, Y, screen)
                    mixer.music.load("ShowSound.mp3")
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    
                # Clique droit -> Mettre/Enlever un flag
                if event.button == 3:
                    cell.placeOrRemoveFlag()
                    cell.display(X * (Cell.Cell.SIZE + Board.Board.MARGIN_CELL), Y * (Cell.Cell.SIZE + Board.Board.MARGIN_CELL), board.getBombNumber(X, Y), screen)
                    mixer.music.load("FlagSound.mp3")
                    mixer.music.set_volume(0.2)
                    mixer.music.play()
                    
        
        pygame.display.flip()



main()