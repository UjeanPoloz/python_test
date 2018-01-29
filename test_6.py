import re

var_input = input("Введите строку для работы с ней: ")

user_str = re.sub(r'[\s]','', var_input)
ind = 0
duplications = False

for ind, letter in enumerate(user_str):
    for j in range(ind+1, len(user_str)):
        if letter == user_str[j]:
            duplications = True

    if duplications:
        print('\nСтрока не изограмма')
        break

if not duplications:
    print('\nСтрока изограмма')