name_1 = 'Bob'
name_2 = 'Ivan'
name_3 = 'Mary'
name_4 = 'Alice'

names = [name_1, name_2, name_3, name_4, 'Serj', 'Petr']
# names_my = list()

print(names)
print(type(names))
print(id(names))

# names.append('Anna')
# names.insert(1, 'Anna')
new_names = ['Kirill', 'Andrey']
names.extend(new_names)
print(names)
print(id(names))



