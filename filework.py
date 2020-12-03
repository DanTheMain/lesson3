# Скачайте файл по ссылке
# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt

content = ''
with open('./referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()

with open('./referat2.txt', 'w', encoding='utf-8') as f:
    f.write(content.replace('.', '!'))

print(content)
print(len(content))
print(len(content.split()))

with open('./referat2.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
