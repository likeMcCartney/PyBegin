from dataclasses import replace


S = 'spammy'
print(S)
S = S[:3] + 'xx' +S[5:]
print(S)

S = 'spammy'
print(S)
S = S.replace('mm', 'xx')
print(S)

print('aa$bb$cc$dd'.replace('$', 'SPAM'))

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')
print(where)
S = S[:where] + 'EGGS' + S[(where + 4):]
print(S)

S = 'xxxxSPAMxxxxSPAMxxxx'
print(S)
print(S.replace('SPAM', 'EGGS'))
print(S.replace('SPAM', 'EGGS', 1))

S = 'spammy'
L = list(S)
print(L)
L[3] = 'x'
L[4] = 'x'
print(L)
S = ''.join(L)
print(S)

print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))

print('=' * 80)
# =========================================================================
line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
print(col1)
print(col3)

line = 'aaa bbb ccc'
cols = line.split()
print(cols)

line = 'bob,hacker,40'
print(line.split(','))
line = "i'mSPAMaSPAMlumberjack"
print(line.split('SPAM'))

print('=' * 80)
# =========================================================================
line = "The knights who say Ni!\n"
print(line)
print(line.rstrip())
print(line.upper().rstrip())
print(line.isalpha())
print(line.endswith('Ni!\n'))

print(line.find('Ni') != -1)
print('Ni' in line)
sub = 'Ni!\n'
print(line.endswith(sub))
print(line[-len(sub):] == sub)

print('=' * 80)
# =========================================================================
# String module

S = 'a+b+c+'
print(S)
x = S.replace('+', 'SPAM')
print(x)

