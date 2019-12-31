def printList(myList, sep=' '):
    print(sep.join(map(str, myList)))

printList([1, 2, 3])
printList([3, 2, 1], sep='\n')

def mySum(*args):
    nowSum = 0
    for now in args:
        nowSum += now
    return nowSum

print(mySum(1, 2))
print(mySum(1, 2, 3, 4))

def myMin(first, *others):
    nowMin = first
    for now in others:
        if now < nowMin:
            nowMin = now
    return nowMin

print(myMin(1))
print(myMin(3, 1, 2))