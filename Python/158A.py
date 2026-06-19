n, k = map(int, input().split())
temp = input()
score = list(map(int, temp.split()))

k = score[k - 1]
count = 0

for x in score :
    if x > 0 and x >= k :
        count += 1

print(count)
