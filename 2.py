"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем n конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""

from random import randint

def in_data(name, take_once):
    total = int(input(f'{name}, сколько конфет ты возьмешь: (min = 1, max = {take_once}): '))
    while total < 1 or total > take_once:
        total = int(input(f'{name}, введите правильное количество конфет: '))
    return total

def print_data(name, n, counter, value):
    print(f'{name}  взял {n} конфет, съел {counter} конфеты. {value} конфеты, оставленные на столе')

player1 = input('Введите имя игрока 1:')
player2 = input('Введите имя игрока 2: ')
value = int(input('Введите количество конфет на столе:'))
flag = randint(0, 1)
if flag:
    print(f'{player1} ходит первым.')
else:
    print(f'{player2} ходит первым.')

counter1 = 0
counter2 = 0 
take_once = int(input('Введите количество конфет, которые можно взять за один ход:'))
while value > 0:
    if flag:
        n = in_data(player1, take_once)
        counter1 += n
        value -= n
        flag = False
        print_data(player1, n, counter1, value)
    else:
        n = in_data(player2, take_once)
        counter2 += n
        value -= n
        flag = True
        print_data(player2, n, counter2, value)

if flag:
    print(f'{player1} забрал/а все конфеты и стал/а победителем!')
else:
    print(f'{player2} забрал/а все конфеты и стал/а победителем!')