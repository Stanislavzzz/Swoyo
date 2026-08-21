text_hello = "Привет, Мир!"
print(text_hello)
print()
# list_text = list(text_hello)
# print(list_text)
# list_text[1] = 'q'
# print(list_text)
# # new_text = str(list_text)
# # print(new_text)
# new_text = ''.join(list_text)
# print(new_text)
# print()


new_text = text_hello[:1] + 'q' + text_hello[2:]
print(new_text)

new_text_1 = f"{text_hello[:1]}q{text_hello[2:]}"
print(new_text_1)