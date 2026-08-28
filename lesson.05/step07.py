res = {}
for x in range(1, 11):
    if x % 2 == 0:
        res[x] = x
    else:
        res[x] = x * 2
print(res)


result = {x: x if x % 2 == 0 else x * 2  for x in range(1, 11) if x % 2 == 0}
print(result)
