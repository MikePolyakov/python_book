lambda x: x**2

def sqr(x):
    return x**2

print(' '.join(map(lambda x: str(x**2), range(1, 101))))

n = int(input())
points = []
for i in range(n):
    point = tuple(map(int, input().split()))
    points.append(point)
points.sort(key=lambda point: point[0]**2 + point[1]**2)
for point in points:
    print(' '.join(map(str, point)))

def traditionalSqr(x):
    return x**2

lambdaSqr = lambda x: x**2
print(traditionalSqr(3))
print(lambdaSqr(3))