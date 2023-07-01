"""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.

Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.

Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""
with open('1polynomial.txt', 'r') as f1, open('2polynomial.txt', 'r') as f2:
    polynomial1 = f1.readline().strip()  
    polynomial2 = f2.readline().strip()  

sum_polynomial = add_polynomials(polynomial1, polynomial2)

print('Сумма многочленов:')
print(sum_polynomial)

with open('sum_polynomial.txt', 'w') as f:
    f.write(sum_polynomial)