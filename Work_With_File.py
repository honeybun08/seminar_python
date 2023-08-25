import os
import re

filepath = os.path.join("C:/Users/Lenovo/Desktop/GeekBrains/python_seminar",'Info_dict.txt')


def adding(array):
    dict = {0: 'Фамилия:', 1: 'Имя:', 2: 'Отчество:', 3: 'Номер:'}
    counter = 0
    if os.path.exists(filepath):
        with open(filepath,'a',encoding = 'utf-8') as f:
            f.writelines('-'*2 + 'Данные контакта' + '-'*2 + '\n')
            for i in array:
                f.writelines(dict[counter] + ' ' + i + '\n')
                counter += 1
            f.write('\n')
            return print(f'Контакт был добавлен)')         
    else:
        with open(filepath,'w+',encoding = 'utf-8') as f:
            f.writelines('-'*2 + 'Данные контакта' + '-'*2 + '\n')
            for i in array:
                f.writelines(dict[counter] + ' ' + i)
                f.write('\n')
                counter += 1
            f.write('\n')
            return print(f'Контакт был добавлен)')
            

def search_element(teg):
    if os.path.exists(filepath):
        with open(filepath,'r',encoding = 'utf-8') as f:
            new_array = [re.sub('\s+','',line) for line in f.readlines()]
            for i in range(0,len(new_array)):
                if teg in new_array[i]:
                    return print(f'По контакту {teg} нашлось: \n {new_array[i]} \n {new_array[i+1]} \n {new_array[i+2]} \n {new_array[i+3]}')
            return print(f'По контакту "{teg}" ничего не найдено')
    else: print('Файл не существует:( ')


def show_all():
    with open(filepath,'r',encoding = 'utf-8') as f:
        for line in f:
            print(line)


def delete(teg):
    check = False
    with open(filepath,'r',encoding = 'utf-8') as f:
       array = [line for line in f.readlines()]
       for i in range(len(array)):
           if teg in array[i]:
               check = True
               array[i-1], array[i], array[i+1], array[i+2], array[i+3], array[i+4] = '', '', '', '', '', ''
    if check == True:
        with open(filepath,'w',encoding = 'utf-8') as f:
            f.writelines(array)
            return print(f'Данные контакта "{teg}" были удалены)')
    return print(f'Контакт "{teg}" не найден:( ')

# Функция изменения данных в файле
def change(teg, diction, new_teg):
    check = False
    dict = {'1': 'Фамилия:', '2': 'Имя:', '3': 'Отчество:', '4': 'Номер:'}
    # if diction not in dict.keys():
    #     return print(f'Значение "{diction}" не подходит условию:( ')
    with open(filepath,'r',encoding = 'utf-8') as f:
        array = [line for line in f.readlines()]
        for i in range(len(array)):
            if teg in array[i]:
                check = True
                if diction == '1': array[i] = dict[diction] + ' ' + new_teg + '\n'
                if diction == '2': array[i+1] = dict[diction] + ' '  + new_teg + '\n'
                if diction == '3': array[i+2] = dict[diction] + ' '  + new_teg + '\n'
                if diction == '4': array[i+3] = dict[diction] + ' '  + new_teg + '\n'    
    if check == True:               
        with open(filepath,'w',encoding = 'utf-8') as f:
            f.writelines(array)
            return print(f'Данные контакта "{teg}" были изменены)')
    else: return print(f'Контакт "{teg}"не найден:( ')






