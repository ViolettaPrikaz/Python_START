"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""


def del_word(text, sym):
    return " ".join(filter(lambda x: not any(y in x for y in sym) or all(y in x for y in sym), text.split()))

if __name__ == '__main__':
    print(del_word('любовь потеря влюбленность чувства', "абв"))
    print(del_word("ананас личи яблоко вишня", "абв"))
    
