# Задача. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле 
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
# 4. Использование функций. 
# Ваша программа не должна быть линейной

def display_phonebook(fi):
    item = open(fi, 'r')
    screen = item.read()
    print(screen)
    temp = []
    book = {}
    screen = list(screen.split('\n'))
    for i in screen:
        temp = i.split('\t')
        for j in temp:
            z = j.split()
            print()
        
    
    item.close()

def write_phonebook(fi):
    item = open(fi, 'a+')
    while True:
        new_contact = input("Добавить новый контакт в телефонную книгу (да/нет)?: ")
        if new_contact == 'да':
            phone = input("Введите номер телефона: +7")
            name = input("Введите имя: ")
            item.write(f"Имя: {name}\t")
            item.write(f"Телефон: +7{phone}\n")
        else:
            break
    item.close()

def vote_operation(fi):
    print('Телефонная книга')
    print('Для создания контактов введите 1, для просмотра контактов введите 2')
    vote = int(input('Введите цифру: '))
    if vote == 1:
        write_phonebook(fi)
    elif vote == 2:
        display_phonebook(fi)  


phonebook = 'phonebook.txt'
vote_operation(phonebook)


