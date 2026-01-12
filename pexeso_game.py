import pygame
import random
import time

pygame.init()

#game variables and costants
width = 800
height = 600

white = (255, 255, 255)
gray = (128, 128, 128)

tasty_green = (79, 106, 42)
correct_green = (140, 210, 119)
dark_green = (28,45,26)
green = (61, 82, 32)

yellow = (247, 200, 21)
dark_yellow = (156, 74, 26)

redish = (82, 65, 38)
blue = (119, 143, 210)

fps = 60
timer = pygame.time.Clock()

current_time = time.time()

rows = 4
cols = 5
options_list = []
spaces = []
used = []

new_board = True

first_guess = False
second_guess = False
first_guess_num = 0
second_guess_num = 0
score = 0
best_score = 0
matches = 0

start_time = None
elapsed_time = 0.0

game_over = False


#create screen
screen = pygame.display.set_mode([width, height])

pygame.display.set_caption("pepxo Game") #name of the window
title_font = pygame.font.Font('Game/Fonts/Aller_Rg.ttf', 50)
restart_font = pygame.font.Font('Game/Fonts/Aller_Rg.ttf', 40)
small_font = pygame.font.Font('Game/Fonts/Aller_Rg.ttf', 20)

def draw_backgrounds():
    top_menu = pygame.draw.rect(screen, tasty_green, [0, 0, width, 100]) 
    top_menu_border = pygame.draw.rect(screen, green, [0, 0, width, 100], 10)
    #draw.rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
    
    
    
    board_space = pygame.draw.rect(screen, redish, [0, 100, width, height - 200]) 
    bottom_menu = pygame.draw.rect(screen, tasty_green, [0, height - 100, width, 100])
    bottom_menu_border = pygame.draw.rect(screen, green, [0, height - 100, width, 100], 10)
    

    restart_button = pygame.draw.rect(screen, green, [290, height - 87, 200, 75], 0, 5)
    restart_button = pygame.draw.rect(screen, dark_green, [290, height - 87, 200, 75], 5, 5)
    restart_text = restart_font.render('Restart', True, white)
    screen.blit(restart_text, (325, 525))

    score_text = small_font.render(f'Score: {score}', True, white)
    screen.blit(score_text, (15, 520))

    best_text = small_font.render(f'Previous Best: {best_score}', True, white)
    screen.blit(best_text, (15, 550))

    side_menu = pygame.draw.rect(screen, tasty_green, [width - 225, 90, 225, 420])
    side_menu_border = pygame.draw.rect(screen, green, [width - 225, 90, 225, 420], 10)

    return restart_button

def draw_board():
    global rows
    global cols
    global correct

    board_list = []

    for i in range(cols):
        for j in range(rows):
            piece = pygame.draw.rect(screen, white, [i * 100 + 50, j * 98 + 108, 90, 90], 0, 4)
            piece = pygame.draw.rect(screen, dark_green, [i * 100 + 50, j * 98 + 108, 95, 95], 5, 4)
            board_list.append(piece)
            # piece_text = small_font.render(f'{spaces[i * rows + j]}', True, gray)
            # screen.blit(piece_text, (i * 100 + 56, j * 98 + 120))

#when correct:
    for r in range(rows):
        for c in range(cols):
            if correct[r][c] == 1:
                pygame.draw.rect(screen, correct_green, [c * 100 + 50, r * 98 + 108, 92, 92], 5, 4)
                piece_text = small_font.render(f'{spaces[c * rows + r]}', True, correct_green)
                screen.blit(piece_text, (c * 100 + 56, r * 98 + 120))


            
    return board_list

def create_correct_board(rows, cols):
    return [[0 for j in range(cols)] for i in range(rows)]

correct = create_correct_board(rows, cols)

def generate_board():
    global options_list
    global spaces
    global used
    
    for item in range(rows * cols // 2):
        options_list.append(item)
    
    for item in range (rows * cols):
        piece = options_list[random.randint(0, len(options_list)-1)]
        spaces.append(piece)
        if piece in used:
            used.remove(piece)
            options_list.remove(piece)
        else:
            used.append(piece)

def check_guess(first, second):
    global spaces
    global correct
    global score
    global matches

    if spaces[first] == spaces[second]:
        col1 = first // rows
        col2 = second // rows
        row1 = first - (first // rows * rows)
        row2 = second - (second // rows * rows)
        if correct[row1][col1] == 0 and correct[row2][col2] == 0:
            correct[row1][col1] = 1
            correct[row2][col2] = 1
            score += 1
            matches += 1
            
    else:
        score +=1



running = True

while running:
    timer.tick(fps)
    screen.fill(white)

    if new_board == True:
        generate_board()
        new_board = False

    restart = draw_backgrounds()
    board = draw_board()

    if first_guess and second_guess:
        check_guess(first_guess_num, second_guess_num)
        pygame.time.delay(1000)
        first_guess = False
        second_guess = False

    for event in pygame.event.get(): #getting out of the loop
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(board)):
                button = board[i]
                if not game_over:
                    if button.collidepoint(event.pos) and not first_guess:
                        first_guess = True
                        first_guess_num = i
                        
                    if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                        second_guess = True
                        second_guess_num = i
                        
            if restart.collidepoint(event.pos):
                options_list = []
                used = []
                spaces = []
                new_board = True
                score = 0
                matches = 0
                first_guess = False
                second_guess = False
                correct = create_correct_board(rows, cols)
                game_over = False
                current_time = time.time()

    if matches == rows * cols // 2:
        #
        game_over = True
        winner = pygame.draw.rect(screen, yellow, [10, height - 350, width - 20, 100], 0, 5)
        winner_border = pygame.draw.rect(screen, dark_yellow, [10, height - 350, width - 20, 100], 5, 5)
        winner_text = title_font.render(f'You Won In {score} moves!', True, white)
        screen.blit(winner_text, (width - winner_text.get_height() - 580, height - 330))
        if best_score > score or best_score == 0:
            best_score = score


    if first_guess:
        piece_text = small_font.render(f'{spaces[first_guess_num]}', True, blue)
        #piece = pygame.draw.rect(screen, white, [i * 100 + 50, j * 98 + 108, 90, 90], 0, 4)
        #screen.blit(piece_text, (i * 100 + 56, j * 98 + 120))
        location = (first_guess_num // rows * 100 + 56, (first_guess_num - (first_guess_num // rows * rows)) * 98 + 120)
        screen.blit(piece_text, (location))
    if second_guess:
        piece_text = small_font.render(f'{spaces[second_guess_num]}', True, blue)
        location = (second_guess_num // rows * 100 + 56, (second_guess_num - (second_guess_num // rows * rows)) * 98 + 120)
        screen.blit(piece_text, (location))
    
    #timer
    if game_over == False:
        timer_porfavor = time.time() - current_time
        minutes = int(timer_porfavor // 60)
        seconds = int(timer_porfavor % 60)
        time_string = "{:02d}:{:02d}".format(minutes, seconds)
        time_string_text = small_font.render(time_string, True, (255, 255, 255))
        screen.blit(time_string_text, (width - 90 - time_string_text.get_width(), height - 300 - time_string_text.get_height() // 2))

    pygame.display.flip()



pygame.quit()