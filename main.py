def get_sum_even_numbers(start: int, end: int) -> int:
    num_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            num_sum += num

    return num_sum

def get_squares(start: int, end: int) -> list:
    return [num ** 2 for num in range(start, end + 1) if num % 2 != 0]

def get_numbers_count():
    nums_count = 0
    input_num = 0
    while input_num >= 0:
        try:
            input_num = float(input("Введите число: "))
        except ValueError:
            print("Введено не число.")
            continue
        nums_count += 1

    return nums_count


num_sum = get_sum_even_numbers(1, 101)
print(f"Сумма всех нечетных чисел от 1 до 100: {num_sum}")

squares = get_squares(1, 11)
print(f"Список квадратов нечетных чисел от 1 до 10 - {squares}")

nums_count = get_numbers_count()
print(f"Количество введенных чисел - {nums_count}")
print("Введено отрицательное число. Завершение работы программы.")
