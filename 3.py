"""
Задать натуральное число k.
#Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
#Многочлен вывести в консоль и записать в файл.

#Ввод: значение типа <int>
#Вывод: значение типа <str>, файл с одной строкой.

#Пример:
#2
#2x^2 + 4x + 5 = 0
"""



import random

k = int(input("Введите степень многочлена: "))

coefficients = [random.randint(0, 100) for _ in range(k + 1)]

polynomial = ""
sum = 0
for i in range(k + 1):
    coefficient = coefficients[i]
    power = k - i
    if power == 0:
        polynomial += str(coefficient)
        sum += coefficient
    elif power == 1:
        polynomial += str(coefficient) + "x + "
        sum += coefficient
    else:
        polynomial += str(coefficient) + "x^" + str(power) + " + "
        sum += coefficient

print("Многочлен степени", k, "со случайными коэффициентами: ")
print(polynomial, "=", sum)

with open("polynomial.txt", "w") as file:
    file.write(polynomial)