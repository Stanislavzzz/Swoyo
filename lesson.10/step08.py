with open('./data/user_data.txt', mode='r', encoding='utf-8') as file_object:
    data1 = file_object.readlines()

print(data1)


with open('/home/stanislav/PythonProject/SWOYO/lesson_m1_2026_08/data/user_data.txt', mode='r', encoding='utf-8') as file_object:
    data1 = file_object.readlines()

print(data1)


with open(r'c:\data\user_data.txt', mode='r', encoding='utf-8') as file_object:
with open(r'c:\\data\\user_data.txt', mode='r', encoding='utf-8') as file_object:
    data1 = file_object.readlines()

print(data1)
