# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
with open('task1.txt', encoding='utf-8') as f:
    a = f.readlines()
    print('Общее количество строк:', len(a))
with open('task1.txt', encoding='utf-8') as f:
    b = f.read()
    l = b.split()
    while '—' in l:
        l.remove('—')
    print("Общее количество слов:", len(l))
with open('task1.txt', encoding='utf-8') as f:
    c = f.read()
    print("Общее количество символов:", len(c))
