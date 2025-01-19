# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
with open('task3.txt', encoding='utf-8') as f:
    list = f.read().split()
znaki = "'.,;:?!"
for i in range(len(list)):
    x = list[i]
    for s in znaki:
        if s in x:
            x = x[:-1]
            list[i] = x
    list[i] = list[i].lower()
list = sorted(list)
while len(list)>0:
    word = list[0]
    k = 1
    for j in range(1, len(list)):
        if list[j] == word:
            k += 1
    print(f'{word}: {k}')
    for ii in range(k):
        list.remove(word)