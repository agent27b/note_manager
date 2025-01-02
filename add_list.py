# Запрашиваем данные
username = input("Укажите имя автора: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки ('Активна', 'Закрыта'): ")
created_date = input("Укажите дату создания заметки в формате 'ДД-ММ-ГГГГ': ")
issue_date = input("Укажите дату завершения заметки в формате 'ДД-ММ-ГГГГ': ")

# Запрашиваем заголовки и формируем список
titles = []
for i in range(3):
    title = input(f"Введите {i + 1} заголовок заметки: ")
    titles.append(title)

# Выводим данные
print("\nИнформация о заметке:")
print("Имя автора:", username)
print("Заголовки:", titles)
print("Содержание:", content)
print("Статус:", status)
print("Дата создания:", created_date)
print("Дата завершения:", issue_date)
