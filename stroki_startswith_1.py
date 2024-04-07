"""Напишите программу, которая проверяет начинается ли введенная фраза строкой mam вне зависимости от
 регистра букв . В качестве ответа необходимо вывести True, если введенная строка начинается с mam, 
 во всех остальных случаях нужно вывести False
Sample Input 1:
MaMba
Sample Output 1:
True"""
a = input()
print(a.startswith('mam') or a.startswith('Mam') or a.startswith('mAm') or a.startswith('maM') or a.startswith('MAm') or a.startswith('MaM') or a.startswith('mAM') or a.startswith('MAM')) 