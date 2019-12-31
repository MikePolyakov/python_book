n = int(input())
fact = 1
i = 2
while i <= n:
    fact *= i
    i += 1
print(fact)


def factorial(num):
    fact = 1
    i = 2
    while i <= num:
        fact *= i
        i += 1
    return fact

n = int(input())
print(factorial(n))

print(factorial(n) // (factorial(k) * factorial(n - k)))

def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))