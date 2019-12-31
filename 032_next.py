myList = [1, 2, 3]
for i in iter(myList):
    print(i)
for i in myList:
    print(i)

def myRange(n):
    i = 0
    while i < n:
        yield i
        i += 1
for i in myRange(10):
    print(i)


def genDecDigs(cntDigits, maxDigit):
    if cntDigits > 0:
        for nowDigit in range(maxDigit + 1):
            for tail in genDecDigs(cntDigits - 1, nowDigit):
                yield nowDigit * 10 ** (cntDigits - 1) + tail
    else:
        yield 0


print(*genDecDigs(2, 3))

