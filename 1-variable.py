# No data type is to be mentioned in declaring variable
x = 10
y = 2.5
z = "Hellow world"
print(x, y, z)

# multiple value declaration in a same line
name, age = "Palash", 22
print(name)
print(age)

# memory location of a variable
x = 90
y = 10
z = x + y
p = 100

print(id(x))
print(id(y))
print(id(z))
print(id(p))

'''Note: Here both the id's of z(1539261093328) and p(1539261093328) are same 
as their values are also same. So python does not allocate
memory based on their variable name rather on their values.
therefire python is a memory efficient language.
'''
