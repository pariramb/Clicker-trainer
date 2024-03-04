import pygame
import time

import constans
import objects
import text

i = 0
j = 0
word = text.text_list[j]
write_full_word = text.font.render(word, True, constans.WHITE)
# подсчёт ошибок и скорости
err_counter = 0
total_time = 0
# Цикл игры
running = True
without_start = True  # начал печатать - False

def enter(event):
    global i, j, word, write_full_word, err_counter, total_time, running, without_start
    # после этих слов в моем коде появилась жесткая возможность выйти из игры
    if event.type == pygame.QUIT:
        pygame.quit()
    if ((event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1)):
        #координаты зажатой кнопки мышки
        x = event.pos[0]
        y = event.pos[1]
        if ((974 < x <= constans.WIDTH) and (0 < y <= 50)):
            without_start = True
            i = 0
            j = 0
            word = text.text_list[j]
            err_counter = 0
            write_full_word = text.font.render(word, True, constans.WHITE)
            write_err = objects.font.render("Errors: 0", True, constans.RED)
            write_time = objects.font.render("Timer: 0", True, constans.RED)
            return
    elif event.type == pygame.KEYDOWN:
        without_start = False
        if (i == 0 and j == 0):
            #ежели мы не попали не по одной букве в самом начале - таймер все равно побежит)))
            total_time = time.time()
        if (event.key == text.codes[word[i]]):
            #делаем правильные буквы красным
            white_red = text.font.render(word[:i + 1], True, constans.RED)
            objects.screen.blit(white_red, ((1024 - len(word) * 25) / 2 - 40, 150))
            i += 1
        else: #неправильная буква после начала игры
            objects.s.play() #звук ошибки
            err_counter += 1
            objects.screen.fill(constans.BLACK)
            write_err = objects.font.render("Errors: " + str(err_counter), True, constans.RED)
            white_red = text.font.render(word[:i], True, constans.RED)
            timer = round((time.time() - total_time), 1)
            write_time = objects.font.render("Timer: " + str(timer), True, constans.GREEN)
            objects.screen.blit(write_full_word, ((1024 - len(word) * 25) / 2 - 40, 150))
            objects.screen.blit(white_red, ((1024 - len(word) * 25) / 2 - 40, 150))
            objects.screen.blit(objects.klav, (0, 308))
            objects.screen.blit(objects.restart, (974, 0))
            objects.screen.blit(write_err, (0, 30))
            objects.screen.blit(write_time, (0, 80))


def new_screen():
    global i, j, word, write_full_word, err_counter, total_time, running, without_start
    pygame.display.flip()
    if ((i == len(word)) and (j < len(text.text_list) - 1)):
        objects.screen.fill(constans.BLACK)
        objects.screen.blit(objects.klav, (0, 308))
        objects.screen.blit(text.write_err, (0, 30))
        objects.screen.blit(text.write_time, (0, 80))
        objects.screen.blit(objects.restart, (974, 0))
        i = 0
        j += 1
        word = text.text_list[j]
        write_full_word = text.font.render(word, True, constans.WHITE)
        objects.screen.blit(write_full_word, ((1024 - len(word) * 25) / 2 - 40, 150))
        pygame.display.flip()
    elif ((j == len(text.text_list) - 1) and (i == len(word))):
        pygame.mixer.music.pause()
        # фоновая музыка
        pygame.mixer.music.load(
            "artifacts/music/TobyFox.mp3")
        pygame.mixer.music.play(-1)
        timer = time.time() - total_time
        objects.screen.fill(constans.BLACK)
        results = text.font.render('Your results', True, constans.RED)
        old_results = text.font.render('Your old results', True, constans.RED)
        new_speed = text.font2.render('Speed: ' + str(round(text.sum_letters / timer, 2)) + ' let/sec', True,
                                      constans.GREEN)
        old_speed = text.font2.render('Speed: ' + text.old_result[0] + ' let/sec', True, constans.GREEN)
        new_errors = text.font2.render('Errors: ' + str(err_counter), True, constans.RED)
        old_errors = text.font2.render('Errors: ' + text.old_result[1], True, constans.RED)
        objects.screen.blit(results, (270, 0))
        objects.screen.blit(new_errors, (0, 100))
        objects.screen.blit(new_speed, (0, 150))
        objects.screen.blit(old_results, (230, 260))
        objects.screen.blit(old_errors, (0, 360))
        objects.screen.blit(old_speed, (0, 410))
        objects.screen.blit(objects.start, (240, 400))
        text.old_result[0] = str(round(text.sum_letters / timer, 2))
        text.old_result[1] = str(err_counter)
        without_start = True
        press_start = True
        pygame.display.flip()
        while press_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if ((event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1)):
                    x = event.pos[0]
                    y = event.pos[1]
                    if ((240 < x <= 770) and (400 < y <= 600)):
                        pygame.mixer.music.pause()
                        #фоновая музыка
                        pygame.mixer.music.load("artifacts/music/Toby_Fox_-_Spider_Dance_64962807.mp3")
                        pygame.mixer.music.play(-1)
                        i = 0
                        j = 0
                        word = text.text_list[j]
                        err_counter = 0
                        write_full_word = text.font.render(word, True, constans.WHITE)
                        write_err = objects.font.render("Errors: 0", True, constans.RED)
                        write_time = objects.font.render("Timer: 0", True, constans.RED)
                        press_start = False


def running():
    while running:
        # Держим цикл на правильной скорости
        objects.clock.tick(constans.FPS)
        objects.screen.fill(constans.BLACK)
        # вывод клавиатуры
        objects.screen.blit(objects.klav, (0, 308))
        # вывод кнопки restart
        objects.screen.blit(objects.restart, (974, 0))
        #objects.screen.blit(text.write_err, (0, 30))
        if (without_start):
            text.write_time = objects.font.render("Timer: 0", True, constans.GREEN)
            text.write_err = objects.font.render("Errors: 0", True, constans.RED)
        else:
            timer = round((time.time() - total_time), 1)
            #вывод времени изменяющегося на экран
            text.write_time = objects.font.render("Timer: " + str(timer), True, constans.GREEN)
            text.write_err = objects.font.render("Errors: " + str(err_counter), True, constans.RED)
            #показывает количество введенных буковок в красном
        white_red = text.font.render(word[:i], True, constans.RED)
        #везде второй аргумент фунцкии blit координата
        objects.screen.blit(text.write_time, (0, 80))
        objects.screen.blit(text.write_err, (0, 30))
        objects.screen.blit(write_full_word, ((1024 - len(word) * 25) / 2 - 40, 150))
        objects.screen.blit(white_red, ((1024 - len(word) * 25) / 2 - 40, 150))

        # Ввод процесса (события)
        for event in pygame.event.get():
            enter(event)
        # После отрисовки всего, переворачиваем экран
        # короче есть два экрана, на одном мы пишем, второй мы видим, после нижней строчки кода эти экраны меняются
        new_screen()
