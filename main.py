import pygame
import sys

class TicTacToe:
    def __init__(self):
        image = pygame.image.load('Imgs/board.png')
        x = pygame.image.load('Imgs/x.png')
        o = pygame.image.load('Imgs/o.png')
        pygame.init()
        pygame.display.set_caption("Tic-Tac-Toe")
        width, height = 600, 600
        self.screen = pygame.display.set_mode((width, height))
        self.o = pygame.transform.scale(o, (100, 100))
        self.x = pygame.transform.scale(x, (100, 100))
        self.board_sprite = pygame.transform.scale(image, (600, 600))
        
        self.game_board = [[0,0,0],
                           [0,0,0],
                           [0,0,0]]
        self.winning_indices = []
        self.player_1_turn = True
        self.player_2_turn = False
        self.moves = 0
        self.winner = ""
        self.way_of_win = ""
        self.game_over = False

    def drawImages(self):
        self.screen.blit(self.board_sprite, (0,0))
        for i in range(3):
            for j in range(3):
                if self.game_board[i][j] == 'X':
                    self.screen.blit(self.x, ((i * 200) + 55, (j * 200) + 55))
                elif self.game_board[i][j] == 'O':
                    self.screen.blit(self.o, ((i * 200) + 55, (j * 200) + 55))

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
        elif pygame.mouse.get_pressed()[0] and self.player_2_turn and not self.game_over:
            position = pygame.Vector2(pygame.mouse.get_pos())//200
            if self.game_board[int(position[0])][int(position[1])] == 0 and not self.game_over:
                self.game_board[int(position[0])][int(position[1])] = 'O'
                self.player_2_turn = False
                self.player_1_turn = True
                self.moves += 1
                self.checkWinner()

    def checkWinner(self):
        x_or_o = 'X'
        for j in range(2):
            for i in range(3):
                if self.game_board[i][0] == x_or_o and self.game_board[i][1] == x_or_o and self.game_board[i][2] == x_or_o:
                    if x_or_o == 'X':
                        self.winner = "Player X"
                    else: 
                        self.winner = "Player O"
                    self.way_of_win = "column"
                    self.game_over = True
                    self.winning_indices = [[i,0], [i,1], [i,2]]
                elif self.game_board[0][i] == x_or_o and self.game_board[1][i] == x_or_o and self.game_board[2][i] == x_or_o:
                    if x_or_o == 'X':
                        self.winner = "Player X"
                    else: 
                        self.winner = "Player O"
                    self.way_of_win = "row"
                    self.game_over = True
                    self.winning_indices = [[0,i], [1,i], [2, i]]
            if self.game_board[0][0] == x_or_o and self.game_board[1][1] == x_or_o and self.game_board[2][2] == x_or_o:
                if x_or_o == 'X':
                    self.winner = "Player X"
                else: 
                    self.winner = "Player O"
                self.way_of_win = "diagnol"
                self.game_over = True
                self.winning_indices = [[0,0], [1,1], [2,2]]
            elif self.game_board[0][2] == x_or_o and self.game_board[1][1] == x_or_o and self.game_board[2][0] == x_or_o:
                if x_or_o == 'X':
                    self.winner = "Player X"
                else: 
                    self.winner = "Player O"
                self.way_of_win = "diagnol"
                self.game_over = True
                self.winning_indices = [[0,2], [1,1], [2,0]]
            x_or_o = 'O'

    def checkTie(self):
        if self.moves == 9 and self.way_of_win == "":
            self.game_over = True
            self.way_of_win = "tie"

    def setCaption(self):
        if not self.game_over and self.player_1_turn:
            pygame.display.set_caption("Player X turn")
        elif not self.game_over and self.player_2_turn:
            pygame.display.set_caption("Player O turn")
        elif self.game_over and self.way_of_win != "tie":
            pygame.display.set_caption(f"{self.winner} won by way of {self.way_of_win}")
        elif self.game_over and self.way_of_win == "tie":
            pygame.display.set_caption(f"It's a {self.way_of_win}")

    def drawWinnerLine(self):
        if self.game_over and self.way_of_win != "tie":
            if self.way_of_win == "column":
                startPoint = pygame.Vector2(self.winning_indices[0]) * 200
                endPoint = pygame.Vector2(self.winning_indices[-1]) * 200
                startPoint[0] += 100.0
                startPoint[1] += 50.0
                endPoint[0] += 100.0
                endPoint[1] += 150.0
                pygame.draw.line(self.screen, 'yellow', startPoint, endPoint, 20)
            elif self.way_of_win == "row":
                startPoint = pygame.Vector2(self.winning_indices[0]) * 200
                endPoint = pygame.Vector2(self.winning_indices[-1]) * 200
                startPoint[0] += 50.0
                startPoint[1] += 100.0
                endPoint[0] += 150.0
                endPoint[1] += 100.0
                pygame.draw.line(self.screen, 'green', startPoint, endPoint, 20)
            elif self.way_of_win == "diagnol":
                startPoint = pygame.Vector2(self.winning_indices[0]) * 250
                endPoint = pygame.Vector2(self.winning_indices[-1]) * 250
                startPoint[0] += 50.0
                startPoint[1] += 50.0
                endPoint[0] += 50.0
                endPoint[1] += 50.0
                pygame.draw.line(self.screen, 'orange', startPoint, endPoint, 20)

    def play(self):
        self.drawImages()
        self.setCaption()
        self.move()
        self.drawWinnerLine()


tic = TicTacToe()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tic.play()
    pygame.display.flip()