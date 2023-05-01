# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k),
# не превосходящие числа N.
# Пример
# Ввод: 17 -> Вывод: 1, 2, 4, 8, 16

def num ():
    while True:
        try:
            global n
            n = int(input('Введите число: '))
            if n == int(n):
                return n
        except:
            print('Это не число: ')
def degree ():
    k = 1
    my_list = []
    for i in range(n):
        if k < n:
            my_list.append(k)
            k *= 2
    return my_list


print(f'Ввод: {num()} -> Вывод: ', *degree())

# k = 1
# while k < n:
#     print(k, end=' ')
#     k *= 2

