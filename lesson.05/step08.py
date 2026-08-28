# res = []
# for x in range(1, 31):
#     if x % 2 != 0:
#         res.append(x)
# print(res)


result = (x for x in range(1, 11) if x % 2 != 0)
print(type(result))
print(result)

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
