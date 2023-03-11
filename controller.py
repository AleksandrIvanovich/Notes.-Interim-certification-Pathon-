import interface
import database_module
import logger
import export_to_csv



def run():
    
    while True:
    
        command = interface.start_page()

        match command:
            case '1':     # Список всех заметок
                data = database_module.get_all_notes()
                interface.show_notes(data)

            case '2': # Поиск заметки
                user_search = interface.search_note()
                data = database_module.get_note_info(user_search)
                interface.show_notes(data)
            
            case '3': # Добавить заметку
                new_note = interface.add_note()
                database_module.add_notes(new_note)
                logger.add(new_note, 'added')
                interface.done_message()

            case '4': # Изменить запись
                data = database_module.get_all_notes()
                if data == []:
                    print("Список заметок пуст\n")
                else:   
                    interface.show_notes(data)
                    deal_id = interface.change_note()
                    one_note = database_module.get_one_note(deal_id)
                    changed_note = interface.change_note_content(one_note)
                    if changed_note['status'] == 'Я что-то нажал и всё сломалось':
                        database_module.delete_note(changed_note['note_id'])
                        logger.add(changed_note, 'deleted')
                    else:
                        database_module.change_note(changed_note)
                        logger.add(changed_note, 'changed')
            
            case '5': # Экспорт
                data = export_to_csv.export_csv()
                interface.result_mess(True)
                logger.add(data, 'exported')
                      
            case '6': # Выход
                interface.bye_mess()
                break
            
            case _:
                interface.error_input()


def change_action(user_answer: dict):
    match user_answer['user_choise']:
        case 1: # завершить дело
            return
        
        case 2: # изменить дело
            return

        case 3: # удалить дело
            return