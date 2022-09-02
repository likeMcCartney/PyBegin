
x = 1
if x:
    y = 2
    if y:
        print('Block 2')
    print('Block 1')
print('Block 0')

print('='*80)
# =====================================================

    # x = 'SPAM'                # Error: first line is intented
x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)
        # x += 'NI'             # Error: unexpected intent
    if x.endswith('NI'):
        x *= 2
    # print(x)                  # Error: unindent does not match any outer indentation level

print('='*80)
# =====================================================

x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x)

print('='*80)
# =====================================================
