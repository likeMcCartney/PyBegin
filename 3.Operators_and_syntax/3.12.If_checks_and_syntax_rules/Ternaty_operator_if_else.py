X = 1

Y = 3
Z = 5
if X:
    A = Y
else:
    A = Z

print(A)

A = Y if X else Z               # Ternaty if else
print(A)

A = 't' if 'spam' else 'f'      # Not empty strings are equivalent to truth
print(A)
A = 't' if '' else 'f'
print(A)
