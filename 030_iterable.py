"""
В языке Питон есть много функций, которые принимают в качестве параметра iterable
и могут сделать что-то полезное.
\С некоторыми из них, такими как sorted или map мы уже немного знакомы.
\Рассмотрим еще некоторые из них:

sum - находит сумму всех элементов iterable.

min, max - находит минимум и максимум в последовательности iterable.

map - умеет принимать более двух параметров. Например, такая запись map(f, iterA, iterB)
\вернет iterable со значениями f(iterA[0], iterB[0]), f(iterA[1], iterB[1]), ...

filter(predicate, iterable) - применяет функцию predicate ко всем элементам iterable и
 возвращает iterable, который содержит только те элементы, которые удовлетворяли предикаты (т.е. функция predicate вернула True). Например, так может выглядеть решение задачи о поиске минимального положительного элемента в списке:
"""

print(min(filter(lambda x: x > 0, map(int, input().split()))))

f = open('data.txt', 'r', encoding='utf8')
for i, line in enumerate(f):
    if line.strip() == '':
        print('Blank line at line', i)

print(all(map(lambda x: abs(int(x)) <= 100, input().split())))

input()  # Пропускаем количества, обойдемся без них
people = map(int, input().split())
sortedPeople = sorted(enumerate(people), key=lambda x: x[1])
taxi = map(int, input().split())
sortedTaxi = sorted(enumerate(taxi), key=lambda x: x[1], reverse=True)
ans = zip(sortedPeople, sortedTaxi)
sortedAns = sorted(ans, key=lambda x: x[0][0])
print(*map(lambda x: x[1][0], sortedAns))

input()  # Пропускаем количества, обойдемся без них
print(
    *map(
        lambda x: x[1][0],
        sorted(
            zip(
                sorted(
                    enumerate(map(int, input().split())),
                    key=lambda x: x[1]
                ),
                sorted(
                    enumerate(map(int, input().split())),
                    key=lambda x: x[1],
                    reverse=True
                )
            ),
            key=lambda x: x[0][0]
        )
    )
)