import re

def is_isogram(str_var):
    user_str = re.sub(r'[\s]', '', var_input)
    ind = 0

    for ind, letter in enumerate(user_str):
        for j in range(ind + 1, len(user_str)):

            if letter == user_str[j]:
                return False

    return True

var_input = input("Введите строку для работы с ней: ")

if is_isogram(var_input):
    print('Строка изограмма')
else:
    print('Строка не изограмма')