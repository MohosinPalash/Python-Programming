'''Variables are of three types: Numeric, Sequence, Dictionarty
Numeric: integer, complex, float, boolean
Sequence: string, list, set, tuple, range
'''
# Numeric Data Types

i, f, c, b = 5, 2.5, 3+7j, 5 < 6
variable_type = type(i)
print(variable_type)
variable_type = type(f)
print(variable_type)
variable_type = type(c)
print(variable_type)
variable_type = type(b)
print(variable_type)

# Sequence Data Types
str, li, tp, st = "Palash", [1, 2, 3], (1, 2, 3), {1, 2, 3}
variable_type = type(str)
print(variable_type)
variable_type = type(li)
print(variable_type)
variable_type = type(st)
print(variable_type)
variable_type = type(tp)
print(variable_type)
