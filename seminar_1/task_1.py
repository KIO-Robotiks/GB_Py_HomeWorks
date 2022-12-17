# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def week(number):

    try:
        number = int(number)
    except:
        return "Это не число."
    if number < 1 or number > 7:
        return "Такого дня недели нет."
    elif number > 0 and number < 6:
        return "нет"
    else:
        return "Да"

print('Узнаем выходной ли день ...')
number = input('Ведите номер дня недели: ')
print(week(number))
