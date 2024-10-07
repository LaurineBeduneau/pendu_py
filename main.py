import pygame
import task9

pygame.init()

background_image = pygame.image.load('fond-vectoriel.jpg')

(width, height) = (600, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jeu du Pendu')

font = pygame.font.Font(None, 36)
text_color = (0, 0, 0)
button_color = (173, 216, 230)

def draw_stickman(screen, errors):
    if errors > 0:
        pygame.draw.circle(screen, (0, 0, 0), (300, 150), 30, 2)
    if errors > 1:
        pygame.draw.line(screen, (0, 0, 0), (300, 180), (300, 300), 2)
    if errors > 2:
        pygame.draw.line(screen, (0, 0, 0), (300, 200), (250, 250), 2)
    if errors > 3:
        pygame.draw.line(screen, (0, 0, 0), (300, 200), (350, 250), 2)
    if errors > 4:
        pygame.draw.line(screen, (0, 0, 0), (300, 300), (250, 400), 2)
    if errors > 5:
        pygame.draw.line(screen, (0, 0, 0), (300, 300), (350, 400), 2)

def display_word(screen, font, word):
    text = font.render(word, True, text_color)
    screen.blit(text, (150, 500))

def display_message(screen, font, message):
    text = font.render(message, True, text_color)
    screen.blit(text, (150, 250))

alphabet = [chr(i) for i in range(97, 123)]
buttons = []
for index, letter in enumerate(alphabet):
    x = 30 + (index % 13) * 40
    y = 40 + (index // 13) * 40
    rect = pygame.Rect(x, y, 30, 30)
    buttons.append((rect, letter))

running = True
game_over = False
message = ""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for rect, letter in buttons:
                if rect.collidepoint(mouse_pos):
                    game_over, message = task9.update_game(letter)
                    win_check, win_message = task9.check_win()
                    if win_check:
                        message = win_message
                        game_over = True
                    break

    screen.blit(background_image, (0, 0))
    draw_stickman(screen, task9.error)
    display_word(screen, font, ' '.join(task9.display))

    for rect, letter in buttons:
        pygame.draw.rect(screen, button_color, rect)
        text = font.render(letter, True, text_color)
        screen.blit(text, (rect.x + 5, rect.y + 5))

    if game_over:
        display_message(screen, font, message)

    pygame.display.flip()

pygame.quit()