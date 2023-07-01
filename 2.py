"""
Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""


def factorials(N):
    result = []
    for i in range(1, N+1):
        factorial = 1
        for j in range(1, i+1):
            factorial *= j
        result.append(factorial)
    return result

N = int(input("Введите натуральное число N: "))
print(factorials(N))
