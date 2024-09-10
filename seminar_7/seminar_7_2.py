# Задача №3. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод: 
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values): 
#     print(‘same’) 
# else: 
#     print(‘different’)
          
# Вывод: same     
 
def same_by(characteristic, objects):
    resalt = 0
    for item in objects:
        if item is characteristic:
            resalt += 1
            print(resalt)
    return resalt

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values): 
    print(same_by) 
    print('same') 
else: 
    print(same_by)
    print('different')
