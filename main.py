import pygame
import sys
from pygame.locals import *


class TicTacToe:
    def __init__(self):
        image = pygame.image.load('Imgs/board.png')
        x = pygame.image.load('Imgs/x.png')
        o = pygame.image.load('Imgs/o.png')
        pygame.init()
        width, height = 600, 600
        self.o = pygame.transform.scale(o, (100, 100))
        self.x = pygame.transform.scale(x, (100, 100))
        self.screen = pygame.display.set_mode((width, height))

        self.board_sprite = pygame.transform.scale(image, (600, 600))
        # self.x = screen.blit)i
        self.game_board = [[0,0,0],
                           [0,0,0],
                           [0,0,0]]
        self.player_1_turn = True
        self.player_2_turn = False
        self.moves = 0
        self.winner = ""
        self.way_of_win = ""
        self.game_over = False

    def draw_images(self):
        self.screen.blit(self.board_sprite, (0,0))
        for i in range(3):
            for j in range(3):
                if self.game_board[i][j] == 'X':
                    self.screen.blit(self.x, ((i * 200) + 55, (j * 200) + 55))
                elif self.game_board[i][j] == 'O':
                    self.screen.blit(self.o, ((i * 200) + 55, (j * 200) + 55))



    # def display(self):
    #     for i in range(len(self.game_board)):
    #         print(self.game_board[i])

    def move(self):
        if pygame.mouse.get_pressed()[0] and self.player_1_turn and not self.game_over:
            position = pygame.Vector2(pygame.mouse.get_pos())//200
            if self.game_board[int(position[0])][int(position[1])] == 0 and not self.game_over:
                self.game_board[int(position[0])][int(position[1])] = 'X'
                self.player_1_turn = False
                self.player_2_turn = True
                self.moves += 1
                self.checkWinner()
                self.checkTie()
            # elif self.game_board[int(position[0])][int(position[1])] == 0 and not self.game_over:
            #     self.game_board[int(position[0])][int(position[1])] = 'O'
        elif pygame.mouse.get_pressed()[0] and self.player_2_turn and not self.game_over:
            position = pygame.Vector2(pygame.mouse.get_pos())//200
            # if self.game_board[int(position[0])][int(position[1])] == 0 and not self.game_over:
            #     self.game_board[int(position[0])][int(position[1])] = 'X'
            if self.game_board[int(position[0])][int(position[1])] == 0 and not self.game_over:
                self.game_board[int(position[0])][int(position[1])] = 'O'
                self.player_2_turn = False
                self.player_1_turn = True
                self.moves += 1
                self.checkWinner()
        # if self.player_1_turn and not self.game_over:
        #     row = int(input("Player 1, enter a row(rows start at 0): "))
        #     column = int(input("Player 1, enter a column(columns start at 0): "))
        #     if self.game_board[row][column] == 0:
        #         self.game_board[row][column] = 'X'
        #         self.player_1_turn = False
        #         self.player_2_turn = True
        #         self.moves += 1
        #         self.checkWinner()
        #         self.checkTie()
        #     else:
        #         print("Not a valid choice, try again")
        # if self.player_2_turn and not self.game_over:
        #     row = int(input("Player 2, enter a row(rows start at 0): "))
        #     column = int(input("Player 2, enter a column(columns start at 0): "))
        #     if self.game_board[row][column] == 0:
        #         self.game_board[row][column] = 'O'
        #         self.player_2_turn = False
        #         self.player_1_turn = True
        #         self.moves += 1
        #         self.checkWinner()
        #     else:
        #         print("Not a valid choice, try again")

    def checkWinner(self):
        x_or_o = 'X'
        for j in range(2):
            for i in range(3):
                if self.game_board[i][0] == x_or_o and self.game_board[i][1] == x_or_o and self.game_board[i][2] == x_or_o:
                    if x_or_o == 'X':
                        self.winner = "player1"
                    else: 
                        self.winner = "player2"
                    self.way_of_win = "row"
                    self.game_over = True
                elif self.game_board[0][i] == x_or_o and self.game_board[1][i] == x_or_o and self.game_board[2][i] == x_or_o:
                    if x_or_o == 'X':
                        self.winner = "player1"
                    else: 
                        self.winner = "player2"
                    self.way_of_win = "column"
                    self.game_over = True
            if self.game_board[0][0] == x_or_o and self.game_board[1][1] == x_or_o and self.game_board[2][2] == x_or_o:
                if x_or_o == 'X':
                    self.winner = "player1"
                else: 
                    self.winner = "player2"
                self.way_of_win = "diagnol"
                self.game_over = True
            elif self.game_board[0][2] == x_or_o and self.game_board[1][1] == x_or_o and self.game_board[2][0] == x_or_o:
                if x_or_o == 'X':
                    self.winner = "player1"
                else: 
                    self.winner = "player2"
                self.way_of_win = "diagnol"
                self.game_over = True
            x_or_o = 'O'

    def checkTie(self):
        if self.moves == 9:
            self.game_over = True
            self.way_of_win = "tie"

    def play(self):
        if self.way_of_win != "tie" and self.game_over:
            print(f"{self.winner} won in the way of {self.way_of_win}")
            exit()
        elif self.way_of_win == "tie" and self.game_over:
            print(f"It's a {self.way_of_win}")
            exit()
        self.draw_images()
        self.move()



tic = TicTacToe()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
            # print(pygame.Vector2(pygame.mouse.get_pos())//200)
    tic.play()
    pygame.display.flip()