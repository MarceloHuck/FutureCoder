name = 'World'
line = ''
for char in name:
    line = line + char + ' '
    print(line)
    
name = 'World'
line = ''
for char in name:
    line = char + line
    print(line)
    

name = 'World'
print(name)
line = ''
for char in name:
    line += '-'
print(line)


name = 'World'
line = '+'
for _ in name:
    line += '-'
line += '+'
print(line)
name = '|' + name + '|'
print(name)
print(line)

name = 'World'
line = '+' + name + '+'
print(line)
for char in name:
    line = char
    for _ in name:
        line += ' '
    line += char
    print(line)
    
line = '+' + name + '+'
print(line)

name = 'World'
line = ''
for char in name:
    print(line + char)
    line += ' '