'''
Properties of list:
ordered, changeable, allows duplicate values, contains
any types of data in a single list, allows nested list
'''
list = [1, 4, 36, 5.5, 65, 'Palash', [10, 15, 20], 36]
print(list)
print(list[5])
# print the items of nested list
print(list[6][2])

# append another list
list = list + ['Rakib', 10, 2000]
print(list)
list.extend(['Tanjim', 2, 1500])
print(list)

# remove the
list.remove('Palash')
print(list)
# count(frequency)
print(list.count(36))
