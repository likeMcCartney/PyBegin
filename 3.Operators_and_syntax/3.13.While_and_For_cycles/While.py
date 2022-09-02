# while True:
#     print('Type Ctrl+C to stop me')

x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]

print('\n')

a = 0; b = 10
while a < b:
    print(a, end=' ')
    a += 1

print('\n')

print('=' * 80)
# =========================================================

a = 0; b = 10
while a < b:
    a += 1
    if not a % 2:
        continue
    print(a, end=' ')

print('\n')

while True:
    name = input('Enter name: ')
    if name == 'stop':
        break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age) ** 2)

y = 12
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')    
