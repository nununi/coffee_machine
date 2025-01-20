     class CoffeeMachine:
         def __init__(self, config_file='config.txt'):
             self.water = 0
             self.coffee_beans = 0
             self.milk = 0
             self.load_config(config_file)

         def load_config(self, config_file):
             try:
                 with open(config_file, 'r') as file:
                     for line in file:
                         key, value = line.strip().split('=')
                         if key == 'water':
                             self.water = int(value)
                         elif key == 'coffee_beans':
                             self.coffee_beans = int(value)
                         elif key == 'milk':
                             self.milk = int(value)
             except FileNotFoundError:
                 print(f"Файл {config_file} не найден. Используются значения по умолчанию.")
             except Exception as e:
                 print(f"Ошибка при загрузке конфигурации: {e}")

         def make_coffee(self, water_needed, coffee_needed, milk_needed):
             if self.water < water_needed:
                 print("Недостаточно воды!")
                 return False
             if self.coffee_beans < coffee_needed:
                 print("Недостаточно кофе!")
                 return False
             if self.milk < milk_needed:
                 print("Недостаточно молока!")
                 return False

             self.water -= water_needed
             self.coffee_beans -= coffee_needed
             self.milk -= milk_needed
             print("Кофе готов!")
             return True

         def refill(self, water, coffee, milk):
             self.water += water
             self.coffee_beans += coffee
             self.milk += milk
             print("Заправка завершена!")

         def status(self):
             print(f"Текущие запасы:")
             print(f"Вода: {self.water} мл")
             print(f"Кофейные зерна: {self.coffee_beans} г")
             print(f"Молоко: {self.milk} мл")

     class ControlMode:
         def __init__(self, machine):
             self.machine = machine

         def run(self):
             while True:
                 print("\nВыберите действие:")
                 print("1. Сделать кофе")
                 print("2. Заправить кофемашину")
                 print("3. Проверить запасы")
                 print("4. Выход")

                 choice = input("Введите номер действия: ")

                 if choice == '1':
                     water_needed = int(input("Введите количество воды (мл): "))
                     coffee_needed = int(input("Введите количество кофе (г): "))
                     milk_needed = int(input("Введите количество молока (мл): "))
                     self.machine.make_coffee(water_needed, coffee_needed, milk_needed)

                 elif choice == '2':
                     water = int(input("Введите количество воды для заправки (мл): "))
                     coffee = int(input("Введите количество кофе для заправки (г): "))
                     milk = int(input("Введите количество молока для заправки (мл): "))
                     self.machine.refill(water, coffee, milk)
                 elif choice == '3':
                     self.machine.status()

                 elif choice == '4':
                     print("Выход из режима управления.")
                     break

                 else:
                     print("Неверный выбор. Пожалуйста, попробуйте снова.")

     def main():
         machine = CoffeeMachine()
         control_mode = ControlMode(machine)
         control_mode.run()

     if __name__ == "__main__":
         main()
     


