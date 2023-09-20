import math

print("Инженерный калькулятор")
while True:
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("0. Выход")

    choice = input("Введите номер операции: ")

    if choice == "0":
        print("Выход из калькулятора.")
        break

    try:
        num1 = float(input("Введите первое число: "))
        if choice not in ("6", "7", "8", "9", "10"):
            num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка ввода! Пожалуйста, введите числа.")
        continue

    if choice == "1": result = num1 + num2
    elif choice == "2": result = num1 - num2
    elif choice == "3": result = num1 * num2
    elif choice == "4":
        if num2 == 0: print("Ошибка: Деление на ноль!"); continue
        result = num1 / num2
    elif choice == "5": result = num1 ** num2
    elif choice == "6":
        if num1 < 0: print("Ошибка: Квадратный корень отрицательного числа!"); continue
        result = math.sqrt(num1)
    elif choice == "7":
        if num1 < 0: print("Ошибка: Факториал отрицательного числа!"); continue
        result = 1
        for i in range(1, int(num1) + 1): result *= i
    elif choice == "8": result = math.sin(num1)
    elif choice == "9": result = math.cos(num1)
    elif choice == "10": result = math.tan(num1)
    else:
        print("Неправильный выбор операции. Пожалуйста, выберите снова.")
        continue

    print(f"Результат: {result}")