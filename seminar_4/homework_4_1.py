# Задание 1. Три списка 
# Даны три списка. 
# array_1 = [1, 5, 10, 20, 40, 80, 100] 
# array_2 = [6, 7, 20, 80, 100] 
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120] 

# Нужно выполнить две задачи: 
# 1. найти элементы, которые есть в каждом списке; 
# 2. найти элементы из первого списка, которых нет во втором и третьем списках. 

# Каждую задачу нужно выполнить двумя способами: 
# 1. без использования множеств; 
# 2. с использованием множеств.

array_1 = [1, 5, 10, 20, 40, 80, 100] 
array_2 = [6, 7, 20, 80, 100] 
array_3 = [3, 4, 15, 20, 30, 70, 80, 120] 

print("Задача 1:") 
# Решение без мно"жеств:
def get_general_elem():
    merge_array = array_1 + array_2 + array_3
    result = []
    for number in merge_array:
        if merge_array.count(number) == 3:
            if number not in result:
                result.append(number)
    return result         
print("Решение без множеств: ", get_general_elem())
# Решение с множествами:
result = set(array_1) & set(array_2) & set(array_3)
print("Решение с использованием множеств: ", result)


print("Задача 2:") 
# Решение без множеств:
def get_notinclud_elem():
    result = []
    for number in array_1:
        if number not in (array_2 or array_3):
            result.append(number)
    return result         
print("Решение без множеств: ", get_notinclud_elem())

# Решение с множествами:
result2 = set(array_1) - set(array_2) - set(array_3)
print("Решение с использованием множеств: ", result2)