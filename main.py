# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import time

WIDTH = 1024
HEIGHT = 700
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Клавиатурный тренажёр")
clock = pygame.time.Clock()
# фоновая музыка
pygame.mixer.music.load("Toby Fox — Fallen Down (www.lightaudio.ru).mp3")
pygame.mixer.music.play(-1)
s = pygame.mixer.Sound("de2f1291e610ae2.ogg")
# кнопка start
start = pygame.image.load("start.jpg")
# клавиатура
klav = pygame.image.load("клавиатура.jpeg")
# кнопка restart
restart = pygame.image.load("restart.jpg")
# набираемый текст в файле (подойдёт любой текст без заглавных букв(на латинице))
font = pygame.font.Font(None, 120)
text = ''
with open('sentences.txt') as f:
    for string in f:
        text += string[:len(string)]
if (len(text) == 0):
    text = 'default text'
text_list = text.split(sep=' ')
sum_letters = 0
for i in range(len(text_list)):
    sum_letters += len(text_list[i])
codes = {'!': 33, "'": 39, ',': 44, '.': 46, '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55,
         '8':
             56, '9': 57, '?': 63, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104,
         'i': 105, 'j': 106, 'k': 107,
         'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118,
         'w': 119,
         'x': 120, 'y': 121, 'z': 122}
i = 0
j = 0
word = text_list[j]
write_full_word = font.render(word, True, WHITE)
# подсчёт ошибок и скорости
old_result = ['0', '0']
err_counter = 0
total_time = 0
font1 = pygame.font.Font(None, 65)
write_err = font1.render("Errors: 0", True, RED)
write_time = font1.render("Timer: 0", True, RED)
# Цикл игры
running = True
without_start = True  # начал печатать - False
while (running):
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    screen.fill(BLACK)
    # вывод клавиатуры
    screen.blit(klav, (0, 308))
    # вывод кнопки restart
    screen.blit(restart, (974, 0))
    screen.blit(write_err, (0, 30))
    if (without_start):
        write_time = font1.render("Timer: 0", True, GREEN)
    else:
        timer = round((time.time() - total_time), 1)
        write_time = font1.render("Timer: " + str(timer), True, GREEN)
    white_red = font.render(word[:i], True, RED)
    screen.blit(write_time, (0, 80))
    screen.blit(write_full_word, ((1024 - len(word) * 25) / 2 - 40, 150))
    screen.blit(white_red, ((1024 - len(word) * 25) / 2 - 40, 150))

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window

        if event.type == pygame.QUIT:
            pygame.quit()
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1)):
            x = event.pos[0]
            y = event.pos[1]
            if ((974 < x <= WIDTH) and (0 < y <= 50)):
                without_start = True
                i = 0;
                j = 0;
                word = text_list[j]
                err_counter = 0
                write_full_word = font.render(word, True, WHITE)
                write_err = font1.render("Errors: 0", True, RED)
                write_time = font1.render("Timer: 0", True, RED)
                break
        elif event.type == pygame.KEYDOWN:
            without_start = False
            if (i == 0 and j == 0):
                total_time = time.time()
            if (event.key == codes[word[i]]):
                white_red = font.render(word[:i + 1], True, RED)
                screen.blit(white_red, ((1024 - len(word) * 25) / 2 - 40, 150))
                i += 1
            else:
                s.play()
                err_counter += 1
                screen.fill(BLACK)
                write_err = font1.render("Errors: " + str(err_counter), True, RED)
                white_red = font.render(word[:i], True, RED)
                timer = round((time.time() - total_time), 1)
                write_time = font1.render("Timer: " + str(timer), True, GREEN)
                screen.blit(write_full_word, ((1024 - len(word) * 25) / 2 - 40, 150))
                screen.blit(white_red, ((1024 - len(word) * 25) / 2 - 40, 150))
                screen.blit(klav, (0, 308))
                screen.blit(restart, (974, 0))
                screen.blit(write_err, (0, 30))
                screen.blit(write_time, (0, 80))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
    if ((i == len(word)) and (j < len(text_list) - 1)):
        screen.fill(BLACK)
        screen.blit(klav, (0, 308))
        screen.blit(write_err, (0, 30))
        screen.blit(write_time, (0, 80))
        screen.blit(restart, (974, 0))
        i = 0
        j += 1
        word = text_list[j]
        write_full_word = font.render(word, True, WHITE)
        screen.blit(write_full_word, ((1024 - len(word) * 25) / 2 - 40, 150))
        pygame.display.flip()
    elif ((j == len(text_list) - 1) and (i == len(word))):
        pygame.mixer.music.pause()
        # фоновая музыка
        pygame.mixer.music.load("Toby Fox — 1 – Once Upon a Time (OST_ Undertale) (www.lightaudio.ru).mp3")
        pygame.mixer.music.play(-1)
        timer = time.time() - total_time
        screen.fill(BLACK)
        font2 = pygame.font.Font(None, 80)
        results = font.render('Your results', True, RED)
        screen.blit(results, (260, 0))
        new_speed = font2.render('Speed: ' + str(round(sum_letters / timer, 2)) + ' let/sec', True, GREEN)
        old_speed = font2.render('Speed: ' + old_result[0] + ' let/sec', True, GREEN)
        new_errors = font2.render('Errors: ' + str(err_counter), True, RED)
        old_errors = font2.render('Errors: ' + old_result[1], True, RED)
        screen.blit(new_errors, (0, 150))
        screen.blit(new_speed, (0, 280))
        screen.blit(old_errors, (550, 150))
        screen.blit(old_speed, (550, 280))
        screen.blit(start, (240, 400))
        old_result[0] = str(round(sum_letters / timer, 2))
        old_result[1] = str(err_counter)
        without_start = True
        press_start = True
        pygame.display.flip()
        while press_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if ((event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1)):
                    pygame.mixer.music.pause()
                    # фоновая музыка
                    pygame.mixer.music.load("Toby Fox — Fallen Down (www.lightaudio.ru).mp3")
                    pygame.mixer.music.play(-1)
                    x = event.pos[0]
                    y = event.pos[1]
                    if ((240 < x <= 770) and (400 < y <= 600)):
                        without_start = True
                        i = 0;
                        j = 0;
                        word = text_list[j]
                        err_counter = 0
                        write_full_word = font.render(word, True, WHITE)
                        write_err = font1.render("Errors: 0", True, RED)
                        write_time = font1.render("Timer: 0", True, RED)
                        press_start = False
pygame.quit()
