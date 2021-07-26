'''Criteria: unchangeable, size efficient, can not remove any 
specific element rather have to delete the whole tuple
'''
import sys
tuple = (1, 2, 6, 5)
list = [1, 2, 6, 5]

print('Size of tuple', sys.getsizeof(tuple))
print('Size of list', sys.getsizeof(list))

del tuple
print(tuple)
print(list)
