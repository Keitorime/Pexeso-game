import pygame

pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Определение размеров окна
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Пример кнопки в Pygame")

# Создание кнопки
button_rect = pygame.Rect(150, 100, 100, 50)
button_text = pygame.font.SysFont(None, 30).render("Нажми!", True, WHITE)
text_rect = button_text.get_rect(center=button_rect.center)

# Отрисовка кнопки
pygame.draw.rect(screen, BLACK, button_rect)
screen.blit(button_text, text_rect)

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            # Создание нового окна
            new_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption("Новое окно")

            # Отрисовка текста на новом окне
            new_screen.fill(WHITE)
            new_text = pygame.font.SysFont(None, 50).render("Новое окно!", True, BLACK)
            new_rect = new_text.get_rect(center=new_screen.get_rect().center)
            new_screen.blit(new_text, new_rect)

            # Обновление экрана
            pygame.display.update()

    # Обновление экрана
    pygame.display.update()