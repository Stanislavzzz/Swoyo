# text_hello = "   Привет , мИр !   "
#
# print(text_hello.strip())
# print(text_hello.lstrip())
# print(text_hello.rstrip())
# print()

text_hello = "Провивет, Миров!"
new_text = text_hello[:1] + 'q' + text_hello[2:]
print(new_text)

new_text_1 = f"{text_hello[:1]}q{text_hello[2:]}"
print(new_text_1)

# new_text_2 = text_hello.replace("ров", "w")
new_text_2 = text_hello.replace("ров", "w", 1)
print(new_text_2)
