table = [
    ['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
    ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
    ['my song.mp3','anapa-2003.jpg', 'cs 1.6.exe', 'folder', 'cheat.txt'],
    ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4', 'array.py'],
    ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']
]

print("Начальный список:")
for row in table:
    print(row)

for row in table:
    for i in range(len(row)):
        if row[i] == 'folder':
           row[i] = ''
        if row[i] == 'data.accdb':
            row[i] = 'data.sql'

print("\nБез папок и с заменой data:")
for row in table:
    print(row)

ru_files = []
for row in table:
    for item in row:
        if item.endswith('.ru'):
            ru_files.append(item)

print("\nВсе файлы .ru:")
print(ru_files)

for row in table:
    for i in range(len(row)):
        if '.' in row[i]:
            name, ext = row[i].split('.')
            row[i] = f'new_{name}.{ext}'

print("\nВсе файлы с добавлением new_:")
for row in table:
    print(row)