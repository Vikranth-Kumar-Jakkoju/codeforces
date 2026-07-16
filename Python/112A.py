string1 = input()
string2 = input()

string1 = string1.lower()
string2 = string2.lower()

if string1 == string2 :
    print(0)
else :
    for i in range(len(string1)) :
        if string1[i] > string2[i] :
            print(1)
            break
        elif string1[i] < string2[i] :
            print(-1)
            break