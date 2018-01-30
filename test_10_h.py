import random

def pretty_print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print('%d' % elem, end='\t')
        print()
    print()

def rotate_matrix(matrix):
    rotated_matrix = [list(i) for i in zip(*matrix[::-1])]
    return rotated_matrix

matrix_columns = 5
matrix_rows = 3
low_bound = -10
hight_bound = abs(low_bound)
coordinat_list = 0

matrix = [[random.randint(low_bound, hight_bound) for i in range(matrix_columns)] \
          for ii in range(matrix_rows)]

matrix_test = [[5, 6, 4, 4],
               [-2, 5, 3, 7],
               [8, 7, -2, 6]]

matrix_test_2 = [[3, 8, 7],
                 [5, 9, 6],
                 [2, 6, 7]]

matrix_test_3 = [[2, 3, 5, 2],
                 [2, 4, 6, 2],
                 [-2, 7, 2, 0]]


pretty_print_matrix(matrix)
rotated_matrix = rotate_matrix(matrix)

for ind, rows in enumerate(matrix):
    min_var = int(min(rows))

    for rotated_ind, rotated_rows in enumerate(rotated_matrix):
        max_var = int(max(rotated_rows))

        if max_var == min_var:
            coordinat_list += 1

            print('Седловой элемент: %d \tКоординаты:' % max_var, end='\t')
            print('%d : %d  \t(строка : столбец)' % (ind+1, rotated_ind+1))

if coordinat_list == 0:
    print('Матрица не имеет cедловых элементов')
