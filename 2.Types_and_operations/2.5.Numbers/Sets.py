x = set('abcde')
y = set('bdxyz')

print(x)

print('e' in x)     # Occurence in a set check
print(x - y)

print(x | y)
print(x & y)

engineers = set(['bob', 'sue', 'ann', 'vic'])
managers = set(['tom', 'sue'])

print(engineers & managers)     # Someone who is an engineer and a manager
print(engineers | managers)     # Both engineers and managers
print(engineers - managers)     # All engineers excepting managers