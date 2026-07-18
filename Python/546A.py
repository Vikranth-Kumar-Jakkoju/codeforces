k, n, w = map(int, input().split())

cost = (w * (w + 1)) // 2
cost = cost * k

if cost - n > 0 :
    print(cost - n)
else :
    print(0)