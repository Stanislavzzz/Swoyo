my_list = [3, 5, 7, 4, 2]

new_text_1 = f"{max(my_list)} - {len(my_list)} {100+ 10 / 2}"
print(new_text_1)


name = "Bob"
age = 20
new_text_2 = f"{name} - {age}"
print(new_text_2)

# new_text_2 = "{name} - {age}".format(name=name, age=age)
new_text_2 = "{} - {}".format(name, age)
print(new_text_2)