# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и,
# при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# 1 2 1 4 3 5 6
# +1+1 = 2


import random
count = 0

a_1 = int(input("Введите размер массива "))

mass_1 = []
for el_2 in range(a_1):
    mass_1.append(random.randint(-10, 10))
print(mass_1)

for i in range(1, len(mass_1)-1):
    if mass_1[i-1] < mass_1[i] > mass_1[i + 1]:
        count += 1

print(count)