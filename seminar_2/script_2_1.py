# Задача №1. Решение в группах 
# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while 
# Input: 5 
# Output: 120

num = int(input('Введите число: '))
counter = 1
sum = 1

if (num > 0):
    while (counter <= num):
        sum = sum * counter  
        counter += 1
    print(sum)
else:
    print('Вы ввели неправильное число.')
 