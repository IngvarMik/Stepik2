"""islower метод"""
print(''.islower())#False
print('abcdefg', 'abcdefg'.islower())# abcdefg True
print('abcDefG', 'abcDefG'.islower())# abcDefG False
print('qwerty!', 'qwerty!'.islower())# qwerty! True
print('12345', '12345'.islower())# 12345 False
print('12345abc', '12345abc'.islower())# 12345abc True
print('12345aBc', '12345aBc'.islower())# 12345aBc False
"""isupper метод"""
print(''.isupper()) # False
print('ABCDEF', 'ABCDEF'.isupper()) # ABCDEF True
print('ABCdEF', 'ABCdEF'.isupper()) # ABCdEF False
print('QWERTY!', 'QWERTY!'.isupper()) # QWERTY! True
print('12345', '12345'.isupper()) # 12345 False
print('12345ZXC', '12345ZXC'.isupper()) # 12345ZXC True
print('12345ZxC', '12345ZxC'.isupper()) # 12345ZxC False
"""isdigit метод"""
print(''.isdigit()) # False
print('0123456789', '0123456789'.isdigit()) # 0123456789 True
print('0,1', '0,1'.isdigit()) # 0,1 False
print('qwerty', 'qwerty'.isdigit()) # qwerty False
print('12a45', '12a45'.isdigit()) # 12a45 False
"""Метод isalpha"""
print(''.isalpha()) # False
print('ЗемфиРа', 'ЗемфиРа'.isalpha()) # ЗемфиРа True
print('Я искала тебя', 'Я искала тебя'.isalpha()) # Я искала тебя False
print('Годами', 'Годами'.isalpha()) # Годами True
print('qwerty', 'qwerty'.isalpha()) # qwerty True
print('12a45', '12a45'.isalpha()) # 12a45 False
print('qwerty!', 'qwerty!'.isalpha()) # qwerty! False
"""Метод isalnum"""
print(''.isalnum()) # False
print('ЗемфиРа', 'ЗемфиРа'.isalnum()) # ЗемфиРа True
print('Я искала тебя', 'Я искала тебя'.isalnum()) # Я искала тебя False
print('Годами', 'Годами'.isalnum()) # Годами True
print('qwerty', 'qwerty'.isalnum()) # qwerty True
print('12a45', '12a45'.isalnum()) # 12a45 True
print('qwerty!', 'qwerty!'.isalnum()) # qwerty! False
"""Метод istitle"""
print(''.istitle()) # False
print('ЗемфиРа', 'ЗемфиРа'.istitle()) # ЗемфиРа False
print('Хочешь солнце', 'Хочешь солнце'.istitle()) # Хочешь солнце False
print('вместо лампы', 'вместо лампы'.istitle()) # вместо лампы False
print('Хочешь', 'Хочешь'.istitle()) # Хочешь True
print('За Окошком Альпы?', 'За Окошком Альпы?'.istitle()) # За Окошком Альпы? True
print('12345', '12345'.istitle()) # 12345 False
