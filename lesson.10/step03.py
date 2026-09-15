file_object = open('users.txt', mode='r', encoding='utf-8')


# data1 = file_object.readline()
# print(data1)
# data2 = file_object.readline()
# print(data2)
# data3 = file_object.readline()
# print(data3)
# data4 = file_object.readline()
# print(data4)

# data1 = file_object.readlines()
# print(data1)

# for line in file_object:
#     print(line)


data1 = file_object.read(2)
print(data1)

data2 = file_object.read(4)
print(data2)





