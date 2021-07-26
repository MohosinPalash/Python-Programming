'''Criteria: 
unordered, 
changeable, 
indexed, 
key name may be anything, 
nested dictionary possible
'''
d1 = {'name': 'Palash', 'age': 22, 'BYear': 1997}
print(d1)
print(d1.get('age'))
print(d1.items())
print(d1.keys())

d2 = d1.copy()
print(d2)
print('Length = ', len(d2))

d2['university'] = "AUST"
print(d2)
d2.pop('university')
print(d2)
