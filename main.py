import pygame

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_SIZE = (300, 300)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the window title
pygame.display.set_caption("Tic-Tac-Toe")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the font
font = pygame.font.Font(None, 36)

# Set up the game board
board = [['', '', ''], ['', '', ''], ['', '', '']]
player = 'X'

# Define the functions
def draw_board():
    screen.fill(WHITE)
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, BLACK, (i*100, j*100, 100, 100), 2)
            text = font.render(board[j][i], True, BLACK)
            text_rect = text.get_rect(center=(i*100+50, j*100+50))
            screen.blit(text, text_rect)
            

def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        elif board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    elif board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

def switch_player():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            i = x // 100
            j = y // 100
            if board[j][i] == '':
                board[j][i] = player
                if check_win():
                    winner = font.render(player + " wins!", True, BLACK)
                    winner_rect = winner.get_rect(center=(150, 230))
                    screen.blit(winner, winner_rect)
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    board = [['', '', ''], ['', '', ''], ['', '', '']]
                else:
                    switch_player()

    # Fill the background
    screen.fill(WHITE)

    # Draw the game board
    draw_board()

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
