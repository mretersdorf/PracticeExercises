# Question 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.


def exponents(base, exp):
    return base**exp


base = int(input("Please provide a base number: "))
exp = int(input("Please provide an exponent: "))

print("The calculated value is: " + str(exponents(base, exp)))