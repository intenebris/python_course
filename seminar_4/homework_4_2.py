# Задача 2. Палиндром 
# Пользователь вводит строку. Необходимо написать программу, которая определяет, существует ли у этой строки перестановка, при которой она станет палиндромом. Затем она должна выводить соответствующее сообщение. 

# Пример 1 
# Введите строку: aab 
# Можно сделать палиндромом 

# Пример 2 
# Введите строку: aabc 
# Нельзя сделать палиндромом

date = input("Введите строку: ")
counter = 0

for elem in date:
    if (date.count(elem) % 2 == 0) or (date.count(elem) == len(date)):
        counter += 1
if (counter + 1 == len(date)) or (counter == len(date)):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')    