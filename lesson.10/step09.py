from pathlib import Path


my_path = Path('./data/user_data.txt')
#
# with open(my_path, mode='r', encoding='utf-8') as file_object:
#     data1 = file_object.readlines()
#
# print(data1)

print(my_path.name)
print(my_path.parent)
print(my_path.exists())
print(my_path.is_file())
print(my_path.is_dir())
print(my_path.resolve())