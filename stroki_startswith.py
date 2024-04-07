"""метод startswith"""
s = 'Мила Кунис'
print(s.startswith('Мила'))
print(s.startswith('М'))
print(s.startswith('Бред'))
print('-----')
print(s.startswith('Мила', 1))
print(s.startswith('ила', 1))
print('-----')
print(s.startswith('ил', 1, 2))
print(s.startswith('ил', 1, 3))

"""метод endswith"""
s = 'Мила Кунис'

print(s.endswith('Кунис'))
print(s.endswith('с'))
print(s.endswith('Бред'))
print('-----')
print(s.endswith('нис', 10))
print(s.endswith('нис', 7))
print(s.endswith('нис', -3))
print('-----')
print(s.endswith('ис', 8, 9))
print(s.endswith('ис', 8, 10))