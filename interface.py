import time
import database_module
from time  import gmtime, strftime
import locale
import datetime

def error_input():
    print('\033 Ошибка!')
    print('\033 Пожалуйста введите команду соответствующую пункту меню. ')
    time.sleep(1)


def done_message():
    print('\033 Выполнено!')

main_menu = \
    'Выберите пункт меню:\n\
    1. \033 Список заметок\n\
    2. \033 Поиск заметки\n\
    3. \033 Добавить заметку\n\
    4. \033 Изменить заметку\n\
    5. \033 Экспорт заметок в csv формат\n\
    6. \033 Выход'

def start_page():  # Starting page, choose number
    print(main_menu)
    print()
    command = input('\033 Выберите действие:  ')
    print(50 * "_")
    return command

def show_notes(data):  # 1 in menu
    if data != []:
        print('\033 Список заметок: ')
        for item in range(len(data)):
            a = data[item]['note_id']
            b = data[item]['data']  
            c = data[item]['note']  
            d = data[item]['status']
            print(f'{a}) {b}. | {c}. | {d}.')
        print(50 * "•")
    else:
        print('\033 Список заметок пуст')
        print()

def search_note(): # 2 Поиск заметок
    search_request = input('Введите данные для поиска: ')
    print(50 * "=")
    return search_request


def add_note(): # 3 Добавить заметку
    print('\033 Добавление заметки ')
    print(50 * "-")
    locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')
    data_note = strftime("%A %d %b %Yг %H:%M:%S", gmtime())
   
    body_note = input('Введите текст заметки: ')  # text
    status_note = input('Введите статус: ') # text
    note = [{'note_id': 1, 'data': data_note, 'note': body_note, 'status': status_note} ]
    return note  # возвращение списка словаря

def change_note(): # 4 Изменить заметку
    print('\033 Изменить заметку: ')
    print(50 * "~")
    while True:
        try:  
            note_id = int(input('Выберите заметку для внесения изменений: '))
            with open(database_module.path_to_db, 'r', encoding='UTF-8') as file:  # Проверяем, есть ли запись с таким id
                data = database_module.json.load(file) 
            for i in range(0, len(data)):  
                if data == []:
                    print("Cписок заметок пуст")
                elif note_id == int(data[i]['note_id']):
                    return note_id  
            else:   
                print('Заметки с таким номером не существует!') 
        except:
            print('Вы ввели не число!')  

def change_note_content(one_note): # Что менять
    while True:
        menu_command = input('Что необходимо сделать?\n 1 - Изменить заметку \n 2 - Удалить заметку\n')
        if menu_command == '1':
            print('\033 Изменить содержание заметки: ')
            while True:
                submenu_command = input('Что необходимо изменить?\n 1 - Заменить содержание\n 2 - Заменить статус\n')     
                match submenu_command:
                    case '1':  # Изменить дату
                        print('Введите новую заметку: ')
                        one_note['note'] = input()
                        done_message()
                        break
                    # case '2':  # Изменить заметку
                    #     print('Введите заметку: ')
                    #     one_note['note'] = input()
                    #     done_message()
                    #     break
                    case '2':  # Изменить статус
                        print('Введите статус: ')
                        one_note['status'] = input()
                        done_message()
                        break
                    case _:
                        error_input()
            break
        elif menu_command == '2':
            one_note['status'] = 'Я что-то нажал и всё сломалось'  # удаление по ID
            done_message()
            break
        else:
            error_input()
    return one_note

def result_mess(done):
    if done:
        done_message()
    else:
        print('\033 Произошла ошибка при выполнении операции!')
        
def bye_mess():  # 6 in menu
    print('Работа завершена!')       