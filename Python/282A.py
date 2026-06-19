n = int(input())
num = 0

for i in range(n) :
    x = input()
    if(x[1] == '+') :
        num += 1
    elif(x[1] == '-') :
        num -= 1

print(num)