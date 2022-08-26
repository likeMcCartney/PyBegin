# ===========================================================================================================
# Numbers

a = 3
b = 2
print(f"a = {a}, b = {b}; a + b = {a + b}; a - b = {a - b}")

pi = 3.14
R = 8
print(f"pi = {pi}, radius R = {R}, perimeter of the circle l = 2*pi*R = {2 * pi * R}")
print(f"area of the circle S = pi*R^2 = {pi * R**2}")

print('# ===========================================================================================================')
# ===========================================================================================================
# Import libs
import math
import re

print(math.pi)
print(math.sqrt(625))

print('# ===========================================================================================================')
# ===========================================================================================================
# Strings

str = "Everybody lies, but everybody dies"
print(str)
print(len(str))
print(str[0])
print(str[4])
print(str[-1])
print(str[-2])

print(str[4:9])     # Extract all elements from 4 to 9
print(str[1:])      # Print all elements excepting the 1'st
print(str)          # No changes
print(str[:3])      # Same as str[0:3]
print(str[:-1])     # Print all elements excepting the last
print(str[:])       # Also no changes

print(str + ' (c) Gregory House')   # Concatenation
print(str*2)                        # Repeat 2 times

# Trying to change string
#str[0] = 'z'       # Not working
str = 'z' + str[1:]
print(str)

print(str.find('li'))               # Pattern offset
print(str.replace('li', 'iLI'))     # Replace string pattern with user pattern

line = "aaa,bbb,ccc,ddd"
s = line.split(',')
print(s[0], s[1], s[2], s[3])   # Split and create list
print(str.upper())              # Upper

print('# ===========================================================================================================')
# ===========================================================================================================
# Lists

L = [123, 'Spam', 1.23]     # List of 3 different types
print(len(L))
print(L)
print(L[0])
print(L[-1])
print(L + [4, 5, 6])
print(L)

# Specific type methods
L.append('NI')      # Add one element to the end
print(L)
L.pop(2)            # Remove 2'nd element
print(L)

M = ['bb','cc','aa']
print(M)
M.sort()            # Sort
print(M)
M.reverse()         # Reverse
print(M)

# Python doesn't allow access to list elements which doesn't exist
# print(M[99])

Matr = [[1,2,3],
        [4,5,6],
        [7,8,9]]
print(Matr)
print(Matr[0])
print(Matr[0][2])
col2 = [row[1] for row in Matr]     # Choose elements of 2'nd column
print(col2)

print([row[1] + 1 for row in Matr])                 # Print Matr[i][2] + 1
print([row[1] for row in Matr if row[1] % 2 == 0])  # Print Matr[i][2] if Matr[i][2] is even

diag = [Matr[i][i] for i in [0, 1, 2]]
print(diag)
doubles = [c * 2 for c in 'spam']
print(doubles)

print('# ===========================================================================================================')
# ===========================================================================================================
# Dictionaries (mapping)

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D)
print(D['food'])
D['quantity'] += 1
print(D)

# Usually creates like this
D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40

print(D)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
        'job': ['dev', 'mgr'],
        'age': 40.5}
print(rec['name'])
print(rec['name']['last'])
print(rec['job'])
print(rec['job'][-1])
rec['job'].append('janitor')
print(rec['job'])
print(rec)

rec = 0

D = {'a': 1, 'c': 3, 'b': 2}
print(D)

Ks = D.keys()

for key in sorted(D):
    print(key, '=>', D[key])

for c in 'spam':
    print(c.upper())
squares = [x ** 2 for x in [1,2,3,4,5]]
print(squares)
# Equivalent
squares = []
for x in [1,2,3,4,5]:
    squares.append(x ** 2)
print(squares)

# List generator works twice faster then cycles
D['e'] = 99
print(D)
print('a' in D)
print('f' in D)

print('# ===========================================================================================================')
# ===========================================================================================================
# Tuple

T = (1, 2, 3, 4)
print(T)
print(len(T))
T += (5, 6)          # Concatenation
print(T)
print(T[0])
# Tuple elements can not be changed
# T[0] = 2

print('# ===========================================================================================================')
# ===========================================================================================================
# Files

f = open('data.txt', 'w')   # Create file and open it for writing
f.write('Hello\n')          # Print "Hello world"
f.write('world\n')
f.close()                   # Close file

f = open('data.txt')        # Open file for reading
bytes = f.read()
print(bytes)
print(bytes.split())

print('# ===========================================================================================================')
# ===========================================================================================================

X = set('spam')
Y = set(['h', 'a', 'm'])
print(X, Y)
print(X & Y)
print(X | Y)
print(X - Y)

import decimal
d = decimal.Decimal('3.141')
d += 1
print(d)
print(1 > 2)
print(1 < 2)

X = None
print(X)
L = [None] * 100
print(L)
