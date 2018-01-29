import random

list = []

for i in range(0,10):
    list.append(random.randint(-100,100))

rating_var_max = max(list)
rating_var_min = min(list)

if rating_var_max > abs(rating_var_min):
    rating_var = rating_var_max
else:
    rating_var = abs(rating_var_min)

print('Задан список: \n\t', list)

for i, list_var in enumerate(list):
    if abs(list[i]) == rating_var or list[i] == 0:
        list[i] = int(list_var / rating_var)
    else:
        list[i] = float("{0:.3f}".format(list_var / rating_var))

print('\nНормированный список по числу %d: \n\t' % rating_var, list)
