text_hello_1 = "Привет', Мир!"
text_hello_2 = 'Привет,"" Мир!'
text_hello_3 = """Привет', "  
   123
       qwerty
Мир!"""
text_hello_4 = '''Привет, Мир!'''

print(text_hello_1)
print(text_hello_2)
print(text_hello_3)
print(text_hello_4)

text_char = 'a'
print(text_char)
print(type(text_char))

num = 100
text_hello_5 = f'''Привет, {num + 10}  Мир!'''
print(text_hello_5)
print(type(text_hello_5))