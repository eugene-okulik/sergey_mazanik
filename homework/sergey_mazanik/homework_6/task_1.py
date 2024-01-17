'''
Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте “Etiam tincidunt neque erat,
quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
и после этого выводит получившийся текст на экран. Знаки препинания не должны оказаться внутри слова.
Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова, но уже преобразованного.
'''

sentence = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae \
semper at, dignissim vitae libero'
lst = sentence.split()
new_lst = []
for i in lst:
    if not i[-1].isalpha():
        new_lst.append(i[:-1] + 'ing' + i[-1])
    else:
        new_lst.append(i + 'ing')
print(*new_lst)
