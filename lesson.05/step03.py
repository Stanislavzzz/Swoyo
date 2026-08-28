# res = []
# for x in range(1, 31):
#     if x % 2 != 0:
#         res.append(x)
# print(res)
#
#
# result = [x for x in range(1, 31) if x % 2 != 0]
# print(result)


words = ["hello", "", "python", "", "world"]
res = []
for word in words:
    if word:
        res.append(word)
print(res)

result = [word for word in words if word]
print(result)