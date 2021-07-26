'''Criteria: don't allow repeated values,
sort in ascending order
'''
s = {1, 3, 2, 5, 4, 4}
print(s)

# insert items in set
s.add(6)  # single value
s.update([8, 9, 7])  # multiple values
s1 = {10, 12, 13}
s.update(s1)  # another set
print(s)


# remove items from set
s.remove(10)
print(s)
# s.remove(30)  # shows error
# print(s)
s.discard(30)  # does not show error
print(s)


# set functions
s2 = {1, 3, 4, 5}
s3 = {2, 4, 6, 7}
anotherSet = {10, 12, 13}
s4 = s2.intersection(s3)
print(s4)
s5 = s2.difference(s3)
print(s5)
s6 = s2.symmetric_difference(s3)
print(s6)

s7 = s2.union(s3, anotherSet)
print(s7)
s8 = s2 | anotherSet  # Another Process
print(s8)

# convert list into set
li = [1, 2, 5, 1, 5]
result = set(li)
print(result)
# Again convert the set into list
result = list(set(li))
print(result)
'''Benefit: Remove the duplicate values in list'''
