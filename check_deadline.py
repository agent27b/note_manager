from datetime import datetime

def get_current_date():
    """Возвращает текущую дату в формате день-месяц-год."""
    return datetime.now().strftime("%d-%m-%Y")

def get_deadline_from_user():
    """
    Запрашивает у пользователя дату дедлайна и возвращает её в формате datetime.
    Поддерживает несколько форматов ввода: "день-месяц-год" и "год-месяц-день".
    Повторяет запрос, если введённая дата имеет неверный формат.
    """
    while True:
        deadline_input = input("Введите дату дедлайна (в формате день-месяц-год или год-месяц-день): ").strip()
        try:
            # Пробуем преобразовать введённую строку в объект datetime
            for fmt in ("%d-%m-%Y", "%Y-%m-%d"):
                try:
                    deadline = datetime.strptime(deadline_input, fmt)
                    return deadline
                except ValueError:
                    continue
            # Если ни один формат не подошёл
            raise ValueError
        except ValueError:
            print("Ошибка: неверный формат даты. Убедитесь, что вводите дату в формате день-месяц-год или год-месяц-день, например: 10-12-2024 или 2024-12-10.")

def calculate_days_difference(current_date, deadline):
    """Вычисляет разницу в днях между текущей датой и дедлайном."""
    difference = (deadline - current_date).days
    return difference

def analyze_deadline(current_date, deadline):
    """
    Анализирует дедлайн и выводит соответствующее сообщение:
    - Если дедлайн истёк, выводит количество прошедших дней.
    - Если дедлайн сегодня, выводит соответствующее сообщение.
    - Если дедлайн в будущем, выводит количество оставшихся дней.
    """
    difference = calculate_days_difference(current_date, deadline)
    if difference < 0:
        print(f"Внимание! Дедлайн истёк {abs(difference)} дня(дней) назад.")
    elif difference == 0:
        print("Дедлайн сегодня!")
    else:
        print(f"До дедлайна осталось {difference} дня(дней).")

def main():
    """Основная функция программы."""
    # Получаем текущую дату
    current_date = datetime.now()
    print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}")

    # Запрашиваем у пользователя дату дедлайна
    deadline = get_deadline_from_user()

    # Анализируем дедлайн и выводим результат
    analyze_deadline(current_date, deadline)

# Запуск программы
if __name__ == "__main__":
    main()