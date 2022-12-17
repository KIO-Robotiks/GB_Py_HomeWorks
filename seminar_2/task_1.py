# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def sum(number):

    try:
        number = float(number)
        number = str(number)
    except:
        return "Это не число."

    sum = 0
    non_list = ['.', '-']
    for i in number:
        if i not in non_list:
            sum += int(i)
    return sum

print('Узнаем сумму цифр вещественного числа ...')
number = input('Ведите число: ')
print(f'Сумма чисел = {sum(number)}')

