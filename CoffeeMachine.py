  import time

# Функции для работы с файлами
def read_level_from_file(filename):
    try:
        with open(filename, 'r') as file:
            level = int(file.read().strip())
            return level
    except (FileNotFoundError, ValueError):
        print(f"Ошибка при чтении {filename}. Возвращается значение по умолчанию 0.")
        return 0

def write_level_to_file(filename, level):
    with open(filename, 'w') as file:
        file.write(str(level))

def check_water_level():
    return read_level_from_file('water_level.txt')

def check_coffee_beans_level():
    return read_level_from_file('coffee_level.txt')

def check_temperature():
    return read_level_from_file('temperature.txt')

def check_sugar_level():
    return read_level_from_file('sugar_level.txt')

def brew_coffee():
    water_level = check_water_level()
    coffee_level = check_coffee_beans_level()
    temperature = check_temperature()
    sugar_level = check_sugar_level()

    if water_level < 200:
        print("Недостаточно воды для приготовления кофе.")
        return
    
    if coffee_level < 10:
        print("Недостаточно кофе для приготовления.")
        return

    if temperature < 90:
        print("Температура воды недостаточна для приготовления кофе.")
        return

    print("Приготовление кофе...")
    
    # Нагрев воды (симуляция)
    print("Нагрев воды до 90°C...")
    time.sleep(5)  # Имитация времени нагрева
    
    # Симуляция процесса приготовления
    print("Процесс приготовления...")
    time.sleep(5)  # Имитация времени приготовления
    
    # Обновление уровней
    new_water_level = water_level - 200
    new_coffee_level = coffee_level - 10
    
    # Добавление сахара в кофе
    if sugar_level > 0:
        print(f"Добавление {sugar_level} граммов сахара в кофе.")
    
    write_level_to_file('water_level.txt', new_water_level)
    write_level_to_file('coffee_level.txt', new_coffee_level)
    
    print("Кофе успешно приготовлено!")

def set_temperature():
    new_temperature = int(input("Введите новую температуру (°C): "))
    write_level_to_file('temperature.txt', new_temperature)
    print(f"Температура установлена на {new_temperature}°C.")

def set_sugar_level():
    new_sugar_level = int(input("Введите уровень сахара (граммы): "))
    write_level_to_file('sugar_level.txt', new_sugar_level)
    print(f"Уровень сахара установлен на {new_sugar_level} граммов.")

def main():
    while True:
        command = input("Введите 'brew' для приготовления кофе, 'set_temp' для установки температуры, 'set_sugar' для установки сахара или 'exit' для выхода: ").strip().lower()
        if command == 'brew':
            brew_coffee()
        elif command == 'set_temp':
            set_temperature()
        elif command == 'set_sugar':
            set_sugar_level()
elif command == 'exit':
            break
        else:
            print("Неверная команда. Пожалуйста, введите 'brew', 'set_temp', 'set_sugar' или 'exit'.")

if __name__ == "__main__":
    main()


