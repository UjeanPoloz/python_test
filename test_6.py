import re

def is_isogram(str_var):
    user_str = re.sub(r'[\s]', '', var_input)
    ind = 0

    for ind, letter in enumerate(user_str):
            if letter in user_str[ind+1:]:
                return False

    return True

var_input = input("Введите строку для работы с ней: ")

if is_isogram(var_input):
    print('Строка изограмма')
else:
    print('Строка не изограмма')