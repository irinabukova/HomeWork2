# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# Стороны монеты вводятся построчно или в одну строку, если умеете.
# Пример
# Ввод: 1 1 0 0 0 -> Вывод: 2
import random

n = int(input('Введите количество монет: '))
my_list = []
def fill(n:int, new_list: list):
    # global my_list
    new_list = []
    for i in range(n):
        my_list.append(random.randint(0,1))
    return new_list

fill(n, my_list)
print(*my_list)

count1 = 0
count0 = 0
for i in range(len(my_list)):  #Почему если вставляю функцию fill(n) перестает работать
    if my_list[i] > 0:
        count1 += 1
    else:
        count0 +=1
# print(count1, count0)

if count1 > count0:
    print(f'Нужно перевернуть {count0} монеты')
else:
    print(f'Нужно перевернуть {count1} монеты')