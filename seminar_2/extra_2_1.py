# Допзадание 1
# Пользователь вводит любое число (дробное или целое), надо посчитать количество цифр в числе. 
# Решаем строго математически, обращаться к числу как к строке нельзя.

# 0 -> 1
# 9 -> 1
# 56.77 -> 4
# -0.0001 - > 5
# 100.18006 -> 8

number = float(input('Введите число: ').strip())

if number % 1 == 0:
    number = int(number)
print('Вы ввели число ', number)    
def find_fract_symbols(res):
    count = 0
    while res % 1 != 0:
        res *= 10
        count += 1 
    return count    

def find_int_symbols(res):
    res = int(res)
    count = 0
    if res == 0:
        count = 1
    else:    
        while res > 0:
            res //= 10
            count += 1
    return count  

print('Количество цифр в числе: ', find_fract_symbols(number) + find_int_symbols(number))

   