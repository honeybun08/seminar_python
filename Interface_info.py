import os
from hw8_task1 import *
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')


while True:
    clear()
    print('Выберите операцию: \n 1 - Добавление контакта \n 2 - Вывод по фамилии \n 3 - Удаление данных '
           '\n 4 - Изменение данных \n 5 - Вывод всех контактов \n 6 - Выход')
    choose()
    input('Введите ENTER чтобы продолжить')

  