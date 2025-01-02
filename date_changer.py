# Запрашиваем данные
username = input("Укажите имя автора: ")
title = input("Введите заголовок заметки: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки ('Активна', 'Закрыта'): ")
created_date = input("Укажите дату создания заметки в формате 'ДД-ММ-ГГГГ': ")
issue_date = input("Укажите дату завершения заметки в формате 'ДД-ММ-ГГГГ': ")

# Преобразуем строки в дату
from datetime import datetime
temp_created_date = datetime.strptime(created_date, "%d-%m-%Y").date()
temp_issue_date = datetime.strptime(issue_date, "%d-%m-%Y").date()

# Выводим данные
print("\nИнформация о заметке:")
print("Имя автора:", username)
print("Заголовок:", title)
print("Содержание:", content)
print("Статус:", status)
print("Дата создания:", datetime.strftime(temp_created_date, "%d-%m")) # Выводим обрезанную дату начала
print("Дата завершения:", datetime.strftime(temp_issue_date, "%d-%m")) # Выводим обрезанную дату окончания

