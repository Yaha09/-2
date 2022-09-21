# Есть строка letters. Нужно пройтись по каждому символу строки с помощью цикла и:

# Посчитать количество символов равных значению переменной template
# Вывести все символы, не равные значению exclude
# Для теста можно использовать:

# letters = 'Who keeps company with the wolf, will learn to howl.'
# template = 'w'
# exclude = 'l'


letters = 'Who keeps company with the wolf, will learn to howl.'
template = 'w'
exclude = 'l'
counter_template = 0
counter_exclude = 0
counter_ = 0
for i in letters:
    counter_ = counter_ + 1
    if i == template:
        counter_template = counter_template + 1
    if i != exclude:
        counter_exclude = counter_exclude + 1

print('количество в тексте ', template, counter_template)
print('количество не ', exclude, counter_exclude)
print('количество символов ',counter_)






