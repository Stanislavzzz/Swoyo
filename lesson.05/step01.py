# for i in range(10):
#     print(i)
#


numbers = [10, 20, 30, 40]

iterator = iter(numbers)
# print(iterator)
# print(type(iterator))
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

is_running = True
while is_running:
    try:
        val = next(iterator)
        print(val)
    except StopIteration:
        # break
        is_running = False
else:
    print('OK')


#
# text = "Python"
# it = iter(text)
# print(next(it))
#
#
# data = {"a": 1, "b": 2}
# it = iter(data)
# print(next(it))