# Задайте список из n чисел последовательности (1 + 1/n)^n,
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

def my_func(n):
    
    my_list = []
    sum = 0
    for i in range(n):
        x = (1 + 1/n)*n
        my_list.append(x)
        sum += x
    
    return str(my_list), sum

print('Зададим последовательность (1 + 1/n)^n получим сумму её элементов..')
n = int(input('Введите число n: '))
my_list, sum = my_func(n)
print(my_list)
print(f'Сумма её чисел = {sum}')
