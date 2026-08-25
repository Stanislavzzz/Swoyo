def greeting(user_name="Guest"):
    print(f'Привет, {user_name}')


greeting('Bob')
greeting()


def update_dict(my_dict, key="city", value="Moscow"):
    new_dict = my_dict.copy()
    new_dict[key] = value
    return new_dict


info = {"name": "Bob", "age": 30}
print(info)
# new_info = update_dict(info, "city", "Moscow")
new_info = update_dict(my_dict=info)

print(info)
print(new_info)
