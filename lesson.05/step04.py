# a = [1, 2]
# b = [10, 20]
#
# res = []
# for num in a:
#     for num2 in b:
#         res.append((num, num2))
# print(res)
#
#
# result = [(num, num2) for num in a for num2 in b]
# print(result)

#
# res = []
# for num in range(1, 4):
#     for num2 in range(1, 5):
#         if num != num2:
#             res.append(f"{num} * {num2} = {num * num2}")
# print(res)
#
#
# result = [f"{num} * {num2} = {num * num2}" for num in range(1, 4) for num2 in range(1, 5) if num != num2]
# print(result)


# res = []
# for num in range(1, 4):
#     if num % 2 != 0:
#         for num2 in range(1, 5):
#             res.append(f"{num} * {num2} = {num * num2}")
# print(res)
#
#
# result = [f"{num} * {num2} = {num * num2}" for num in range(1, 4)  if num % 2 != 0 for num2 in range(1, 5)]
# print(result)