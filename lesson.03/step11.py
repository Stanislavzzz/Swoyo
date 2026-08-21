text_hello = "Провивет, миров!"
print(text_hello)

if "Мир".lower() in text_hello.lower():
    print("OK")
else:
    print("No")


# print(text_hello.find("ров!"))
# print(text_hello.rfind("р"))
# print(text_hello.rfind("йцуке"))
# print()

# print(text_hello.index("ров!"))
# print(text_hello.rindex("р"))
# print(text_hello.index("йцуке"))
# print()

print(text_hello.count("123"))
print(text_hello.startswith("Пр"))
print(text_hello.endswith("123"))