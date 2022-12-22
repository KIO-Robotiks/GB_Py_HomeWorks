# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number_start = 2
number = number_start
x = []

while number > 0:
    x.insert(0, number % 2)
    number = number // 2

print(f'Число {number_start} в двоичной системе = ', *x)

