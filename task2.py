# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

def operation(a, b): # функция премножения аргументов
    return a*b
def print_operation_table(operation, num_rows, num_columns): # функция вывода на экран результатов функции opertion
    for i in range(1, num_rows+1):                           # в заданном диапазоне строк и столбцов
        for j in range(1,num_columns+1):
            print(operation(i,j), end='  ')
        print()
print_operation_table(operation, 6, 6)

