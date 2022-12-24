# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from common import get_random_list

# Функция создания многочлена степени k и его записи в file_name
def mnogochlen(k, file_name):

    koefs = get_random_list(k + 1, 5, 'int')

    mnogochlen_tmp = ''

    for koef in koefs:
        if koef == 0:
            pass
        else:
            mnogochlen_tmp += f' + {koef}x**{k}'
        k -= 1

    mnogochlen = mnogochlen_tmp.replace('x**0', '').replace('x**1 ', 'x ').replace('1x', 'x')[3:]

    with open(file_name, 'w') as file:
        file.write(mnogochlen)

# Записываем файлы с многочленами
mnogochlen(3, 'mnogochlen_1')
mnogochlen(5, 'mnogochlen_2')
