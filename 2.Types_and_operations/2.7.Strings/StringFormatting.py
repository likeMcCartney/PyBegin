exclamation = 'Ni!'
print("Knights who say %s" % (exclamation))
print("%d %s %d you" % (1, 'spam', 4))
print("%s -- %s -- %s" % (42, 3.14159, [1, 2, 3]))

print('=' * 80)
# =========================================================================

x = 1234
res = "integers: ...%d...%-6d...%06d" % (x, x, x)
print(res)

x = 1.23456789
print(x)
print("%e | %f | %g" % (x, x, x))
print("%-6.2f | %05.2f | %+06.1f" % (x, x, x))
print("%s" % x, str(x))

print('=' * 80)
# =========================================================================
# Formatting strings from dictionaries
print("%(n)d %(x)s" % {"n": 1, "x": 'spam'})

reply = """
Greetings...
Hello %(name)s!
You are squared is %(age)s
"""
values = {'name': 'Bob', 'age': 40}
print(reply % values)

food = 'spam'
age = 40
print(vars())
