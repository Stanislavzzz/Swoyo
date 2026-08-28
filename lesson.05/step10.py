def fact_gen(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result
        print(1111)


for value in fact_gen(5):
    print(value)