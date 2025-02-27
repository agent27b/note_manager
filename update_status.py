def display_current_status(status):
    # Показываем текущий статус заметки
    print(f"Текущий статус заметки: \"{status}\"")

def display_status_options():
    # Показываем доступные для выбора варианты
    print("\nВыберите новый статус заметки:")
    print("1. выполнено")
    print("2. в процессе")
    print("3. отложено")
    print("Или введите новый статус вручную.")

def validate_status(status):
    # Проверяем правильность статуса
    valid_statuses = ["выполнено", "в процессе", "отложено"]
    return status.lower() in valid_statuses

def get_new_status():
    # Запрашиваем новый статус и показываем пользователю
    while True:
        choice = input("Ваш выбор (введите число или текст): ").strip().lower()

        # Если пользователь вводит число
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                return "выполнено"
            elif choice == 2:
                return "в процессе"
            elif choice == 3:
                return "отложено"
            else:
                print("Ошибка! Введите число от 1 до 3.")
        # Если пользователь вводит текст
        else:
            if validate_status(choice):
                return choice
            else:
                print("Ошибка! Статус может быть: выполнено, в процессе, отложено.")

def main():
    # Инициализация текущего статуса заметки
    note = {"status": "в процессе"}

    # Показываем текущий статус
    display_current_status(note["status"])

    # Показываем доступные для выбора статусы
    display_status_options()

    # Запрашиваем новый статус
    new_status = get_new_status()

    # Обновляем статус заметки
    note["status"] = new_status

    # Выводим обновлённый статус
    print(f"\nСтатус заметки успешно изменён на: \"{note['status']}\"")

# Запуск программы
if __name__ == "__main__":
    main()