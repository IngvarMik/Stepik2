"""примеры действия split"""
print('1, 2, 3, 4, 5'.split(', '))
print('a->b->C->->d->e'.split('->'))
print('1      4      5'.split())
print('   a  b   c   '.split())
print('    '.split())
print('wwwww'.split('w'))
print('1, 2, 3, 4, 5'.split(', ', maxsplit=2))
print('a b C d e'.split(maxsplit=1))
print('a b C d e'.split(maxsplit=2))
print('a b C d e'.split(maxsplit=3))
S = input()
print(len(S.split()))# как узнать длину слова

