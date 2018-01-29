import random

list = []

for i in range(0,10):
    list.append(random.randint(-100,100))

rating_var_max = max(list)
rating_var_min = min(list)

rating_var = abs(max(rating_var_min, rating_var_max, key=abs))

print('Задан список: \n\t', list)

for i, list_var in enumerate(list):
    if abs(list[i]) == rating_var or list[i] == 0:
        list[i] = int(list_var / rating_var)
    else:
        list[i] = round(list_var / rating_var, 3)

print('\nНормированный список по числу %d: \n\t' % rating_var, list)
