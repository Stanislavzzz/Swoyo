file_object = open('users_w.txt', mode='w', encoding='utf-8')

info_1 = "Домашнее задание. Стандартная библиотека Python 2\n"
info_2 = "Домашнее задание. Стандартная библиотека Python 3\n"

my_list = [info_1, info_2]
file_object.writelines(my_list)

# print(data)
file_object.close()



