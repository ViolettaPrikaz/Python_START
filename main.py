import sqlite3


def create_employees_table(conn):
    
    c = conn.cursor()
    c.execute('''CREATE TABLE employees
                 (id INTEGER PRIMARY KEY,
                  first_name TEXT,
                  last_name TEXT,
                  position TEXT,
                  salary REAL,
                  department_id INTEGER,
                  FOREIGN KEY (department_id) REFERENCES departments(id))''')


def create_departments_table(conn):
  
    c = conn.cursor()
    c.execute('''CREATE TABLE departments
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  num_employees INTEGER)''')


def add_employee(conn):
    
    first_name = input("Введите имя сотрудника: ")
    last_name = input("Введите фамилию сотрудника: ")
    position = input("Введите должность сотрудника: ")
    salary = float(input("Введите зарплату сотрудника: "))
    department_id = int(input("Введите ID отдела, в котором работает сотрудник: "))

    c = conn.cursor()
    c.execute("INSERT INTO employees (first_name, last_name, position, salary, department_id) VALUES (?, ?, ?, ?, ?)",
              (first_name, last_name, position, salary, department_id))
    conn.commit()
    print("Сотрудник успешно добавлен")


def add_department(conn):
   
    name = input("Введите название отдела: ")
    num_employees = int(input("Введите количество сотрудников в отделе: "))

    c = conn.cursor()
    c.execute("INSERT INTO departments (name, num_employees) VALUES (?, ?)", (name, num_employees))
    conn.commit()
    print("Отдел успешно добавлен")


def edit_employee(conn):
    
    employee_id = int(input("Введите ID сотрудника для редактирования: "))
    c = conn.cursor()
    c.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
    employee = c.fetchone()

    if employee is not None:
        print("Текущая информация о сотруднике:")
        print(employee)
        first_name = input("Введите имя сотрудника: ")
        last_name = input("Введите фамилию сотрудника: ")
        position = input("Введите должность сотрудника: ")
        salary = float(input("Введите зарплату сотрудника: "))
        department_id = int(input("Введите ID отдела, в котором работает сотрудник: "))

        c.execute("UPDATE employees SET first_name=?, last_name=?, position=?, salary=?, department_id=? WHERE id=?",
                  (first_name, last_name, position, salary, department_id, employee_id))
        conn.commit()
        print("Данные о сотруднике успешно обновлены")
    else:
        print("Сотрудник с таким ID не найден")


def edit_department(conn):
    
    department_id = int(input("Введите ID отдела для редактирования: "))
    c = conn.cursor()
    c.execute("SELECT * FROM departments WHERE id=?", (department_id,))
    department = c.fetchone()

    if department is not None:
        print("Текущая информация об отделе:")
        print(department)
        name = input("Введите название отдела: ")
        num_employees = int(input("Введите количество сотрудников в отделе: "))

        c = conn.cursor()
        c.execute("UPDATE departments SET name=?, num_employees=? WHERE id=?",
                  (name, num_employees, department_id))
        conn.commit()
        print("Данные об отделе успешно обновлены")
    else:
        print("Отдел с таким ID не найден")


def delete_employee(conn):
   
    employee_id = int(input("Введите ID сотрудника для удаления: "))
    c = conn.cursor()
    c.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
    employee = c.fetchone()

    if employee is not None:
        c.execute("DELETE FROM employees WHERE id=?", (employee_id,))
        conn.commit()
        print("Сотрудник успешно удален")
    else:
        print("Сотрудник с таким ID не найден")


def delete_department(conn):
    
    department_id = int(input("Введите ID отдела для удаления: "))
    c = conn.cursor()
    c.execute("SELECT * FROM departments WHERE id=?", (department_id,))
    department = c.fetchone()

    if department is not None:
        c.execute("DELETE FROM departments WHERE id=?", (department_id,))
        conn.commit()
        print("Отдел успешно удален")
    else:
        print("Отдел с таким ID не найден")


def show_employees(conn):
   
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    employees = c.fetchall()

    if len(employees) > 0:
        for employee in employees:
            print(employee)
    else:
        print("Нет сотрудников в базе данных")


def show_departments(conn):
  
    c = conn.cursor()
    c.execute("SELECT * FROM departments")
    departments = c.fetchall()

    if len(departments) > 0:
        for department in departments:
            print(department)
    else:
        print("Нет отделов в базе данных")


def save_database(conn):
    
    file_name = input("Введите имя файла для сохранения: ")
    with open(file_name, 'w') as f:
        for line in conn.iterdump():
            f.write(f"{line}\n")
    print(f"База данных успешно сохранена в файл {file_name}")


def load_database(conn):
   
    file_name = input("Введите имя файла для загрузки: ")
    with open(file_name, 'r') as f:
        sql_script = f.read()
        conn.executescript(sql_script)
    print(f"База данных успешно загружена из файла {file_name}")


def main():
    conn = sqlite3.connect('com.db')
    create_employees_table(conn)
    create_departments_table(conn)

    while True:
        print("1. Добавить сотрудника")
        print("2. Редактировать данные о сотруднике")
        print("3. Удалить сотрудника")
        print("4. Показать список сотрудников")
        print("5. Добавить отдел")
        print("6. Редактировать данные об отделе")
        print("7. Удалить отдел")
        print("8. Показать список отделов")
        print("9. Сохранить базу данных в файл")
        print("10. Загрузить базу данных из файла")
        print("11. Выход")

        choice = input("Выберите действие: ")
        if choice == '1':
            add_employee(conn)
        elif choice == '2':
            edit_employee(conn)
        elif choice == '3':
            delete_employee(conn)
        elif choice == '4':
            show_employees(conn)
        elif choice == '5':
            add_department(conn)
        elif choice == '6':
            edit_department(conn)
        elif choice == '7':
            delete_department(conn)
        elif choice == '8':
            show_departments(conn)
        elif choice == '9':
            save_database(conn)
        elif choice == '10':
            load_database(conn)
        elif choice == '11':
            break
        else:
            print("Неверный выбор")


if __name__ == '__main__':
    main()