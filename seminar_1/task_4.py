# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def place(number):
    if number == 1:
        return 'x > 0 and y > 0'
    elif number == 2:
        return 'x < 0 and y > 0'
    elif number == 3:
        return 'x < 0 and y < 0'
    elif number == 4:
        return 'x > 0 and y < 0'

print('Определим возможные значения X и Y:')
number = int(input('Введите номер четверти: '))
print(f'Возможные значения в четверти {number}: {place(number)}')