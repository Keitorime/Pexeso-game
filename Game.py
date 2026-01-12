import pygame
import sys
import random
import time

#А це початок...
pygame.init()
screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spexiso")
icon = pygame.image.load('Game/Images/Character/head.png')
pygame.display.set_icon(icon)
image = pygame.image.load('Game/Images/Background2.jpg')
font = pygame.font.Font('Game/Fonts/Roboto-Black.ttf', 40)

text_rect = pygame.Rect(screen_height, 35, 110, 33)
text_surface = pygame.font.Font('Game/Fonts/Roboto-Black.ttf', 30).render("Spexiso", True, 'white')
text_rect.center = text_rect.center

Start = pygame.Rect(50, 380, 150, 33)
Start_text = pygame.font.SysFont('Game/Fonts/Roboto-Black.ttf', 30).render("Start", True, 'white')
Start_rect = Start_text.get_rect(center=Start.center)

About_Game = pygame.Rect(50, 420, 150, 33)
About_Game_text = pygame.font.SysFont('Game/Fonts/Roboto-Black.ttf', 30).render("About", True, 'white')
About_Game_rect = About_Game_text.get_rect(center=About_Game.center)

Exit = pygame.Rect(50, 460, 150, 33)
Exit_text = pygame.font.SysFont('Game/Fonts/Roboto-Black.ttf', 30).render("Exit", True, 'white')
Exit_rect = Exit_text.get_rect(center=Exit.center)

game_state = "main_menu"
running = True
moving_left = False
moving_right = False

# Звуки

# forest_sound = pygame.mixer.Sound('Game/Sounds/forest_night.mp3')
# forest_sound.play()

# Рух персонажа
count = 0
clock = pygame.time.Clock()
p_speed = 7
p_x = 300
p_y = 500

last_direction = "right"
is_jumping = False
jump_count = 10

