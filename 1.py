"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""

def calculate(expression):
    
    expression = expression.replace('-', '+-')
    
    terms = expression.split('+')
    total = 0
    for term in terms:
        if '*' in term:
            factors = term.split('*')
            product = 1
            for factor in factors:
                product *= float(factor)
            total += product
        elif '/' in term:
            factors = term.split('/')
            quotient = float(factors[0])
            for factor in factors[1:]:
                quotient /= float(factor)
            total += quotient
        else:
            total += float(term)
    return total

def simplify_parentheses(expression):
    
    while True:
        
        start = expression.rfind('(')
        if start == -1:
            break
        end = expression.find(')', start)
        if end == -1:
            raise ValueError("Недопустимое выражение: несовпадающие круглые скобки")
        
        inner_expression = expression[start+1:end]
        value = calculate(inner_expression)
        expression = expression[:start] + str(value) + expression[end+1:]
    return expression

string_ = input("Введите математическое выражение: ")
try:
    expression = simplify_parentheses(string_)
    result = calculate(expression)
    print(f"{string_} = {result}")
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {str(e)}")