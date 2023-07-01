
"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""


import random

num = int(input('Введите количество рандомных чисел: '))

rnd_list = []
for i in range(num):
    rnd_list.append(random.randint(0, num-1))
print(rnd_list)

list_1 = []
list_2 = []
list_3 = list(set(rnd_list)) 
for n in rnd_list:
    if rnd_list.count(n) == 1:
        list_1.append(n)
    else:
        if list_2.count(n) == 0:
            list_2.append(n)
print("список чисел, которые не повторяются в заданном списке")
print(list_1)
print("список повторяемых чисел")
print(list_2)
print("список без повторений")
print(list_3)


