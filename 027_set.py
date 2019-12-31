mySet = {3, 1, 2}
print(mySet)

firstSet = {1, 2, 1, 3}
secondSet = {3, 2, 1}
print(firstSet == secondSet)

setFromList = set([1, 2, 3])
print(setFromList)
setFromTuple = set((4, 5, 6))
print(setFromTuple)
setFromStr = set("lol")
print(setFromStr)
setFromRange = set(range(2, 22, 3))
print(setFromRange)
setFromMap = set(map(abs, (1, 2, 3, -2, -4)))
print(setFromMap)
setFromSet = set({1, 2, 3})
print(setFromSet)

mixedSet = {1, 3.14, (1, 2, 3), "i have no idea why i'm here"}
print(mixedSet)

mySet = {'abba', 'a', 'long string'}
print(', '.join(mySet))
print(', '.join(sorted(mySet)))

emptySet = set()

mySet = {1, '2', 2, '1'}
for elem in mySet:
    print(elem, end=' ')

mySet = {1, 2, 3}
if 1 in mySet:
    print('1 in set')
else:
    print('1 not in set')
x = 42
if x not in mySet:
    print('x not in set')
else:
    print('x in set')