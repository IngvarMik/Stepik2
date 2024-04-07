""" Метод ljust"""
d = 'qwerty'
print(d.ljust(10)) # qwerty
print(d.ljust(10, '-')) # qwerty----
print(d.ljust(15, '&')) # qwerty&&&& - 15 это общее количество символов
print(d.ljust(5, '!')) # qwerty

"""Метод rjust"""
d = 'qwerty'
print(d.rjust(10)) #     qwerty
print(d.rjust(10, '-')) # ----qwerty
print(d.rjust(10, '&')) # &&&&qwerty
print(d.rjust(5, '!')) # !qwerty

"""Метод center"""
d = 'qwerty'
print(d.center(10)) #   qwerty  
print(d.center(12, '!')) # !!!qwerty!!!
print(d.center(13, '?')) # ????qwerty???
print(d.center(5, '!')) # qwerty

"""Метод zfill"""
d = '123'
print(d.zfill(5)) # 00123
print(d.zfill(6)) # 000123
print(d.zfill(2)) # 123
print(d.zfill(3)) # 123
print('0.123'.zfill(6)) # 00.123