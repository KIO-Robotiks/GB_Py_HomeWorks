# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
import random

x = random.random()
y = random.random()
z = random.random()

print(x,y,z)


if (not(x or y or z)) == (not x and not y and not z):
    print ('Yes')
else:
    print('No')