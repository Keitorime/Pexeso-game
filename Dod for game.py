# flags = pygame.NOFRAME прибирає рамку вікна
# pygame.display.set_caption() назва вікна
# screen.fill((255, 255, 255)) Заливка вікна

# elif event.type == pygame.KEYDOWN:
# if event.key == pygame.K_a:   додає клавішу на яку змінюється колір
#     screen.fill((103, 165, 54))


# image = pygame.image.load('Game/Images/Draicon.png')
#  додає картинку на основний екран
# screen.blit(image, (100, 0))

# elif event.type == pygame.KEYDOWN: перемикання кольору головного екрану по кнопках на клавіатурі
#     if event.key == pygame.K_a:
#         screen.fill((0, 0, 0))
#     if event.key == pygame.K_b:
#         screen.fill((255, 255, 255))
#     if event.key == pygame.K_c:
#         screen.fill((103, 165, 54))

# pygame.draw.circle(screen, 'Blue', (250,150), 30) додає коло

# square = pygame.Surface((100,40)) додає квадрат
# square.fill('Green')
# screen.blit(square,(0,0))

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spexiso")
icon = pygame.image.load('Game/Images/Draicon.png')
pygame.display.set_icon(icon)
image = pygame.image.load('Game/Images/Background2.jpg')
font = pygame.font.Font('Game/Fonts/Roboto-Black.ttf', 40)
text = font.render('Spexiso', True, 'Black')

Start = pygame.Rect(50, 380, 150, 33)
Start_text = pygame.font.SysFont('Game/Fonts/Roboto-Black.ttf', 30).render("Start", True, 'white')
Start_rect = Start_text.get_rect(center=Start.center)

About_Game = pygame.Rect(50, 420, 150, 33)
About_Game_text = pygame.font.SysFont('Game/Fonts/Roboto-Black.ttf', 30).render("About", True, 'white')
About_Game_rect = About_Game_text.get_rect(center=About_Game.center)

Exit = pygame.Rect(50, 460, 150, 33)
Exit_text = pygame.font.SysFont('Game/Fonts/Roboto-Black.ttf', 30).render("Exit", True, 'white')
Exit_rect = Exit_text.get_rect(center=Exit.center)

screen.blit(image, (0, 0))
screen.blit(text, (600, 35))
pygame.draw.rect(screen, 'Black', Start)
screen.blit(Start_text, Start_rect)

pygame.draw.rect(screen, 'Black', About_Game)
screen.blit(About_Game_text, About_Game_rect)

pygame.draw.rect(screen, 'Black', Exit)
screen.blit(Exit_text, Exit_rect)

pygame.display.update()
procid = True
while procid:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            procid = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and Exit_rect.collidepoint(event.pos):
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and Start_rect.collidepoint(event.pos):
            # Создание нового окна
            new_screen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("Spexico")

            # Отрисовка текста на новом окне
            new_screen.fill('White')
            new_text = pygame.font.SysFont(None, 50).render("New window", True, 'Black')
            new_rect = new_text.get_rect(center=new_screen.get_rect().center)
            new_screen.blit(new_text, new_rect)

            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONDOWN and About_Game_rect.collidepoint(event.pos):
            new_screen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("Spexico")

            fon = pygame.image.load('Game/Images/Back_Green.jpg')
            screen.blit(fon, (0, 0))
            # new_text = pygame.font.SysFont(None, 50).render("New window", True, 'Black')
            # new_rect = new_text.get_rect(center=new_screen.get_rect().center)
            # new_screen.blit(new_text, new_rect)

            About_Back = pygame.Rect(50, 500, 150, 33)
            About_Back_text = pygame.font.SysFont('Game/Fonts/Roboto-Black.ttf', 30).render("Back", True, 'white')
            About_Back_rect = About_Back_text.get_rect(center=About_Back.center)
            pygame.draw.rect(new_screen, 'Black', About_Back)
            new_screen.blit(About_Back_text, About_Back_rect)

            pygame.display.update()


