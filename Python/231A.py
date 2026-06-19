n = int(input())
np = 0

for i in range(n) :
    inp = input()
    c = int(inp[0])
    c += int(inp[2])
    c += int(inp[4])
    if(c >= 2) :
        np+=1

print(np)

