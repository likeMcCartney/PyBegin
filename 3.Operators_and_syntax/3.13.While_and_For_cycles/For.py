for x in ['spam', 'eggs', 'ham']:
    print(x, end=" ")

sum = 0
for x in [1, 2, 3, 4]:
    sum = sum + x
print(sum)

prod = 1
for item in [1, 2, 3, 4]: prod *= item
print(prod)

S = 'lumberjack'
T = ['and', "I'm", 'okay']
for x in S: print(x, end=' ')
for x in T: print(x, end=' ')

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)

D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])

print(list(D.items()))
for (key, value) in D.items():
    print(key, '=>', value)

T = [(1, 2), (3, 4), (5, 6)]
for both in T:
    a, b = both
    print(a, b)

((a, b), c) = ((1, 2), 3)
print(a, b, c)
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)

a, *b, c = (1, 2, 3, 4)
print(a, b, c)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

items = ['aaa', 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]
for key in tests:
    for item in items:
        if item == key:
            print(key, 'was found')
            break
    else:
        print(key, 'not found!')

for key in tests:
    if key in items:
        print(key, 'was found')
    else:
        print(key, 'not found')

seq1 = 'spam'
seq2 = 'scam'

res = []
for x in seq1:
    if x in seq2:
        res.append(x)
print(x)
