n = input()

count = 0
is_lucky = True

for i in n :
    if i == '4' or i == '7' :
        count = count + 1
    else :
        is_lucky = False

if is_lucky or (count == 4 or count == 7) :
    print("YES")
else :
    print("NO")