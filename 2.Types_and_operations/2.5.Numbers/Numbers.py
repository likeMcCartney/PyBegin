a = 3
b = 4
print((a + 1, a - 1))       # Addition, subtraction
print((b * 3, b / 2))       # Multiplication, division
print((a % 2, b ** 2))      # Division by modulus, exponentiation
print((2 + 4.0, 2.0 ** b))  # Type cast

print(b / 2 + 3)
print(b / (2 + 3))
print(repr(1 / 3))

print('# ===========================================================================================')
# ===========================================================================================
# Division

print(7 / 3)        # Classical division
print(7 // 3)       # Division with rounding down

print('# ===========================================================================================')
# ===========================================================================================
# Bitwise operations

x = 1               # 0001
print(x << 2)       # Left shift by 2 bits
print(x | 2)        # Bitwise "or"
print(x & 1)        # Bitwise "and"

print('# ===========================================================================================')
# ===========================================================================================
# Long ints

y = 9999999999999999999999999999999999999
print(y)
print(y + 1)
print(2 ** 200)

print('# ===========================================================================================')
# ===========================================================================================
# Complex numbers

c = 1j * 1J
print(c)
print(2 + 1j * 3)
print((2 + 1j) * 3)

print('# ===========================================================================================')
# ===========================================================================================
# Octal and hexadecimal literals

o = 0o10        # Octal numbers
print(o)
h = 0x10        # Hexadecimal number
print(h)

print(oct(64), hex(64), hex(255))

print(int('0100'), int('0100', 8), int('0x40', 16))

print(eval('100'), eval('0o100'), eval('0x40'))          # Interprets string as Python code and executes it. Very dangeroys function

print("%o, %x, %X" % (64, 64, 255))

print('# ===========================================================================================')
# ===========================================================================================
# Other implemented means for working with numbers 
import math
print(math.pi)                          # Constants
print(math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144), math.sqrt(2))
print(abs(-42), 2**4, pow(2, 4))
print(int(2.567), round(2.567), round(2.567, 2))

import random
print(random.random())
print(random.random())
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.choice(['Life of Brain', 'Holy Grail', 'Meaning of Life']))
print(random.choice(['Life of Brain', 'Holy Grail', 'Meaning of Life']))