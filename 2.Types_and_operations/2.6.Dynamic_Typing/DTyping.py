import imp
from re import A


a = 3
print(a)
a = 'spam'
print(a)
a = 3.1415
print(a)

a = 3
b = a           # b and a refers to the same object
print(a, b)
a = 5           # Create new object for b
print(a, b)
a = b
a = a + 2
print(a, b)

L1 = [1, 2, 3]
L2 = L1 
print(L1, L2)
L1 = 24         # Create new object for L1
print(L1, L2)
L1 = L2         # L1 and L2 refers to the same object
print(L1, L2)
L1[0] = 24      # NEW OBJECT DIDN'T CREATE, CHANGE L1 AND L2 AT THE SAME TIME
print(L1, L2)

L1 = [2, 3, 4]
L2 = L1[:]      # Create new object, assign values equal to L1
print(L1, L2)
L1[0] = 24      # L1[0] changed, but L2[0] did not. L2 refers to copy of L1
print(L1, L2)

# Dictionary
import copy
X = {'sex' : 'male', 'age' : 23, 'firstname' : 'Paul', 'lastname' : 'Kanashkov'}
Y = X
print(X, Y)
X['age'] += 1
print(X, Y)
Y = copy.copy(X)
Y = copy.deepcopy(X)
X['age'] += 1
Y['age'] -= 1
print(X, Y)

# Equality
L = [1, 2, 3]
M = L[:]
print(L == M)   # Same value
print(L is M)   # Same object


