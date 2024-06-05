#import libraries
import pygame
from sys import exit
from time import sleep

# Initialise pygame
pygame.init()

# Constants
window_width, window_height,button_size = 300,300,100
black = (0, 0, 0)
margin_color = (255, 255, 255)
current_player = 1
current_turn = 1
board_values = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
def draw():
    pygame.display.set_caption("Draw")
    sleep(3)
    pygame.quit()
    exit()    
    
def end_game():
    pygame.display.set_caption(f"P{current_player} WIN")
    sleep(5)
    pygame.quit()
    exit()   
    
      
def check_for_win():
    player_won = False
  
    # Create column lists
    column_list,column0,column1,column2 = [],[],[],[] 
    
    for row in range(0, 3):
        column0.append(board_values[row][0])
        column1.append(board_values[row][1])
        column2.append(board_values[row][2])
        
    # Merge all 3 lists into a 2d list 
    column_list.append(column0)
    column_list.append(column1)
    column_list.append(column2)
   
    
    # Initialise the diagonals
    diagonal0,diagonal1 = [],[]
    
    # Assign values to the diagonals
    for i in range(0, 3):
        diagonal0.append(board_values[i][i])
    
    for k in range(0, 3):
        diagonal1.append(board_values[k][2 - k])
        
    # CHECKING FOR A WIN
    
    # Check for row, column, and diagonal wins
    if [current_player, current_player, current_player] in board_values:
        player_won = True

    for col_values in column_list:
        if [current_player, current_player, current_player] == col_values:
            player_won = True

    if diagonal0 == [current_player, current_player, current_player]:
        player_won = True

    if diagonal1 == [current_player, current_player, current_player]:
        player_won = True

    # Return the result               
    return player_won

# Create the window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Button Grid - P1")

# Button class
class Button:
    def __init__(self, row, col, size):
        # Initialize button properties
        self.row ,self.col= row,col
        self.rect = pygame.Rect(col * size, row * size, size, size)
        self.is_hovered,self.clicked = False,False

    def draw(self):
        # Draw the button with a small border
        pygame.draw.rect(window, black, self.rect)
        pygame.draw.rect(window, margin_color, self.rect, 2)

        # Draw X or O in the center of the button
        if self.clicked:
            font = pygame.font.SysFont(None, 60)
            text = font.render("X" if board_values[self.row][self.col] == 1 else "O", True, (255, 255, 255))
            text_rect = text.get_rect(center=self.rect.center)
            window.blit(text, text_rect)

# Create the buttons in a 3x3 grid
buttons = [[Button(row, col, button_size) for col in range(3)] for row in range(3)]

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            draw()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button     
                for row in buttons:
                    for button in row:
                        if button.rect.collidepoint(event.pos) and not button.clicked:
                            button.clicked = True
                            board_values[button.row][button.col] = current_player

                            # Draw X or O before checking for a win
                            for row in buttons:
                                for b in row:
                                    b.draw()
                            pygame.display.flip()

                            if check_for_win():
                                end_game()

                            # Switch players
                            current_player = 1 if current_player == 2 else 2

                            if current_player == 1:
                                pygame.display.set_caption("Button Grid - P1")
                            else:
                                pygame.display.set_caption("Button Grid - P2")
                                
                                

                            current_turn += 1
                            
                            if current_turn == 10:
                                draw()
        #Cheat, Press R to win                      
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                end_game()              

    for row in buttons:
        for button in row:
            button.is_hovered = button.rect.collidepoint(pygame.mouse.get_pos())

    pygame.display.flip()
