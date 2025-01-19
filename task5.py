# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
with open('task5.txt', encoding='utf-8') as f:
    str = f.read()
    list = str.split()
imax = -1
znaki = "'.,;:?!"
for i in range(len(list)):
    x = list[i]
    for s in znaki:
        if s in x:
            x = x[:-1]
            list[i] = x
for i in range(len(list)-1):
    if len(list[i]) < len(list[i+1]):
        imax = i+1
print(list[imax])
with open('task51.txt','w', encoding='utf-8') as f:
    for c in ['Самое длинное слово: ', list[imax]+'\n', 'Его длина: ', f'{len(list[imax])}']:
        f.write(c)