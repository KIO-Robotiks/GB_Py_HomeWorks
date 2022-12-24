# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from common import get_random_list

my_list = get_random_list(5, 20, 'real')

# my_list = [1.1, 1.2, 3.1, 5, 10.01]  # Для проверки примера из задачи

print(f'Наш список: {my_list}')

my_list_2 = []

for i in my_list:
    x = i % 1
    if x > 0:
        x = round(x, 3)
        my_list_2.append(x)

my_max = my_list_2[0]
my_min = my_list_2[0]

for i in my_list_2:
    if i > my_max:
        my_max = i
    if i < my_min:
        my_min = i

print(f'Искомая разница = {round(my_max - my_min, 2)}')