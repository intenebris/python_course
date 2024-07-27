# Задача №2. Решение в группах 
# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1. 
# Input:     5 
# Output:  6

num = int(input('Введите натуральное число: '))

fibFirst = -1
fibSecond = 1
fibSum = 0
i = 1

while (i <= num + 3):
    fibSum = fibFirst + fibSecond
    if (fibSum == num):
        print('Число ', num, ' по счету ', i)
        break
    elif (i == (num + 3)):
        print('-1')    
    fibFirst = fibSecond
    fibSecond = fibSum
    i += 1
