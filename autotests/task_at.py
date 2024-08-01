"""
n = 100

def calculateSum(n):
    lng = str(n)
    sum = 0
    for i in range(len(lng)):
        sum = sum + int(lng[i])
    return sum    

res = calculateSum(n)

print(res)
"""

"""
n = 6 -> 1 4 1  
n = 24 -> 4 16 4    
n = 60 -> 10 40 10 

n = 60
p = int(n / 6)
s = p
k = 2 * (p + s)
print(f"{p} {k} {s}")
"""

"""
n = 385916 -> yes
n = 123456 -> no


n = 385916

def checkHuppyNumber(x):
    num = str(x)
    lng = len(num)
    firstSum = 0
    secondSum = 0
    for i in range(int(lng)):
        if i < int(lng / 2):
            firstSum = firstSum + int(num[i])
        else:
            secondSum = secondSum + int(num[i])       
    if  firstSum == secondSum:
        print('yes')
    else:
        print('no')    
       

checkHuppyNumber(n)
"""


"""
a, b, c = 3, 2, 4 -> yes
a, b, c = 3, 2, 1 -> no

a = 3
b = 5
c = 10

def isBreakChoco (a,b,c):
    if c % b == 0 or c % a == 0:
        print('yes')
    else:
        print('no')
        
isBreakChoco (a,b,c)
"""

"""
На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
coins = [0, 1, 0, 1, 1, 0]
На выходе:
3

coins = [1, 1, 1, 1, 0]
emblem = 0
tails = 0
i = 0
if len(coins) <= 1000:
    while i < len(coins):
        if coins[i] == 0:
            tails += 1   
        else:
            emblem += 1
        i += 1    
    if emblem < tails:
        print(emblem)
    else:
        print(tails)
"""


"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

Пример
На входе:
s = 12
p = 27
На выходе:
3 9


s = 12
p = 27
x = 0
y = 0

for x in range(1001):
    for y in range(1001):
        if x * y == p and x + y == s:
            if x <= y:
                print(f"{x} {y}")
                break
"""

"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
"""
"""
n = 3
i = 0
result = 0
while result <= n - result:
    result = 2**i
    print(result)
    i += 1
"""


"""
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# 1
list_1 = [1, 2, 3, 4, 5]
k = 3
counter = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        counter +=1
print(counter) 
"""       

"""
Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
list_1 = [1, 2, 3, 4, 5, 10, 2]
k = 7
temp = 0
result = k
find_index = 0
for i in range(len(list_1)):
    temp = k - list_1[i]
    if temp < 0:
        temp *= -1
    if temp < result:
        result = temp
        find_index = list_1[i]
    if list_1[i] == k:
        find_index = list_1[i]
print(find_index)
"""

"""
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
Пример:
k = 'ноутбук'
# 12
"""

# k = 'ноутбук'
k = input('Введите слово: ')

def play_scrable(word):
    # Словари
    rus_dic = {"А":1, "В":1, "Е":1, "И":1, "Н":1, "О":1, "Р":1, "С":1, "Т":1, "Д":2, "К":2, "Л":2, "М":2, "П":2, "У":2, "Б":3, "Г":3, "Ё":3, "Ь":3, "Я":3, "Й":4, "Ы":4, "Ж":5, "З":5, "Х":5, "Ц":5, "Ч":5, "Ш":8, "Э":8, "Ю":8, "Ф":10, "Щ":10, "Ъ":10}
    eng_dic = {"A":1, "E":1, "I":1, "O":1, "U":1, "L":1, "N":1, "S":1, "T":1, "R":1, "D":2, "G":2, "B":3, "C":3, "M":3, "P":3, "F":4, "H":4, "V":4, "W":4, "Y":4, "K":5, "J":8, "X":8, "Q":10, "Z":10}
    word = k.upper()
    result = 0
    if word[0] in eng_dic:
        for i in word:
            result += eng_dic[i]
        return result
    else:
        for i in word:
            result += rus_dic[i]
        return result

print(play_scrable(k))     