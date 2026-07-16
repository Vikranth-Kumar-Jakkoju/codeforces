name = input()

distinct_characters = set(name)

if len(distinct_characters) % 2 == 0 :
    print("IGNORE HIM!")
else :
    print("CHAT WITH HER!")