# Задача №2. Общее обсуждение Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные. 
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1

grades = [1, 3, 4, 3, 4, 5]

def change_grades(lst):
    if 4 in lst:
        lst[lst.index(4)] = 1
        return change_grades(lst)
    elif 5 in lst:  
        lst[lst.index(5)] = 1
        return change_grades(lst)
    else:
        return lst

print(f"Ложные оценки Василия {grades}")
print(f"Исправленные оценки {change_grades(grades)}")