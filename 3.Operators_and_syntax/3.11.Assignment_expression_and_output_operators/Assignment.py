spam = 'spam'                   # Basic form
spam, ham = 'yum', 'YUM'        # Tuple assignment
[spam, ham] = ['yum', 'YUM']    # List assignment
a, b, c, d = 'spam'
a, *b = 'spam'
spam = ham = 'lunch'
spams = 0
spams += 42

print('='*80)
# =========================================================================

nudge = 1
wink = 2
A, B = nudge, wink
print(A, B)
[C, D] = [nudge, wink]
print(C, D)

print('='*80)
# =========================================================================

[a, b, c] = [1, 2, 3]
print(a, c)
(a, b, c) = 'ABC'
print(a, c)

print('='*80)
# =========================================================================

string = "SPAM"
a, b, c, d = string
print(a, d)
#a, b, c = string                           # Error

a, b, c = string[0], string[1], string[2:]
print(a, b, c)
a, b, c = list(string[:2]) + [string[2:]]
print(a, b, c)
a, b = string[:2]
c = string[2:]
print(a, b, c)
(a, b), c = string[:2], string[2:]
print(a, b, c)

print('='*80)
# =========================================================================
