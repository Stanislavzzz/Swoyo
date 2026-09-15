# file_object = open('users.txt', mode='r', encoding='utf-8')
# data1 = file_object.readlines()
# file_object.close()
# print(data1)


with open('users.txt', mode='r', encoding='utf-8') as file_object:
    data1 = file_object.readlines()

print(data1)

