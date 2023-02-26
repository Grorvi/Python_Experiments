import random

number = int(input('Введите число: '))
my_list = []
desired_number = 0
for i in range(15):
    my_list.append(random.randint(1,101))
    min_d = max(my_list) - number

    if int(my_list[i]) == number:
        desired_number += 1
for i in set(my_list):
    if abs(i - number) < min_d:
        min_dmin_d = abs(i - number)
        closest_num = i
print(f'{desired_number} раз встречается в заданном списке число {number}')
print(f'список {my_list}')