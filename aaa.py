def factorial(n):
    sum = 1
    for i in range(n, 0, -1):
        sum = sum * i
    yield sum


b =factorial(5)

for i in b:
    print(i)