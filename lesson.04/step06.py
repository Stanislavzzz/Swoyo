# print()
# print(1)
# print(2, 5, 6, 7)
# print(1, 4, 6, 8, 3, 1, 2)

#
# def greeting(user_name, age, profession):
#     print(f'Привет, {user_name}')
#
#
# greeting('Bob')


# def sum_numbers(*args, **kwargs):
def sum_numbers(name, *args, **kwargs):
    print(name)
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

    # for number in args:
    #     print(number)
    # return sum(args)



# print(sum_numbers(1, 2, 3, 4, 5, num=10, age=30))
# print(sum_numbers(1, 2, 3, city='Moscow'))
# print(sum_numbers(1, 2))
# print(sum_numbers(1, 2, 6, 7, 8, 9, 10))
print(sum_numbers("Bob", 123, 345))