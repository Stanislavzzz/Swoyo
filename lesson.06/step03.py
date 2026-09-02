class Greeter:
    def greet_world(self):
        print("Hello, world!")

    def greet_user(self, name='Bob', age=30):
        print(f"Hello, {name}, {age}!")


g = Greeter()
g.greet_world()
g.greet_user()

y = Greeter()
y.greet_world()
y.greet_user(name='Anna')