# Задача 2 Последовательность необязательная
# Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8

arr = [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ]
new_arr = []
max_size = 0
min_value = 0
max_value = 0
for i in range(len(arr)):
    if arr[i] + 1 in arr:
        new_arr.append(arr[i])
        print(new_arr)
        if max_size < len(new_arr):
            max_size = len(new_arr)
            min_value = min(new_arr)
            max_value = max(new_arr)
            print(f"size is {max_size}, min is {min_value}, max is {max_value}")
    else:
        new_arr.clear()
        print("clear")
new_arr.clear()
new_arr.append(min_value)
new_arr.append(max_value)
print(new_arr)        