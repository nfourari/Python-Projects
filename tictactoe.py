
import pygame
import math
import random

def check_win(board):

    for i in range(3):
        if (board[i][0] == 1 and board[i][1] == 1 and board[i][2] == 1):
            return -1
        if (board[i][0] == 2 and board[i][1] == 2 and board[i][2] == 2):
            return -2
        if (board[0][i] == 1 and board[1][i] == 1 and board[2][i] == 1):
            return -1
        if (board[0][i] == 2 and board[1][i] == 2 and board[2][i] == 2):
            return -2

    if (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1):
            return -1
    if (board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2):
            return -2
    if (board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1):
            return -1
    if (board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 2):
            return -2
        
    return 0

def main():
    pygame.init()

    screen = pygame.display.set_mode( [600, 600]  )

    board = [ [0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0] ]

    running = True

    turn = 0
    game_state = 9
    # game_state is going to be the amount of moves left in the game.
    # OR if the game is over.
    # If it is 0 it is a tie
    # If it is a -1 then player 1 wins
    # If it is a -2 then player 2 wins.

    while (running == True):

        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    turn = 0
                    board = [[0,0,0], [0,0,0],[0,0,0]]
                    game_state = 9
            if event.type == pygame.MOUSEBUTTONUP:
                cords = pygame.mouse.get_pos()
                # changes where we click to index values. 
                row = cords[1] // 200
                col = cords[0] // 200

                if board[row][col] == 0:
                    if (turn == 0):
                        board[row][col] = 1
                        turn = 1
                    else:
                        board[row][col] = 2
                        turn = 0
                    ans = check_win(board)
                    if (ans < 0):
                        game_state = ans
                    else:
                        if (game_state != 0):
                            game_state -= 1
                    
                        
            
                


        # update our values.
       

        # Draw the screen
        screen.fill( (0, 0, 0) )



        for row in range( len(board) ):
            for col in range( len(board[row]) ):
                if (board[row][col] == 1):
                    pygame.draw.rect(screen, (141, 247, 84), (col* 200 + 20, row*200 + 20, 160, 160))
                    pygame.draw.rect(screen, (0, 0, 0), (col*200 + 30, row*200 + 30, 140, 140))
                if (board[row][col] == 2):
                    pygame.draw.circle(screen, (247, 92, 84), (col*200+100, row*200+100), 80)
                    pygame.draw.circle(screen, (0, 0, 0), (col*200+100, row*200+100), 70)

        # Screen, color (Red, green, blue), rectangle (x, y, width, height)
        pygame.draw.rect(screen, (84, 147, 247), (0, 200, 600, 10))
        pygame.draw.rect(screen, (84, 147, 247), (0, 400, 600, 10))
        pygame.draw.rect(screen, (84, 147, 247), (200, 0, 10, 600))
        pygame.draw.rect(screen, (84, 147, 247), (400, 0, 10, 600))

        if (game_state == -1):
            pygame.draw.rect(screen, (141, 247, 84), (50, 50, 500, 500))
            pygame.draw.rect(screen, (0, 0, 0), (70, 70, 460, 460))
        if (game_state == -2):
            pygame.draw.circle(screen, (247, 92, 84), (300, 300), 250)
            pygame.draw.circle(screen, (0, 0, 0), (300, 300), 230)
        if (game_state==0):
            pygame.draw.rect(screen, (141, 247, 84), (50, 50, 500, 500))
            pygame.draw.rect(screen, (0, 0, 0), (70, 70, 460, 460))
            pygame.draw.circle(screen, (247, 92, 84), (300, 300), 225)
            pygame.draw.circle(screen, (0, 0, 0), (300, 300), 215)
        pygame.display.flip()
        
    pygame.quit()

main()
