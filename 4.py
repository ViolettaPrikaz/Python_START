

"""
Написать программу по переводу целого числа из десятичной системы счисления в двоичную.

Ввод: значение типа <int>
Вывод: значение типа <int>

Примеры:
45
101101

3
11

2
10
"""




num = int(input('Введите целое число:'))
binary_num = bin(num)
print('"0b"- числовое значение является двоичным')
print(binary_num)


