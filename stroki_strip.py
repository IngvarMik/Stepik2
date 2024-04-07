"""Метод strip"""
q = '   hello   '
print(q) #   hello 
print(q.strip()) # hello
print('\n\n\n_USB_\n\n\n\n'.strip()) # _USB_
print('123_USB_123'.strip('123')) # _USB_

"""Метод rstrip"""
q = '   hello   '
print(q) # hello
print(q.rstrip()) # hello
print('\n\n\n_USB_\n\n\n\n'.rstrip()) # _USB_
print('123_USB_123'.rstrip('123')) # 123_USB_
print('321232321_USB_31121312'.rstrip('123')) # 321232321_USB_

""" Метод lstrip"""
q = '   hello   '
print(q) # hello 
print(q.lstrip()) #  hello 
print('\n\n\n_USB_\n\n\n\n'.lstrip()) # _USB_
print('123_USB_123'.lstrip('123')) # _USB_123
print('321232321_USB_31121312'.lstrip('123')) # _USB_31121312