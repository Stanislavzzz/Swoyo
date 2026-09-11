import random


num = random.randint(1, 2)
print(num)
num = random.random()
print(num)
num = random.uniform(1, 10)
print(num)

names = ['Bob', 'Alice', 'Bob1', 'Alice1', 'Mary', 'Anna']
print(id(names))
print(random.choice(names))
print(random.choices(names, k=3))
print(random.sample(names, k=5))

random.shuffle(names)
print(names)
print(id(names))