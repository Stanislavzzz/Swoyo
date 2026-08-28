def my_generator():
    print("Шаг 1")
    yield 10
    print("Шаг 2")
    yield 20
    print("Шаг 3")
    yield 30
    # return None


gen = my_generator()
# res1 = next(gen)
# print(res1 + 100)
# print(next(gen))
# print(next(gen))
# # print(next(gen))


for word in gen:
    print(word)