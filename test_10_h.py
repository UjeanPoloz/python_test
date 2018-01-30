import random

def pretty_print_matrix(matrix, n=0):
    if n == 0:
        print('\n---Matrix---\n')
    else:
        print('\n---Sorted Matrix---\n')

    for row in matrix:
        for elem in row:
            print('%d' % elem, end='\t')
        print()
    print()

def rotate_matrix(matrix):
    rotated_matrix = list(zip(*matrix[::-1]))
    for ind in range(len(rotated_matrix)):
        rotated_matrix[ind] = list(rotated_matrix[ind])
    return rotated_matrix

def get_max_min_digit(number, n='all'):
    if n == 'all':
        return int(max(number)), int(min(number))
    if n == 'min':
        return int(min(number))
    if n == 'max':
        return int(max(number))


matrix_columns = 3
matrix_rows = 3
low_bound = -5
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
    min_var = get_max_min_digit(rows, n='min')

    for rotated_ind, rotated_rows in enumerate(rotated_matrix):
        max_var = get_max_min_digit(rotated_rows, n='max')

        if max_var == min_var:
            coordinat_list += 1

            print('Седловой элемент: %d \tКоординаты:' % max_var, end='\t')
            print('%d : %d  \t(строка : столбец)' % (ind+1, rotated_ind+1))

if coordinat_list == 0:
    print('Матрица не имеет cедловых элементов')
