from itertools import combinations

nums = list(map(int, input().split()))
combs = combinations(range(len(nums)), 3)
print(max(map(lambda x: nums[x[0]] * nums[x[1]] * nums[x[2]], combs)))

from functools import partial

binStrToInt = partial(int, base=2)
print(binStrToInt('10010'))

from functools import reduce

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(reduce(gcd, map(int, input().split())))

from itertools import accumulate

print(*accumulate(map(int, input().split()), max))