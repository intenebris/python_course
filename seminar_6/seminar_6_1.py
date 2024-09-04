# import random

# sp = []

# for _ in range(5):
#     sp.append(random.randint(-100,100))

# print(sp)

# print(sp := [random.randint(-10,10) for _ in range(10)])
# print(*sp)

# sp = [random.randint(1,10) for _ in range(10)]
# qua = [el ** 2 for el in sp]

# print(*sp)
# print(*qua)

# sp = [random.randint(1,10) for _ in range(10)]
# print(*sp)
# # возвести в квадрат только нечетные числа
# print(*[el ** 2 for el in sp if el % 2])

# возвести в квадрат только нечетные числа, а четные обнулим

# print(*[el ** 2 if el % 2 else 0 for el in sp])

# sp = [random.randint(1,10) for _ in range(10)]

# dic = {int(i):sp[i] for i in range(len(sp))}
# print(sp)
# print(dic)
# print({el % 2 for el in sp})

# Задача №1. Даны два массива чисел. 
# Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго.

import random

len_arr1 = int(input("Введите размер первого массива: "))
len_arr2 = int(input("Введите размер второго массива: "))

arr1 = [random.randint(1,10) for _ in range(len_arr1)]
arr2 = [random.randint(1,10) for _ in range(len_arr2)]
resault_arr = [el for el in arr1 if el not in arr2]

print(arr1)
print(arr2)
print(f"элементы первого массива, которых нет во втором массиве: {resault_arr}")