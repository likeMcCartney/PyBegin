L = []                              # Empty list
print(L)
L = [123, 'abc', 1.23, {}]          # Four elements
print(L)
L = ['Bob', 40.0, ['dev', 'mgr']]   # Nested sublists
print(L)

print('=' * 80)
# =================================================================================

print(len([1, 2, 3]))           # Length
print([1, 2, 3] + [4, 5, 6])    # Concatenation
print(['Ni!'] * 4)              # Repetition
print(str([1, 2]) + '34')       # Same as '[1, 2]' + '34'
print([1, 2] + list('34'))      # Same as [1, 2] + ['3', '4']

print('=' * 80)
# =================================================================================

print(3 in [1, 2, 3])
for x in [1, 2, 3]:
    print(x, end = ' ')
print('\n')

res = [c * 4 for c in 'SPAM']
print(res)

res = []                        # Equivalent
for c in 'SPAM':
    res.append(c * 4)
print(res)

print(list(map(abs, [-1, -2, 0, 1, 2])))

print('=' * 80)
# =================================================================================

L = ['spam', 'Spam', 'SPAM!']       # Indexing
print(L[2])
print(L[-2])
print(L[1:])                        # Slicing

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])
print(matrix[0][2])

L = ['spam', 'Spam', 'SPAM!']
print(L)
L[1] =  'eggs'
print(L)
L[0:2] = ['eat', 'more']
print(L)

print('=' * 80)
# =================================================================================

L = [1, 2, 3]
print(L)
L[1:2] = [4, 5]     # Replacement/insertion
print(L)
L[1:1] = [6, 7]     # Insertion (replaces nothing)
print(L)
L[1:2] = []         # Deletion (inserts nothing)
print(L)

L = [1]
L[:0] = [2, 3, 4]
print(L)
L[len(L):] = [5, 6, 7]
print(L)
L.extend([8, 9, 10])
print(L)

print('=' * 80)
# =================================================================================
# Methods

L = ['eat', 'more', 'SPAM!']
L.append('please')              # Add element to the end
print(L)
L.sort()
print(L)

L = ['abc', 'ABD', 'aBe']
L.sort()
print(L)
L.sort(key=str.lower)
print(L)
L.sort(key=str.lower, reverse=True)
print(L)

L = ['abc', 'ABD', 'aBe']
print(sorted(L, key=str.lower, reverse=True))
print(sorted([x.lower() for x in L], reverse=True))

L = [1, 2]
L.extend([3, 4, 5])
print(L)
print(L.pop())
print(L)

L.reverse()
print(L)
print(list(reversed(L)))

L = []
L.append(1)         # Push into the stack
L.append(2)
print(L)
print(L.pop())      # Pop out of the stack
print(L)

L = ['SPAM', 'eat', 'more', 'please']
print(L)
del L[0]
print(L)
del L[1:]
print(L)

L = ['Already', 'got', 'one']
print(L)
L[1:] = []
print(L)
L[0] = []
print(L)
