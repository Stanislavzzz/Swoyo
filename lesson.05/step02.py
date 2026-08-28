# res = []
# for x in range(1, 11):
#     res.append(x * 2)
# print(res)
#
#
# result = [x * 2 for x in range(1, 11)]
# print(result)

text = "Python"
res = []
for letter in text:
    res.append(ord(letter))
print(res)


result = [ord(letter) + 100 for letter in text]
print(result)