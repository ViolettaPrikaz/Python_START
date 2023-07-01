"""
Выведите список простых множителей натурального числа N.

#Ввод: значение типа <int>
#Вывод: значение типа <list>

#Примеры:
#20
#[2, 2, 5]

#38
#[2, 19]
"""

N = int(input("Введите натуральное число: "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

factors = []
for i in range(2, N+1):
    if N % i == 0 and is_prime(i):
        factors.append(i)
print("список простых множителей натурального числа", N, "-", factors)