'''
Задача 1

Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]

result = []

for item in lst:
    if lst.count(item) > 1 and item not in result:
        result.append(item)

print(f'{lst=}')
print(f'{result=}')