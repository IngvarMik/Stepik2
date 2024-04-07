"""JOIN пример"""
w = 'ivanov ivan ivanovich'
s = w.split()
print(s)
print('!'.join(s))

y = 'hello world'
print('&'.join(y))

words = ['London', 'is', 'the', 'capital', 'of', 'GB']
print(','.join(words))

"""Ниже перед вами представлен список list_strings, состоящий из строк. При помощи метода .join 
и соединителя - получите строку из этих элементов и выведите ее на экран
Sample Input:
Sample Output:
Follow-the-Cops-Back-Home"""
words = ['Follow', 'the', 'Cops', 'Back', 'Home']
print('-'.join(words))

"""или"""
list_strings = ['Follow', 'the', 'Cops', 'Back', 'Home'] 
print('-'.join(list_strings))