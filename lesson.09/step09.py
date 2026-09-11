import re


# my_str = "Process finished with exit code 0  Process finished with exit code 0 Документы пришлите на почту bob@mail.ru или mary@gmail.com"
# my_pattern = r'\w+@\w+\.\w+'
#
# res = re.findall(my_pattern, my_str)
# print(res)


my_str = "Process finished with exit code 0 Позвоните по +7-987-654-32-10 или 8-800-555-44-33 Process finished with exit code 0 Документы пришлите на почту bob@mail.ru или mary@gmail.com"
my_pattern = r'(?:\+7|8)-?\d{3,}-?\d{3}-?\d{2}-?\d{2}'

res = re.findall(my_pattern, my_str)
print(res)