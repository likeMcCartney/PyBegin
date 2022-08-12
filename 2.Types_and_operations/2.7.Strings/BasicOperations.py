print(len('abc'))       # Number of symbols in the string
print('abc'+'def')      # Concatenation
print('Ni!' * 4)        # Repetition (equivalent to "Ni!" + "Ni!" + ...)

print('='*80)
# ==============================================================================================

myjob = 'hacker'
for c in myjob: print(c)

print('k' in myjob)     # Found
print('z' in myjob)     # Not found

print('='*80)
# ==============================================================================================

S = 'spam'
print(S[0], S[-2])
print(S[1:3], S[1:], S[:-1])

S = 'abcdefghijklmnop'
print(S[1:10:2])        # Extract elements from 1 to 10 with step by 2

S = 'hello'
print(S[::-1])

print('='*80)
# ==============================================================================================

S = "42"
I = 1
print(int(S) + I)           # Adding
print(S + str(I))           # Concatenation

print(str(3.1415))          # String
print(float('3.1415'))      # Floating point value

print('='*80)
# ==============================================================================================

print(ord('s'))             # Translates ASCII-symbol into it's direct numeric value
print(chr(115))             # Translates numerical value into ASCII-symbol

S = '5'
print(S)
S = chr(ord(S) + 1)
print(S)

B = '1101'
I = 0
while B:
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]
print(I)

print('='*80)
# ==============================================================================================
# Changing strings

S = 'spam'
S = S + 'SPAM!'
print(S)
S = S[:4] + 'Burger' + S[-1]
print(S)

S = 'splot'
S = S.replace('pl', 'pamal')
print(S)

print('That is %d %s bird!' % (1, 'dead'))
