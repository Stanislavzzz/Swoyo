file_object = open('users.txt', mode='r', encoding='utf-8')

# print(file_object)
# print(type(file_object))

data = file_object.read()
print(data)
file_object.close()



