"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""



import random

num_items = int(input("Введите количество чисел в списке: "))

num_list = [random.randint(1, 10) for _ in range(num_items)]

print("Список чисел: ", num_list)

unique_nums = []
for num in num_list:
    if num_list.count(num) == 1 and num not in unique_nums:
        unique_nums.append(num)

if len(unique_nums) > 0:
    print("Список чисел, которые не повторяются: ", unique_nums)
else:
    print("В списке нет не повторяющихся чисел.")