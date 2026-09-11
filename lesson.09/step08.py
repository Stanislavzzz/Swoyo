import re


# r'\d\d'
text = 'Мой номер 123-45-67  cat ancatd  78901234catdog'
re_ex = r'\d+'


res = re.findall(re_ex, text)
print(res)