flag = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:


            # Clear the event queue
            pygame.event.clear(pygame.KEYDOWN)
        if event.type == pygame.QUIT:
            running = False

        if game_state == "main_menu":
            if event.type == pygame.MOUSEBUTTONDOWN and Start_rect.collidepoint(event.pos):
                game_state = "game"
            elif event.type == pygame.MOUSEBUTTONDOWN and About_Game_rect.collidepoint(event.pos):
                game_state = "about"
            elif event.type == pygame.MOUSEBUTTONDOWN and Exit_rect.collidepoint(event.pos):
                running = False

        elif game_state == "game":
            if event.type == pygame.MOUSEBUTTONDOWN and Start_Back.collidepoint(event.pos):
                game_state = "main_menu"

        elif game_state == "about":
            if event.type == pygame.MOUSEBUTTONDOWN and About_Back_rect.collidepoint(event.pos):
                game_state = "main_menu"

    if game_state == "main_menu":
        screen.blit(image, (0, 0))
        pygame.draw.rect(screen, 'Black', text_rect)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, 'Black', Start)
        screen.blit(Start_text, Start_rect)
        pygame.draw.rect(screen, 'Black', About_Game)
        screen.blit(About_Game_text, About_Game_rect)
        pygame.draw.rect(screen, 'Black', Exit)
        screen.blit(Exit_text, Exit_rect)

    elif game_state == "game":
        # Тут гра
        # Звуки


        fon = pygame.image.load('Game/Images/Play_Back1.png')
        screen.blit(fon, (0, 0))


        Start_Back = pygame.Rect(-15, 30, 150, 33)
        Start_Back_text = pygame.font.SysFont('Game/Fonts/Roboto-Black.ttf', 30).render("Back", True, 'black')
        Start_Back_rect = Start_Back_text.get_rect(center=Start_Back.center)

        pygame.draw.rect(screen, 'Black', Start_Back)

        right = [
            pygame.image.load('Game/Images/Character/right1.png'),
            pygame.image.load('Game/Images/Character/right2.png'),
            pygame.image.load('Game/Images/Character/right3.png'),
            ]
        left = [
            pygame.image.load('Game/Images/Character/left1.png'),
            pygame.image.load('Game/Images/Character/left2.png'),
            pygame.image.load('Game/Images/Character/left3.png'),
            ]


        screen.blit(right[count], (p_x, p_y))

        keys = pygame.key.get_pressed()

        screen.blit(fon, (0, 0))  # Відображення заднього фону
        screen.blit(Start_Back_text, Start_Back_rect)
        if keys[pygame.K_LEFT]:
            moving_left = True
            moving_right = False
            last_direction = "left"
        elif keys[pygame.K_RIGHT]:
            moving_left = False
            moving_right = True
            last_direction = "right"
        else:
            moving_left = False
            moving_right = False

        if not is_jumping:
            if keys[pygame.K_SPACE]:
                is_jumping = True
                jump_count = 10
        else:
            if jump_count >= -10:
                p_y -= (jump_count * abs(jump_count)) * 0.2
                jump_count -= 1
                if last_direction == "left":
                    screen.blit(left[count], (p_x, p_y))
                else:
                    screen.blit(right[count], (p_x, p_y))
            else:
                is_jumping = False

        if moving_left:
            screen.blit(left[count], (p_x, p_y))
        elif moving_right:
            screen.blit(right[count], (p_x, p_y))
        else:
            if last_direction == "left":
                screen.blit(left[0], (p_x, p_y))
            else:
                screen.blit(right[0], (p_x, p_y))

        if keys[pygame.K_LEFT] and p_x > 1:
            p_x -= p_speed
        elif keys[pygame.K_RIGHT] and p_x < 550:
            p_x += p_speed

            # Анимация ходьбы
        if (moving_left or moving_right) and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            count += 1
            if count >= len(right):
                count = 0
        # Картинка котика
        kitii = pygame.image.load('Game/Images/Character/kitiie_cat.png')
        screen.blit(kitii, (600, 380))
        player_position = pygame.Vector2(p_x, p_y)
        cat_position = pygame.Vector2(600, 380)
        radius = 150
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Клік на картинку котика
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                cat_rect = kitii.get_rect(topleft=(680, 440))
                if cat_rect.collidepoint(mouse_position):
                    # Визначення відстані між гравцем і котиком
                    distance = player_position.distance_to(cat_position)
                    if distance <= radius:

                        while True:
                            pygame.init()

                            # game variables and costants
                            width = 800
                            height = 600

                            white = (255, 255, 255)
                            gray = (128, 128, 128)

                            tasty_green = (79, 106, 42)
                            correct_green = (140, 210, 119)
                            dark_green = (28, 45, 26)
                            green = (61, 82, 32)

                            yellow = (247, 200, 21)
                            dark_yellow = (156, 74, 26)

                            redish = (82, 65, 38)
                            blue = (119, 143, 210)

                            # functionality

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
                            turns = 0
                            best_score = 0
                            matches = 0

                            real_score = 0

                            game_over = False

                            # create screen
                            screen = pygame.display.set_mode([width, height])

                            pygame.display.set_caption("Game")  # name of the window
                            title_font = pygame.font.Font('Game/Fonts/Aller_Rg.ttf', 50)
                            restart_font = pygame.font.Font('Game/Fonts/Aller_Rg.ttf', 40)
                            small_font = pygame.font.Font('Game/Fonts/Aller_Rg.ttf', 20)


                            def draw_backgrounds():
                                top_menu = pygame.draw.rect(screen, tasty_green, [0, 0, width, 100])
                                top_menu_border = pygame.draw.rect(screen, green, [0, 0, width, 100], 10)
                                # draw.rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)

                                top_menu_text = title_font.render('BOSS FIGHT', True, white)
                                screen.blit(top_menu_text, (260, 20))

                                board_space = pygame.draw.rect(screen, redish, [0, 100, width, height - 200])
                                bottom_menu = pygame.draw.rect(screen, tasty_green, [0, height - 100, width, 100])
                                bottom_menu_border = pygame.draw.rect(screen, green, [0, height - 100, width, 100], 10)

                                restart_button = pygame.draw.rect(screen, green, [290, height - 87, 200, 75], 0, 5)
                                restart_button_border = pygame.draw.rect(screen, dark_green,
                                                                         [290, height - 87, 200, 75], 5, 5)
                                restart_text = restart_font.render('Restart', True, white)
                                screen.blit(restart_text, (325, 525))

                                turns_text = small_font.render(f'Current Turns: {turns}', True, white)
                                screen.blit(turns_text, (15, 520))

                                real_score_text = small_font.render(f'Score: {real_score}', True, white)
                                screen.blit(real_score_text, (600, 535))

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
                                        piece = pygame.draw.rect(screen, white, [i * 100 + 50, j * 98 + 108, 90, 90], 0,
                                                                 4)
                                        piece_borders = pygame.draw.rect(screen, dark_green,
                                                                         [i * 100 + 50, j * 98 + 108, 95, 95], 5, 4)
                                        board_list.append(piece)

                                        image_path = f"Game/Images/Pictures_For_Pex/game_pic{spaces[i * rows + j]}.png"
                                        image = pygame.image.load(image_path)

                                        # screen.blit(image, (i * 100 + 53, j * 98 + 110)) show pictures

                                # when correct:
                                for r in range(rows):
                                    for c in range(cols):
                                        if correct[r][c] == 1:
                                            pygame.draw.rect(screen, correct_green,
                                                             [c * 100 + 50, r * 98 + 108, 94, 94], 5, 4)
                                            image_path = f"Game/Images/Pictures_For_Pex/game_pic{spaces[c * rows + r]}.png"
                                            image = pygame.image.load(image_path)
                                            screen.blit(image, (c * 100 + 53, r * 98 + 108))

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

                                for item in range(rows * cols):
                                    piece = options_list[random.randint(0, len(options_list) - 1)]
                                    spaces.append(piece)
                                    # print(spaces)
                                    if piece in used:
                                        used.remove(piece)
                                        options_list.remove(piece)
                                    else:
                                        used.append(piece)


                            def check_guess(first, second):
                                global spaces
                                global correct
                                global turns
                                global matches
                                global real_score

                                if spaces[first] == spaces[second]:
                                    col1 = first // rows
                                    col2 = second // rows
                                    row1 = first - (first // rows * rows)
                                    row2 = second - (second // rows * rows)
                                    if correct[row1][col1] == 0 and correct[row2][col2] == 0:
                                        correct[row1][col1] = 1
                                        correct[row2][col2] = 1
                                        turns += 1
                                        matches += 1
                                        real_score += 100

                                else:
                                    turns += 1
                                    if real_score == 0:
                                        real_score = 0
                                    else:
                                        real_score -= 25


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

                                for event in pygame.event.get():  # getting out of the loop
                                    if event.type == pygame.QUIT:
                                        running = False

                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        for i in range(len(board)):
                                            button = board[i]
                                            if not game_over:
                                                if button.collidepoint(event.pos) and not first_guess:
                                                    first_guess = True
                                                    first_guess_num = i

                                                if button.collidepoint(
                                                        event.pos) and not second_guess and first_guess and i != first_guess_num:
                                                    second_guess = True
                                                    second_guess_num = i

                                        if restart.collidepoint(event.pos):
                                            options_list = []
                                            used = []
                                            spaces = []
                                            new_board = True
                                            turns = 0
                                            matches = 0
                                            real_score = 0
                                            first_guess = False
                                            second_guess = False
                                            correct = create_correct_board(rows, cols)
                                            game_over = False
                                            current_time = time.time()

                                if matches == rows * cols // 2:
                                    game_over = True
                                    winner = pygame.draw.rect(screen, yellow, [10, height - 350, width - 20, 100], 0, 5)
                                    winner_border = pygame.draw.rect(screen, dark_yellow,
                                                                     [10, height - 350, width - 20, 100], 5, 5)
                                    winner_text = title_font.render(f'You Won In {turns} moves!', True, white)
                                    screen.blit(winner_text, (width - winner_text.get_height() - 580, height - 330))
                                    if best_score > real_score or best_score == 0:
                                        best_score = real_score

                                if first_guess:
                                    image_path = f"Game/Images/Pictures_For_Pex/game_pic{spaces[first_guess_num]}.png"
                                    image = pygame.image.load(image_path)
                                    location = (first_guess_num // rows * 100 + 55,
                                                (first_guess_num - (first_guess_num // rows * rows)) * 98 + 110)
                                    screen.blit(image, location)

                                if second_guess:
                                    image_path = f"Game/Images/Pictures_For_Pex/game_pic{spaces[second_guess_num]}.png"
                                    image = pygame.image.load(image_path)
                                    location = (second_guess_num // rows * 100 + 55,
                                                (second_guess_num - (second_guess_num // rows * rows)) * 98 + 110)
                                    screen.blit(image, location)

                                # timer
                                if game_over == False:
                                    timer_porfavor = time.time() - current_time
                                    minutes = int(timer_porfavor // 60)
                                    seconds = int(timer_porfavor % 60)
                                    time_string = "{:02d}:{:02d}".format(minutes, seconds)
                                    time_string_text = small_font.render(time_string, True, (255, 255, 255))
                                    screen.blit(time_string_text, (width - 90 - time_string_text.get_width(),
                                                                   height - 300 - time_string_text.get_height() // 2))

                                pygame.display.flip()
                            pygame.quit()
                            sys.exit()


        clock.tick(18)


    elif game_state == "about":
        #Нове вікно
        fon = pygame.image.load('Game/Images/Back_Green.jpg')
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 36)

        #Історія(трішки лору)\розміщення і наявність тексту
        font = pygame.font.Font(None, 24)

        About_Back = pygame.Rect(50, 500, 150, 33)
        About_Back_text = pygame.font.SysFont('Game/Fonts/Roboto-Black.ttf', 30).render("Back", True, 'white')
        About_Back_rect = About_Back_text.get_rect(center=About_Back.center)

        pygame.draw.rect(screen, 'Black', About_Back)
        screen.blit(About_Back_text, About_Back_rect)



        # Встановлюємо текст і колір
        story = [
            "Our task was to make a fairly familiar and well-known Pekseso game...",
            "But along the way, we came to the idea that this game can be made",
            "more diverse, at least in terms of design, so you can familiarize",
            "yourself with the history and dive into the small, but interesting world",
            "of Spexiso.",
            "The story tells about an unknown assassin whose task was to",
            "defeat a monster that terrorized the settlement, but he",
            "did not expect that he would face not a physically strong opponent,",
            "but a logically strong one... For the assassin, it turned out to be",
            "another difficult test... And then, having finished with",
            "a preface you can see it all for yourself…"
        ]
        text_color = (0, 0, 0)  # Чорний колір тексту (RGB)

        # Встановлюємо позицію тексту
        text_position = (30, 30)  # Початкова позиція тексту (x, y)
        line_spacing = 25
        for i, line in enumerate(story):
            text = font.render(line, True, text_color)
            y = text_position[1] + (i * line_spacing)
            screen.blit(text, (text_position[0], y))

        #Кнопка повернення
        About_Back = pygame.Rect(50, 500, 150, 33)
        About_Back_text = pygame.font.SysFont('Game/Fonts/Roboto-Black.ttf', 30).render("Back", True, 'white')
        About_Back_rect = About_Back_text.get_rect(center=About_Back.center)

        pygame.draw.rect(screen, 'Black', About_Back)
        screen.blit(About_Back_text, About_Back_rect)

        #Тут буде персонаж, але поки прямокутник
        character = pygame.image.load('Game/Images/Character/For_prev.jpg')
        screen.blit(character, (580, 50))

        #Тут буде карта, але поки прямокутник
        rectangle_color = (0, 0, 0)  # Червоний колір (RGB)
        rectangle_position = (300, 310)  # Позиція прямокутника (x, y)
        rectangle_size = (480, 250)  # Розміри прямокутника (ширина, висота)
        pygame.draw.rect(screen, rectangle_color, pygame.Rect(rectangle_position, rectangle_size))


        # Оновлюємо вікно гри
        pygame.display.flip()

    pygame.display.update()