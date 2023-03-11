from database_module import get_all_notes
import csv



def export_csv():
    temp = get_all_notes() # Возвращает весь справочник из рабочего файла

    file_csv = "bd_csv_export.csv" # задали имя файлу в который выгружаем

    with open(file_csv, "w", encoding = 'UTF-8', newline = "") as file: 
        colone = temp[0].keys()
        writer = csv.DictWriter(file, fieldnames = colone)
        writer.writeheader()
        writer.writerows(temp)
    
    print(f"Данные перенесены в файл {file_csv}")

 