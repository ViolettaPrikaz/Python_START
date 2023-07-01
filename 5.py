"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
8
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""



N = int(input("Задайте целое число N: "))

a, b = 0, 1

if N == 0:
    sequence = [0]
elif N == 1:
    sequence = [0, 1, -1]
else:
    sequence = [0, 1, -1]
    for i in range(2, N+1):
        c = a - b
        
        sequence.append(c)
        sequence.append(b)
        sequence.append(-a)
        
        a, b = b, c
    
print(sequence)