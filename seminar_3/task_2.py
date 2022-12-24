# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from common import get_random_list

my_list = get_random_list(5, 100, 'int')

print(f'Наш список: {my_list}')

result_list = []

if len(my_list) % 2 == 0:
    size_of_result_list = int(len(my_list)/2)
else:
    size_of_result_list = len(my_list)//2 + 1

count = 0
for i in range(size_of_result_list):
    x = my_list[count] * my_list[len(my_list)-1 - count]
    result_list.append(x)
    count += 1

print(f'Результирующий список: {result_list}')
