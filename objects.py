import pygame
import constans

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((constans.WIDTH, constans.HEIGHT))
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
# шрифт
font = pygame.font.Font(None, 65)
