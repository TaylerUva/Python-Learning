from uva_libs import hello, goodbye
hello(__file__)

num1 = 5
num2 = 2

quotient = num1 / num2
print("The quotient of", num1, "and", num2, "is", quotient)

# Swap num1 and num2
temp = num1
num1 = num2
num2 = temp

quotient = num1 / num2
print("The quotient of", num1, "and", num2, "is", quotient)

goodbye(__file__)
