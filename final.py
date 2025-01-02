# Создаем словарь для хранения информации о заметке
note = {}

# Запрашиваем данные и заполняем словарь
note["username"] = input("Укажите имя автора: ")
note["content"] = input("Введите содержание заметки: ")
note["status"] = input("Введите статус заметки ('Активна', 'Закрыта'): ")
note["creation_date"] = input("Укажите дату создания заметки в формате 'ДД-ММ-ГГГГ': ")
note["issue_date"] = input("Укажите дату завершения заметки в формате 'ДД-ММ-ГГГГ': ")

# Собираем заголовки в список внутри словаря
note["titles"] = []
for i in range(3):
    title = input(f"Введите {i + 1} заголовок: ")
    note["titles"].append(title)

# Выводим данные
print("\nИнформация о заметке:")
print("Имя автора:",note["username"])
print("Заголовки:", note["titles"])
print("Содержание:", note["content"])
print("Статус:", note["status"])
print("Дата создания:", note["creation_date"])
print("Дата завершения:", note["issue_date"])
