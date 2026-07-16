equation = input()
equation = equation.split("+")
equation.sort(reverse=True)

print("+".join(equation))