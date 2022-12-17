# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint

def create_list(n):       #Создаём рандомный лист
    
    my_list = []
    for i in range(n):
        my_list.append(randint(0,100))

    return my_list

def fog(some_list):      #Создаём перемешанный лис
    
    fog_list = []        #Будущий итоговый лист
    indexes_done = []    #Обработанные индексы начального массива 
    
    for i in range(len(some_list)):              
        index = randint(0,len(some_list)-1)
        if index not in indexes_done:              #Если индекс ещё не обработан, добавляем его эллемент и помечаем это
            indexes_done.append(index)
            fog_list.append(some_list[index])
        else:                                      #Если уже обработан, получаем тот, что точно ещё не обработан и делаем дело дельше...
            while index in indexes_done:
                index = randint(0,len(some_list)-1)
            indexes_done.append(index)
            fog_list.append(some_list[index])        
    
    return fog_list

print('Зададим список и перемешаем его..')
n = int(input('Введите кол-во элементов: '))

list1 = create_list(n)
print(f'Список: {list1}')

list2 = fog(list1)
print(f'Перемешанный список: {list2}')

