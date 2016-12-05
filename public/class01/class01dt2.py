# class01dt2.py

# This script should Copy Values Between Some Common Data Types.

# Demo:
# python class01dt2.py

# Useful converson functions are listed below:
# float()
# int()
# str()

import pdb
# Maybe, I should run this script in the debugger:
# pdb.set_trace()

# I should copy 1 from Integer to Float:
my_i = 1
my_f = float(my_i)
print(my_f)

# I should copy 1.0 from Float to Integer:
my_f = 1.0
my_i = int(my_f)
print(my_i)

# I should copy 1 from Integer to String:
my_i = 1
my_s = str(my_i)
print(my_s)

# I should copy 1.1 from Float to String:
my_f = 1.1
my_s = str(my_f)
print(my_s)

# I should copy '1.1' from String to Float:
my_s = '1.1'
my_f = float(my_s)
print(my_f)

# I should copy '1' from String to Integer:
my_s = '1'
my_i = int(my_s)
print(my_i)

# I should convert True to Integer:
my_b = True
my_i = int(my_b)
print(my_i)

# I should convert False to Integer:
my_b = False
my_i = int(my_b)
print(my_i)

# I should convert 1 from Integer to Boolean:
my_i = 1
my_b = bool(my_i)
print(my_b)

# I should convert 0 from Integer to Boolean:
my_i = 0
my_b = bool(my_i)
print(my_b)

# I should convert 3.3 from Float to Boolean:
my_f = 3.3
my_b = bool(my_f)
print(my_b)

# I should convert 0.0 from Float to Boolean:
my_f = 0.0
my_b = bool(my_f)
print(my_b)

'bye'
