'''
errors-
Compile time error: syntax errors
Run time error: divided by zero
Logical error: wrong output
'''
a = 5
b = 0
try:
    print("Resource open!")
    print(a/b)
except Exception as exp_name:
    print("Denominator can not be zero: ", exp_name)
finally:
    print("Resource close!")
print("Bye")
