"""
Задача 1

Напишите функцию для транспонирования матрицы
"""


def transpose(matrix):

    return [list(row) for row in zip(*matrix)]


original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed_matrix = transpose(original_matrix)
for row in transposed_matrix:
    print(row)
