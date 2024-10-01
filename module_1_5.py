immutable_var = 1, 2, 3.3, 'hello', True
print('Неизменяемый кортеж: ', immutable_var)
# immutable_var[0] = 4
# Строка сверху приводит к ошибке.
# Кортеж не поддерживает изменение элементов, в отличие от списка.
mutable_list = list(immutable_var)
mutable_list[3] = 'modified'
print('Изменяемый список: ', mutable_list)