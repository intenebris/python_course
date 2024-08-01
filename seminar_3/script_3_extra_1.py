# Задача 1 НЕГАФИБОНАЧЧИ 
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 9 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]​

k = int(input('Введите число: '))
# k = 9
f = 0
arr = []
mirror_arr = []
result_arr = []
i = 0

while i < k:
    if i == 0:
      arr.insert(i, f)
      f += 1
      i += 1
    else:
       arr.insert(i, f)
       f = arr[i-1] + arr[i]
       i += 1

for i in range(len(arr)):
   if i == 0:
      mirror_arr.insert(i, 0)
   else:
      mirror_arr.insert(i, -arr[-i])

del mirror_arr[0]
mirror_arr.extend(arr)

print(mirror_arr)
