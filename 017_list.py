myList = [1, 2, 3]
myList[1] = 4
print(myList)

a = [1, 2]
b = a
b[0] = 3
print(a)

a = [1, 2]
b = [1, 2]
a[0] = 3
print(b)

a = [1, 2]
b = a
a = [3, 4]
print(b)


def replaceFirst(myList):
    myList[0] = 'x'


nowList = list('abcdef')
replaceFirst(nowList)
print(nowList)


def reverseList(funcList):
    funcList = funcList[::-1]


mainList = list('abc')
reverseList(mainList)
print(mainList)

"""
К переменным типа список можно применять методы, перечислим некоторые из них:

Методы, не изменяющие список и возвращающие значение:

count(x) - подсчитывает число вхождений значения x в список. Работает за время O(N)

index(x) - находит позицию первого вхождения значения x в список. Работает за время O(N)

index(x, from) - находит позицию первого вхождения значения x в список, начиная с позиции from. 
\Работает за время O(N)

Методы, не возвращающие значение, но изменяющие список:

append(x) - добавляет значение x в конец списка

extend(otherList) - добавляет все содержимое списка otherList в конец списка. 
\В отличие от операции + изменяет объект 
\к которому применен, а не создает новый

remove(x) - удаляет первое вхождение числа x в список. Работает за время O(N)

insert(index, x) - вставляет число x в список так, что оно оказывается на позиции index. 
\Число, стоявшее на позиции index и все числа правее него сдвигаются на один вправо. Работает за время O(N)

reverse() - Разворачивает список (меняет значение по ссылке, а не создает новый список как myList[::-1]). 
\Работает за время O(N)

Методы, возвращающие значение и изменяющие список:

pop() - возвращает последний элемент списка и удаляет его

pop(index) - возвращает элемент списка на позиции index и удаляет его. Работает за время O(N)
"""

numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers.pop(i)
print(' '.join(map(str, numbers)))

numbers = list(map(int, input().split()))
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        numbers.pop(i)
    else:
        i += 1
print(' '.join(map(str, numbers)))

numbers = list(map(int, input().split()))
newList = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        newList.append(numbers[i])
print(' '.join(map(str, newList)))