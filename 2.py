"""Докажите, что выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат.
Вывод: единственное значение типа bool (True либо False)
"""



X = bool(input("Введите значение X (True или False): "))
Y = bool(input("Введите значение Y (True или False): "))
Z = bool(input("Введите значение Z (True или False): "))

result_left = not (X or Y or Z)
result_right = not X and not Y and not Z

if result_left == result_right == True:
    print("True")
else:
    print("False")