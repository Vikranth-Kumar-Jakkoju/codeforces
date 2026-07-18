word = input()

upper = 0
lower = 0

for letter in word :
    if ord(letter) >= ord('a') and ord(letter) <= ord('z') :
        lower = lower + 1
    else :
        upper = upper + 1

if lower >= upper :
    print(word.lower())
else :
    print(word.upper())