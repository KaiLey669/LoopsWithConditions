num_sum = 0

for num in range(1, 101):
    if num % 2 == 0:
        num_sum += num

squares = [num ** 2 for num in range(1, 11) if num % 2 != 0]

print(f"Сумма всех нечетных числе от 1 до 100: {num_sum}")
print(f"Список квадратов нечетных чисел от 1 до 10 - f{squares}")

nums_count = 0
while True:
    try:
        input_num = float(input("Введите отрицательное число: "))
    except ValueError:
        print("Введено не число.")
        continue

    nums_count += 1
    if input_num < 0:
        print(f"Количество введенных чисел - {nums_count}")
        print("Введено отрицательное число. Завершение работы программы.")

        break
    else:
        print("Введено не отрицательное число. Повторите попытку.")
