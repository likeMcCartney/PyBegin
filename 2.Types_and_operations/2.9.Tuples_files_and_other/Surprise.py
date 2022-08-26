X = [1, 2, 3]
Y = ['a', X, 'b']           # Y contains reference to X
D = {'x': X, 'y': 2}        # D also contains reference to X

print(X)
print(Y)
print(D)

X[1] = 'surprise'           # Y and D are not changeable, but X can be changed

print(X)
print(Y)
print(D)

L = [1, 2, 3]
D = {'a' : 1, 'b' : 2}

A = L[:]                    # Instead of A = L
B = D.copy()

A[1] = 'Ni!'
B['b'] = 'spam'
print(L, D)
print(A, B)

X = [1, 2, 3]
L = ['a', X[:], 'b']
D = {'x': X[:], 'y': 2}

import copy
X = copy.deepcopy(Y)
