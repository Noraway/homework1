my_dict = {'Renata': 2002, 'Anastasia': 1977}
print('Словарь: ', my_dict)
print('Существующее значение: ', my_dict.get('Renata'))
print('Несуществующее значение: ', my_dict.get('Ruslan'))
my_dict.update({'Marton': 2002, 'Daniel': 1997})
print('Удаленное значение: ', my_dict.pop('Anastasia'))
print('Измененный словарь: ', my_dict)

print() # Отступ
my_set = {1, 12, 'Персик', 3.3, 1, 1, 1, 7.777, 3.3, 'Персик', 'Картошка'}
print('Множество: ', my_set)
my_set.add('Пирожок')
my_set.add((118, 39))
my_set.discard(3.3)
print('Измененное множество: ', my_set)