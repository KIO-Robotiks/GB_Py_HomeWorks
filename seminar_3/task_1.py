# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from common import get_random_list

my_list = get_random_list(6, 100, 'int')

print(f'Наш список: {my_list}')

sum = 0
for _ in my_list:
    if my_list.index(_)%2 != 0:
        sum += _

print(f'Сумма элементов на нечётных позициях = {sum}')
