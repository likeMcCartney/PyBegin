a, b = 'good', 'bad'            # Assignment, links
print(a, b)

x = 2
y = 1
print(x,y)
if (x > y):                     # Don't do like that. It's not C, relax :)
    x = 1;
    y = 2;
print(x,y)

if x < y:                       # Much better
    x = 2                       # In Python indent matters
    y = 1
print(x,y)

A, B, C, D = 1, 2, 3, 4

X = (A + B +
     C + D)

if (A == 1 and
    B == 2 and
    C == 3):
        print('spam' * 3)
