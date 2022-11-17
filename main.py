# 1 Задание

user = [
    {"name": "John", "age": 15},
    {"name": "Proper", "age": 21},
    {"name": "Alik", "age": 58},
    {"name": "Jack", "age": 9}
]

# а) Создать список и поместить туда имя самого молодого человека.
#  Если возраст совпадает - поместить все имена самых молодых.

age_min = user[0]['age']
my_list = []
for i in user:
    if i['age'] < age_min:
        age_min = i['age']
for i in user:
    if i['age'] == age_min:
        my_list.append(i['name'])
print(my_list)

# б) Создать список и поместить туда самое длинное имя.
# Если длина имени совпадает - поместить все такие имена.

name_max = user[0]['name']
my_list = []
for i in user:
    if i['name'] > name_max:
        name_max = i['name']
for i in user:
    if i['name'] == name_max:
        my_list.append(i['name'])
print(my_list)

# в) Посчитать среднее количество лет всех людей из начального списка.

my_list = []
for i in user:
    my_list.append(i["age"])
my_list = int(sum(my_list) / len(my_list))
print(my_list)

# 2 Задание

my_dict_1 = {
    1: 1,
    2: 4,
    10: 152,
    93: 23,
    23: 223,
    11: 11
}
my_dict_2 = {
    5: 1,
    2: 24,
    6: 152,
    10: 99,
    93: 223,
    11: 11
}

# а) Создать список из ключей, которые есть в обоих словарях.

my_list1 = []
for element in my_dict_1:
    if element in list(my_dict_2.keys()):
        my_list1.append(element)
print(my_list1)

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

my_list2 = []
for element in my_dict_1:
    if element not in list(my_dict_2.keys()):
        my_list2.append(element)
print(my_list2)

# в) Создать новый словарь из пар {ключ:значение},
# для ключей, которые есть в первом, но нет во втором словаре.

new_list = {}
for element in my_dict_1:
    if element not in list(my_dict_2.keys()):
        new_list[element] = my_dict_1[element]
print(new_list)
