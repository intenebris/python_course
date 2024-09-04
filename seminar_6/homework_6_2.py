# Задача 2: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random as rnd

min_value = int(input("Введите min: "))
max_value = int(input("Введите max: "))
ln = 20

arr = [rnd.randint(-20,20) for _ in range(ln)]
print(arr)

def find_index_array(arr, min, max):
    result = []
    for i in range(len(arr)):
        if arr[i] > min and arr[i] < max:
            result.append(i)
    return result        

print(find_index_array(arr, min_value, max_value))