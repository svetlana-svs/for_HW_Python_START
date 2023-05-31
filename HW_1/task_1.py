"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

print('Введите трехзначное число: ')
m = int(input())

if m > 99 and m < 1000: # решение для положительных 3-значных чисел
    d1 = m // 100 # находим 1-ую цифру числа
    d2 = m // 10 % 10 # находим 2-ую цифру числа
    d3 = m % 10  # находим 3-ью цифру числа
    print(f'Сумма цифр числа {m} равна {d1 + d2 + d3} ({d1} + {d2} + {d3})')

elif m < -99 and m > -1000: # решение для отрицательных 3-значных чисел
    d1 = -m // 100 # находим 1-ую цифру числа
    d2 = -m // 10 % 10 # находим 2-ую цифру числа
    d3 = -m % 10  # находим 3-ью цифру числа
    print(f'Сумма цифр числа {m} равна {d1 + d2 + d3} ({d1} + {d2} + {d3})')

else : print('Вы ввели не трехзначное число')