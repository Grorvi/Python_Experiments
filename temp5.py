#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random
coins = int(input())
coins_1 = 0
coins_2 = 0
coins_min = 0
for i in range(coins):
    coins_1 += random.randint(-10, 10)
    if coins_1 > 0:
        coins_2 += 1
    else:
        coins_1 = 0
        print(coins_1)
if coins_1 > coins_min:
    coins_min = coins_1
print(coins_min)


