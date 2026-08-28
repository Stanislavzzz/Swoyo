# if условие:
#     x = A
# else:
#     x = B
#
#
# x = A if условие else B


res = []
for x in range(1, 11):
    if x % 2 == 0:
        res.append(x)
    else:
        res.append(x * 2)
print(res)


result = [str(x) if x % 2 == 0 else x * 2 for x in range(1, 11) if x % 5 != 0]
print(result)
