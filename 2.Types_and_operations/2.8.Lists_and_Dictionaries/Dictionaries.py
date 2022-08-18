from msilib.schema import tables


D1 = {}                                 # Empty dictionary
print(D1)
D2 = {'spam': 2, 'eggs': 3}             # Dictionary with 2 elements
print(D2)
D3 = {'food': {'ham': 1, 'egg': 3}}     # Nesting
print(D3)

print(D2['eggs'])                       # Access via element keys
print(D3['food']['egg'])

# print(D2.has_key('eggs'))             # Not working in Python 3.10.5
print('eggs' in D2)                     # Entry check
print(D2.keys())                        # List of keys
print(D2.values())                      # List of values

print(len(D2))

print('='*80)
# =======================================================================================================================

d2 = {'spam': 2, 'ham': 1, 'eggs': 3}
print(d2['spam'])

print(len(d2))                          # Number of elements in dictionary
ld = d2.keys()                          # Creates keys list
print(ld)

print(d2)
d2['ham'] = ['grill', 'bake', 'fry']    # Changing elements
print(d2)
del d2['eggs']                          # Deleting an element
print(d2)
d2['brunch'] = 'Bacon'                  # Adding new element
print(d2)

print('='*80)
# =======================================================================================================================
# Additional methods

d2 = {'spam': 2, 'ham': 1, 'eggs': 3}
print(d2.values())
print(d2.items())

print(d2.get('spam'))                   # Key exists in dictionary
print(d2.get('toast'))                  # Key is missing
print(d2.get('toast', 88))

print(d2)
d3 = {'toast': 4, 'muffin': 5}
d2.update(d3)                           # Concatenation of 2 dictionaries
print(d2)

print(d2.pop('muffin'))
print(d2.pop('toast'))
print(d2)

print('='*80)
# =======================================================================================================================
# Table of languages

table = {'Python': 'Guido van Rossum',
'Perl': 'Larry Wall',
'Tcl': 'John Ousterhout'}

language = 'Python'
creator = table[language]
print(creator)
for lang in table.keys():
    print(lang, "\t", table[lang])

print('='*80)
# =======================================================================================================================
# Dictionaries as flexible lists
L = [0] * 100
L[99] = 'spam'
print(L[99])
print(L)

D = {}
D[99] = 'spam'
print(D[99])
print(D)

print('='*80)
# =======================================================================================================================
# Sparse data storage
Matrix = {}
Matrix[(2,3,4)] = 88            # Sparced 3-d matrix with two elements
Matrix[(7,8,9)] = 99

X = 2; Y = 3; Z = 4
print(Matrix[(X, Y, Z)])
print(Matrix)

# print(Matrix[(2,3,6)])        # Key (2,3,6) does not exist
if (2,3,6) in Matrix:           # Check if the key exists
    print(Matrix(2,3,6))
else:
    print(0)

try: 
    print(Matrix[(2,3,6)])
except KeyError:                # Catching the exception
    print(0)

print(Matrix.get((2,3,4), 0))   # Exist. Extract an return
print(Matrix.get((2,3,6), 0))   # Do not exist. Use default value

print('='*80)
# =======================================================================================================================
# Using dictionaries as records
rec = {}
rec['name'] = 'mel'
rec['age'] = 45
rec['job'] = 'trainer/writer'

print(rec['name'])

mel = {'name': 'Mark',
'jobs': ['trainer', 'writer'],
'web': 'www.rmi.net/~lutz',
'home': {'state': 'CO', 'zip': 80513}}

print(mel['name'])
print(mel['jobs'])
print(mel['jobs'][1])
print(mel['home']['zip'])

print('='*80)
# =======================================================================================================================
# Other ways to create dictionaries
print({'name': 'mel', 'age': 45})               # Traditional literal expression

D = {}                                          # Dynamic assignment by keys
D['name'] = 'mel'
D['age'] = 45
print(D)

D = dict(name='mel', age=45)                    # Named arguments form
print(D)

print(dict([('name', 'mel'), ('age', 45)]))     # Tuples "key/value"
