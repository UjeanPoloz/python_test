import random

def get_max_min_digit(number):
    return int(max(number)), int(min(number))

list = []

for i in range(0,10):
    list.append(random.randint(-100,100))

print('Задан список: \n\t', list)

max_var, min_var = get_max_min_digit(list)

print('\nМаксимальное число: %d\nМинимальное число: %d' % (max_var, min_var))

# for i, var_first in enumerate(list):
#     if var_first == max_var:
#         for ii, var_second in enumerate(list):
#             if var_second == min_var:
#                 list[i] = min_var
#                 list[ii] = max_var
#                 break
#         break

list[list.index(max_var)] = min_var
list[list.index(min_var)] = max_var

print('\nМодифицированный список: \n\t', list)
