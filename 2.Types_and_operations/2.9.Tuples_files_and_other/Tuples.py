t = ()                          # Empty tuple
print(t)
t1 = (0,)                       # Tuple of 1 element
print(t1)
t2 = (0, 'Ni!', 1.2, 3)         # Tuple of 4 elements
print(t2)
t2 = 0, 'Ni!', 1.2, 3           # Also tuple of 4 elements
print(t2)

t3 = ('abc' ,('def', 'ghi'))    # Nested tuple
print(t3)
print(t3[0])
print(t3[1][0])
print(t3[1:])
print(len(t3))

print(t1 + t2)                  # Concatenation
print(t2 * 3)                   # Repetition

T = (1, 2) + (3, 4)
print(T[0])
print(T[1:3])

print('=' * 80)
# =============================================================================================

x = (40)                        # Integer value
print(x)
x = (40,)                       # Tuple containing integer value
print(x)

print('=' * 80)
# =============================================================================================
# Transformation
T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)                   # Creating list from tuple
tmp.sort()                      # Sorting list
print(tmp)
T = tuple(tmp)
print(T)

T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]
print(L)

T = (1, [2, 3], 4)
print(T)
# T[1] = 'spam'                 # Error. Tuple can't be changed
T[1][0] = 'spam'                # Acceptable. Nested changeable object can be changed
print(T)
