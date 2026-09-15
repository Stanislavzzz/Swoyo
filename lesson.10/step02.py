file_object = open('users_w.txt', mode='w', encoding='utf-8')

info_1 = "Домашнее задание. Стандартная библиотека Python 1\n"
info_2 = "Домашнее задание. Стандартная библиотека Python 2\n"
file_object.write(info_1)
file_object.write(info_2)

# print(data)
file_object.close()



