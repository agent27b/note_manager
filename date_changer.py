# Запрашиваем данные
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки ('Активна', 'Выполнена':")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# Переводим строки в дату
from datetime import datetime
temp_created_date = datetime.strptime(created_date, "%d-%m-%Y").date()
temp_issue_date = datetime.strptime(issue_date, "%d-%m-%Y").date()


# Выводим данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", datetime.strftime(temp_created_date, "%d-%m")) # Выводим обрезанную дату начала
print("Дата истечения заметки:", datetime.strftime(temp_issue_date, "%d-%m")) # Выводим обрезанную дату окончания

