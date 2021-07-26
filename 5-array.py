'''Type code: 
https://www.educative.io/edpresso/what-are-type-codes-in-python
'''


from array import *
salary = array('i', [10000, 20000, 15000, 30000, 50000])
print(salary)
for i in range(5):
    print(salary[i])

# print address and arraylength
print(salary.buffer_info())

''' There are lots of array function to explore
'''
