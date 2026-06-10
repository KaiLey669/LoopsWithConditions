num_sum = 0
for num in range(1, 101):
    if num % 2 == 0:
        num_sum += num

squares = [num ** 2 for num in range(1, 11) if num % 2 != 0]

print(f"Сумма всех нечетных числе от 1 до 100: {num_sum}")
print(f"Список квадратов нечетных чисел от 1 до 10 - {squares}")

nums_count = 0
input_num = 0
while input_num >= 0:
    try:
        input_num = float(input("Введите число: "))
    except ValueError:
        print("Введено не число.")
        continue
    nums_count += 1

print(f"Количество введенных чисел - {nums_count}")
print("Введено отрицательное число. Завершение работы программы.")
