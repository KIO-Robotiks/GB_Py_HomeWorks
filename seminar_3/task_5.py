# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

k = 10

# Определение чисел из Википедии:
list_f = [0, 1]        # F(0) = 0, F(1) = 1, Fn = F(n-1)+F(n-2)    need add (k-2) numbers
list_un_f = [1, -1]    # F(−1) = 1, F(−2) = -1, Fn = F(n-2)−F(n-1) need add (k-1) numbers

count = 2
for i in range(k-1):
    list_f.append(list_f[count-1] + list_f[count-2])
    count += 1

count = 2
for i in range(k-2):
    list_un_f.append(list_un_f[count-2] - list_un_f[count-1])
    count += 1

list_real_un_f = []
for i in list_un_f:
    list_real_un_f.insert(0, i)

result_list = list_real_un_f + list_f

print(result_list)
