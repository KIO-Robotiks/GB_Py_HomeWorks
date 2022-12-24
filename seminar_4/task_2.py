# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('mnogochlen_1', 'r') as file_a:
    m1 = file_a.read()

with open('mnogochlen_2', 'r') as file_b:
    m2 = file_b.read()

print(m1)
print(m2)    

m1 = m1.split(' + ')
m2 = m2.split(' + ')

m_dict = {}

#Добавляем в словарь значения многочлена 1
for i in m1:
    if 'x**' in i:
        key = i[i.find('x'):]
        try:
            value = int(i[0:i.find('x')])
        except:
            value = 1
    elif 'x' in i:
        key = 'x'
        try:
            value = int(i[0:i.find('x')])
        except:
            value = 1
    else:
        key = 0
        value = int(i)
    m_dict[key] = value


# Прибавляем к словарю значения многочлена 2
for i in m2:
    if 'x**' in i:
        key = i[i.find('x'):]
        try:
            value = int(i[0:i.find('x')])
        except:
            value = 1
    elif 'x' in i:
        key = 'x'
        try:
            value = int(i[0:i.find('x')])
        except:
            value = 1
    else:
        key = 0
        value = int(i)
    if key in m_dict:
        m_dict[key] += value
    else:
        m_dict[key] = value

# Удаляем коэффициенты == 1
for key in m_dict:
    if m_dict[key] == 1:
        m_dict[key] = ''

# Превращаем в строку
m_string = ''

for key in m_dict:
    if key != 0:
        m_string += str(m_dict[key]) + str(key) + ' + '
    else:
        m_string += str(m_dict[key]) + ' + '
m_string = m_string.rstrip(' +')

print(m_string)

# Записываем в файл
with open('task_2_result', 'w') as file_result:
    file_result.write(m_string)
