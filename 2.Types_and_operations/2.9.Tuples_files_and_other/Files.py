myfile = open('myfile', 'w')        # Opening the file for write (create file)
myfile.write('hello text file\n')   # Write string into the file
myfile.close()                      # Pushes data to ROM
myfile = open('myfile')             # Opening the file for read (by default)
print(myfile.readline())            # Reads the string
print(myfile.readline())            # Empty string, end of file

print('=' * 80)
# ===========================================================================================================

X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')           # Creates file for write
F.write(S + '\n')                       # Writes string into the file, string ends with '\n' symbol
F.write('%s,%s,%s\n' % (X, Y, Z))       # Translates numbers into string
F.write(str(L) + '$' + str(D) + '\n')   # Translates list and dictionary into string
F.close()

bytes = open('datafile.txt').read()     # Opens the file and reads data
print(bytes)

F = open('datafile.txt')                # Open the file again
line = F.readline().rstrip()            # Read the first line and delete end-of-string symbol
print(line)

line = F.readline()                     # Read line
parts = line.split(',')                 # Create list of splitted values
print(parts)
print(int(parts[1]))                    # Translate string into integer
numbers = [int(P) for P in parts]       # Translate all the list
print(numbers)

line = F.readline()
parts = line.split('$')                 # Split the string by '$' symbol
print(parts)
print(eval(parts[0]))                   # Translate string into object
objects = [eval(P) for P in parts]      # Translate all strings into objects
print(objects)

print('=' * 80)
# ===========================================================================================================
# Module 'Pickle'

F = open('datafile.txt', 'wb')          # 'Pickle' module needs the file to be opened in binary mode
import pickle
pickle.dump(D, F)
F.close()

F = open('datafile.txt', 'rb')
E = pickle.load(F)
print(E)
