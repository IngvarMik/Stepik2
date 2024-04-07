"""Метод partition"""
text = "Python is best"
print(text.partition('is ')) # ('Python ', 'is ', 'best')
print(text.partition('not ')) # ('Python is best', '', '')
s = "Python is best, isn't it"# 
print(s.partition('is'))# ('Python ', 'is', " best, isn't it")

"""Метод rpartition"""
text = "Python is best"

print(text.rpartition('is ')) # ('Python ', 'is ', 'best')
print(text.rpartition('not ')) # ('', '', 'Python is best')

s = "Python is best, isn't it"

print(s.rpartition('is')) # ('Python is best, ', 'is', "n't it")