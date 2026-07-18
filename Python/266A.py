n = int(input())
stones = input()
count = 0

for i in range(1, n) :
    if stones[i - 1] == stones[i] :
        count = count + 1

print(count)