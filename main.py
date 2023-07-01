import pandas as pd


def create_phonebook():
    return pd.DataFrame(columns=['id', 'имя', 'фамилия', 'день рождения', 'место работы', 'номер телефона'])


def add_entry(phonebook):
    entry_data = {}
    entry_data['id'] = len(phonebook) + 1
    entry_data['имя'] = input("Введите имя: ")
    entry_data['фамилия'] = input("Введите фамилию: ")
    entry_data['день рождения'] = input("Введите день рождения: ")
    entry_data['место работы'] = input("Введите место работы: ")
    entry_data['номер телефона'] = input("Введите номер телефона: ")
    
    new_entry = pd.DataFrame(entry_data, index=[0])
    phonebook = pd.concat([phonebook, new_entry], ignore_index=True)
    
    return phonebook


def remove_entry(phonebook):
    id = int(input("Введите id записи для удаления: "))
    phonebook = phonebook[phonebook['id'] != id]
    return phonebook


def edit_entry(phonebook):
    id = int(input("Введите id записи для редактирования: "))
    entry_index = phonebook.index[phonebook['id'] == id].tolist()[0]
    print("Старая запись:")
    print(phonebook.loc[entry_index])
    phonebook.at[entry_index, 'имя'] = input("Введите имя: ")
    phonebook.at[entry_index, 'фамилия'] = input("Введите фамилию: ")
    phonebook.at[entry_index, 'день рождения'] = input("Введите день рождения: ")
    phonebook.at[entry_index, 'место работы'] = input("Введите место работы: ")
    phonebook.at[entry_index, 'номер телефона'] = input("Введите номер телефона: ")
    return phonebook


def search_entry(phonebook):
    name = input("Введите имя или фамилию для поиска: ")
    result = phonebook[(phonebook['имя'].str.lower().str.contains(name.lower())) | (phonebook['фамилия'].str.lower().str.contains(name.lower()))]
    if len(result) > 0:
        print("Результаты поиска:")
        print(result)
    else:
        print("Записи не найдены")


def show_menu():
    print("1. Создать новый справочник")
    print("2. Добавить запись")
    print("3. Удалить запись")
    print("4. Отредактировать запись")
    print("5. Поиск записей")
    print("6. Вывести весь справочник")
    print("7. Сохранить справочник в файл")
    print("8. Загрузить справочник из файла")
    print("9. Выход")
    return input("Выберите действие: ")


def run_phonebook():
    phonebook = None

    while True:
        choice = show_menu()
        if choice == '1':
            phonebook = create_phonebook()
            print("Справочник успешно создан")
        elif choice == '2':
            if phonebook is not None:
                phonebook = add_entry(phonebook)
                print("Запись успешно добавлена")
            else:
                print("Сначала создайте справочник")
        elif choice == '3':
            if phonebook is not None:
                phonebook = remove_entry(phonebook)
                print("Запись успешно удалена")
            else:
                print("Сначала создайте справочник")
        elif choice == '4':
            if phonebook is not None:
                phonebook = edit_entry(phonebook)
                print("Запись успешно отредактирована")
            else:
                print("Сначала создайте справочник")
        elif choice == '5':
            if phonebook is not None:
               search_entry(phonebook)
            else:
                print("Сначала создайте справочник")
        elif choice == '6':
            if phonebook is not None:
                print(phonebook)
            else:
                print("Сначала создайте справочник")
        elif choice == '7':
            if phonebook is not None:
                file_name = 'phonebook.csv'
                phonebook.to_csv(file_name, index=False)
                print(f"Справочник успешно сохранен в файл {file_name}")
            else:
                print("Сначала создайте справочник")
        elif choice == '8':
            file_name = 'phonebook.csv'
            try:
                phonebook = pd.read_csv(file_name)
                print(f"Справочник успешно загружен из файла {file_name}")
            except FileNotFoundError:
                print(f"Файл {file_name} не найден")
        elif choice == '9':
            break
        else:
            print("Неправильный выбор")


run_phonebook()