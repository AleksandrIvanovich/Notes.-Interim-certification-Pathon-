import json


path_to_db = 'db_notebook.json'

def get_all_notes():  # Возвращает весь список заметок из файла db_notebook.json
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file) 
        data = [data[i] for i in range(0, len(data))]
    return data

def get_one_note(note_id_get): # Возвращает одну заметку по его note_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        one_note_get = {}
        for i in range(0, len(data)): 
            if note_id_get == data[i]['note_id']:
                one_note_get = data[i]
                break
    return one_note_get

def get_note_info(note_info_get): # Возвращает контакты по вхождению в значение любого из ключей surname, name, phone, comment
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        info_note_get = []
        for i in range(0, len(data)): 
            if  note_info_get.lower() in data[i]['data']:
                info_note_get.append(data[i])
            elif note_info_get.lower() in data[i]['note'].lower():
                info_note_get.append(data[i])
            elif note_info_get.lower() in data[i]['status'].lower():
                info_note_get.append(data[i])
            
    return info_note_get

def add_notes(notes_new_dict):  # Добавление новых заметок в БД 
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        for i in range(0, len(notes_new_dict)):
            if (data == []): # Если список пуст
                data.append(notes_new_dict[i]) # Добавляем первую заметку
            else:
                notes_new_dict[i]['note_id'] = data[len(data)-1]['note_id']+1
                data.append(notes_new_dict[i])     # Добавляем в список словарей новую заметку   
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)
        
def change_note(note_edit):  # Изменение заметки
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)

        for i in range(0, len(data)): # Для изменения заметки c note_id = 6, находим в БД словарь с note_id = 6 и перезаписываем его.
            if note_edit['note_id'] == data[i]['note_id']:
                data[i] = note_edit
        
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)    

def delete_note(note_id_delete): # Удаление заметки в заменки по note_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)      
        for i in range(0, len(data)): 
            if data[i]['note_id'] == note_id_delete: # находим индекс элемента в списке словарей с нужным note_id
                index_del = i
                break
        data.pop(index_del)   # Удаляем из списка словарь с нужным note_id
        for i in range(0, len(data)): # Перезаписаваем в каждом словаре списка ключ note_id
            data[i]['note_id'] = i+1
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)    

def clear_db(path_to_db): # Очистка базы данных
    first_element = [{'id_counter': 0}, ]
    with open(path_to_db, 'w') as file:
        json.dump(first_element, file, indent=4)
