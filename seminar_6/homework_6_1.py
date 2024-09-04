# Задача 1:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

# Ввод: 7 2 5 
# Вывод: 7 9 11 13 15

first_elem = int(input("Введите первый элемент: "))
dif = int(input("Введите разность: "))
lng_arr = int(input("Введите количество элементов: "))


def create_array(el, df, ln):
    arr = [el]
    elems = el
    for i in range(ln-1):
        elems = elems + df
        arr.append(elems)
    return arr    

print(create_array(first_elem, dif, lng_arr))