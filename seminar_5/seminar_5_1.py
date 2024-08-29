# Задача №1. Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи 
# Input: 7 
# Output: 13 
# Задание необходимо решать через рекурсию

num = int(input("Введите число: "))

def find_fibonacci(num): #7
    if num <= 1:
        return num
    return (find_fibonacci(num-1) + find_fibonacci(num-2))


print(find_fibonacci(num))