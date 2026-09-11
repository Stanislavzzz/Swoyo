import re


# r'\d\d'
text = '123 cat ancatd catdog'
re_ex = r'cat'

# res = re.match(re_ex, text)
# if res:
#     print(res.group())

# res = re.search(re_ex, text)
# if res:
#     print(res.group())

res = re.findall(re_ex, text)
print(res)