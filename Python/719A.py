import itertools

a, b = map(int, input().split())

for y in itertools.count(start=1) :
    a *= 3
    b *= 2
    if a > b :
        print(y)
        break