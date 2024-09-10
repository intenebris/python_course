# # def calc_all(x):
# #     def calc_square(y):
# #         return y**x
# #     return calc_square

# # # print(calc_all(2)(5))

# # calc_cube = calc_all(3)
# # calc_sq = calc_all(2)

# # print(calc_cube(11))
# # print(calc_sq(11))

# calc = {
#     '+': lambda x,y: x + y,
#     '-': lambda x,y: x - y,
#     '*': lambda x,y: x * y,
#     '/': lambda x,y: x / y
#         }

# enter_date = input('Введите арифметическое выражение:')
# num1, op, num2 = enter_date.split()
# print(calc[op](int(num1),int(num2)))

# Задача №2. Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод: 
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
# print(*find_farthest_orbit(orbits)) 
# Вывод: 
# 2

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
    area_ellipses = list(map(lambda x: 3.14*x[0]*x[1] if x[0] != x[1] else 0, orbits))
    farthest_orbit = 0
    for z in area_ellipses:
        if z == max(area_ellipses):
            farthest_orbit = area_ellipses.index(z) + 1
    return farthest_orbit

    

print(find_farthest_orbit(orbits))
