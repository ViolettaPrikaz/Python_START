"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""



import random

size = int(input('Введите размер списка: '))

new_list = [round(random.uniform(1, 99), 2) for _ in range(size)]
dec_list = [int(str(x).split('.')[-1].ljust(2, '0')) for x in new_list]

print(new_list)
print(max(dec_list) - min(dec_list))
