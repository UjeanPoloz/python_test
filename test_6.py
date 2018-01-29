import re

def my_input():
    while True:
        try:
            var = str(input("Введите строку для работы с ней: "))
        except ValueError:
            print("Алгоритм принимает только строки!\n")
        else:
            break
    return var

user_str = re.sub(r'[\s]','', my_input())
ind = 0
concurrences = False

for ind, letter in enumerate(user_str):
    for j in range(ind+1, len(user_str)):
        if letter == user_str[j]:
            concurrences = True

if concurrences:
    print('\nСтрока не изограмма')
else:
    print('\nСтрока изограмма')