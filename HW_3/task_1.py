"""
Задача 16: 
Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
Последняя строка содержит число X.
*Пример:*

5
    7 -2 3 5 1
    3
    -> 1
"""

from random import randint
nd = input('Введите количество цифр в массиве, диапазон массива от и до, искомое число через пробел: ').split()
n = int(nd[0])
d1 = int(nd[1])
d2 = int(nd[2])
x = int(nd[3])
list = [randint(d1, d2) for _ in range(n)]
print(list)
count = 0
for item in list:
    if item == x:
        count += 1
print(f'число {x} встречается в массиве {count} раз')