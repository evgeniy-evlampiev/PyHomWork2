# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

from random import randint

amount_coin = int(input('введите кол-во монет: '))

m = 0 # кол-во решек
k = 0 # кол-во орлов (гербов)
coins = [0, 1]
for i in range(amount_coin):
    random.shuffle(coins)
    print(f'Монета {coins}')
    if int(coins[0]) == 0:
        k += 1
    if int(coins[0]) == 1:
        m += 1
print(f'Всего:  решек {m}   орлов {k}')

if m > k:
    ans = k
else:
    ans = m

print(f"Минимальное кол-во монет, которые нужно перевернуть {ans}")
