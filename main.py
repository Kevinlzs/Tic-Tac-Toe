import pygame
from pygame.locals import *

# pygame.init()
# width, height = 600, 600
# screen = pygame.display.set_mode((width, height))
# image = pygame.image.load('Imgs/board.png')


# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Game logic and rendering code goes here
#     image = pygame.transform.scale(image, (600, 600))
#     screen.blit(image, (0,0))
#     pygame.display.flip()

class TicTacToe:
    def __init__(self):
        # self.board_sprite = image
        self.game_board = [[0,0,0],
                           [0,0,0],
                           [0,0,0]]
        self.player_1_turn = True
        self.player_2_turn = False
        self.moves = 0
        self.winner = ""
        self.way_of_win = ""
        self.game_over = False

    def display(self):
        for i in range(len(self.game_board)):
            print(self.game_board[i])

    def move(self):
        if self.player_1_turn and not self.game_over:
            while(self.player_1_turn):
                self.display()
                row = int(input("Player 1, enter a row(rows start at 0): "))
                column = int(input("Player 1, enter a column(columns start at 0): "))
                if self.game_board[row][column] == 0:
                    self.game_board[row][column] = 'X'
                    self.player_1_turn = False
                    self.player_2_turn = True
                    self.moves += 1
                    self.checkWinner()
                    self.checkTie()
                else:
                    print("Not a valid choice, try again")
        if self.player_2_turn and not self.game_over:
            while(self.player_2_turn):
                self.display()
                row = int(input("Player 2, enter a row(rows start at 0): "))
                column = int(input("Player 2, enter a column(columns start at 0): "))
                if self.game_board[row][column] == 0:
                    self.game_board[row][column] = 'O'
                    self.player_2_turn = False
                    self.player_1_turn = True
                    self.moves += 1
                    self.checkWinner()
                else:
                    print("Not a valid choice, try again")

    def checkWinner(self):
        x_or_o = ''
        for j in range(2):
            if j == 0:
                x_or_o = 'X'
            else:
                x_or_o = 'O'
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

    def checkTie(self):
        if self.moves == 9:
            self.game_over = True
            self.way_of_win = "tie"

    def play(self):
        while True:
            if self.way_of_win != "tie" and self.game_over:
                print(f"{self.winner} won in the way of {self.way_of_win}")
                break
            elif self.way_of_win == "tie" and self.game_over:
                print(f"It's a {self.way_of_win}")
                break
            self.move()


game = TicTacToe()
game.play()