"""Программа получает на вход две строки, назовем их s и postfix. Напишите программу, которая проверяет 
заканчивается ли введенная фраза s строкой postfix 
Входные данные
В отдельных строках вводятся два значения: сперва строка s, затем строка postfix
Выходные данные
Нужно вывести True, если введенная строка s заканчивается строкой postfix , во всех остальных случаях 
нужно вывести False. Регистр букв нужно учитывать"""
s = input()# запрос s
postfix = input()# запрос второй строки
print(s.endswith(postfix))# применяем метод endswith - сравниваем окончание строк

"""Напишите программу, которая проверяет, чтобы введенная фраза s одновременно начиналась со строки prefix 
и заканчивалась строкой postfix 
Входные данные
В отдельных строках вводится три значения: сперва строка s, затем строка prefix и потом postfix
Выходные данные
Нужно вывести True, если введенная строка s одновременно начинается со строки prefix и 
заканчивается строкой postfix . Во всех остальных случаях нужно вывести False. Регистр букв нужно учитывать
Sample Input 1:
translate russian to english
translate
english
Sample Output 1:
True"""
s = input()
prefix = input()
postfix = input()
print(s.startswith(prefix),s.endswith(postfix))# выдает ответ true true

s = input()
prefix = input()
postfix = input()
print(s.startswith(prefix) and s.endswith(postfix))# выдает ответ true - приняли 
