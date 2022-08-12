s1 = ''                             # Empty string, string in apostrophes
print(s1)
s2 = "spam's"                       # String in quotation marks, same as string in apostrophes
print(s2)
block = """block"""                 # String in triple quotation marks
print(block)
s3 = r'\temp\spam'                  # Unformatted string
print(s3)
s4 = u'spam'                        # String with unicode symbols
print(s4)

print(s1 + s2)                      # Concatenation
print(s2 * 3)                       # Repetition

print(s2[0])                        # Reffering to the symbol
print(s2[0:3])                      # Extracting a substring

title = "Meaning " 'of' " Life"     # Implicit concatenation
print(title)

print('# ====================================================================================================================')
# ====================================================================================================================
# Escape sequences

e1 = "This string is too \
long. It's very-very, \
very-very, very-\
very long "
print(e1)

e2 = "That's why we use escape \"\\\" to move to a new line"
print(e2)
e3 = "By the way, we've already used to use escapes \'\\\"\', \'\\\\\' and \"\\\'\" \
to print respective symbols"
print(e3)

print('# ====================================================================================================================')
# ====================================================================================================================

x = "C:\py\code"
print(x)
print(len(x))

fpath = "C:\new\text.dat"
print(fpath)
print(len(fpath))
fpath = r"C:\new\text.dat"
print(fpath)
print(len(fpath))

print('# ====================================================================================================================')
# ====================================================================================================================
# Triple quotation marks
mantra = """Always look
on the bright
side of life"""
print(mantra)

print('# ====================================================================================================================')
# ====================================================================================================================
# Unicode strings

u = u"spam"
print(u)
print("ni" + u)

print(str(u'spam'))
