res = set()
for x in range(1, 11):
    if x % 2 == 0:
        res.add(x)
    else:
        res.add(x * 2)
print(res)


result = {x if x % 2 == 0 else x * 2 for x in range(1, 11)}
print(result)
