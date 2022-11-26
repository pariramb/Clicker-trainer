import pygame

import objects
import constans

codes = {"'": 39, ',': 44, '.': 46, '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55,
         '8':
             56, '9': 57, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104,
         'i': 105, 'j': 106, 'k': 107,
         'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118,
         'w': 119,
         'x': 120, 'y': 121, 'z': 122}
# Шрифты
font = pygame.font.Font(None, 120)
font2 = pygame.font.Font(None, 80)
# набираемый текст в файле (подойдёт любой текст без заглавных букв(на латинице))
text = ''
with open('artifacts\\sentences.txt') as f:
    for string in f:
        text += string[:len(string)]
if (len(text) == 0):
    text = 'default text'
text_list = text.split(sep=' ')
sum_letters = 0
for i in range(len(text_list)):
    sum_letters += len(text_list[i])
old_result = ['0', '0']
write_err = objects.font.render("Errors: 0", True, constans.RED)
write_time = objects.font.render("Timer: 0", True, constans.RED)
