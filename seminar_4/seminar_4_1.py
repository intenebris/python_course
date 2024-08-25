# Задача №1. Решение в группах 
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n. 
# Input: a a a b c a a d c d d 
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 
# Для решения данной задачи используйте функцию .split()

symbols = 'a a a b c a a d c d d'
lst = symbols.split()
new_lst = []
cntr = 1

for i in range(len(lst)):
    if lst[i] == lst[i - 1]:
        cntr = str(cntr)
        new_lst.append(lst[i] + '_'+ cntr)
        cntr = int(cntr)
        cntr += 1
    else:
        new_lst.append(lst[i])   



print(new_lst)