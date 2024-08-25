# Задача 3. Словарь синонимов 
# Одна библиотека поручила вам написать программу для оцифровки словарей синонимов. На вход в программу подаётся N пар слов. Каждое слово является синонимом для своего парного слова. 
# Реализуйте код, который составляет словарь синонимов (все слова в словаре различны), затем запрашивает у пользователя слово и выводит на экран его синоним. Обеспечьте контроль ввода: если такого слова нет, выведите ошибку и запросите слово ещё раз. При этом проверка не должна зависеть от регистра символов. 

# Пример 
# Введите количество пар слов: 3 
# Первая пара: Привет — Здравствуйте 
# Вторая пара: Печально — Грустно 
# Третья пара: Весело — Радостно 
# Введите слово: интересно 
# Такого слова в словаре нет. 
# Введите слово: здравствуйте 
# Синоним: Привет

synonyms_dict = dict()

pairs_count = int(input('Введите количество пар слов:'))

for i in range(pairs_count):
    first_word, second_word = input(f'{i+1} пара: ').strip().lower().split('-')
    synonyms_dict[first_word] = second_word
    synonyms_dict[second_word] = first_word

while True:
    word = input('Введите слово: ').lower()
    if word in synonyms_dict:
        print('Синоним: ', synonyms_dict[word].capitalize())
        break
    else:
        print('Такого слова в словаре нет.')