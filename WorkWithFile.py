def add_person(person):
    data = open('Dict.txt', 'a', encoding='utf-8')
    data.write(person)
    data.write('\n')
    data.close()

def show_all():
    data = open ('Dict.txt', 'r', encoding = 'utf-8')
    for line in data:
        print(line[:-1])
    data.close()

def search_element(name):
    with open ('Dict.txt', 'r', encoding = 'utf-8') as data:
        for line in data:
            if name in line.split():
                print(line)
                break
        else:
            print('Такого нету')

def delete_data_from_file(name):
    with open('Dict.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines()
    with open('Dict.txt', 'w', encoding='utf-8') as data:
        for line in lines:
            if name not in line:
                data.write(line)
        print('Данные успешно удалены из файла.')


def change_data_in_file(old_name, new_name):
    with open('Dict.txt', 'r+', encoding='utf-8') as data:
        lines = data.readlines()
        for line in lines:
            if old_name in line:
                line = line.replace(old_name, new_name)
            data.write(line)
        print('Данные успешно изменены.')
    





