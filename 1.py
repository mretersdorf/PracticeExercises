# Question 1: Given a two integer numbers print their product and  if the product is greater than 1000, then print
# their sum

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

def two_integers(number1, number2):
    product = number1 * number2
    if product > 1000:
        integer_sum = number1 + number2
        print("The product is greater than 1000, so the sum of the numbers is: ", integer_sum)
    elif product <= 1000:
        print("The product of 1 and 2 is: ", product)


two_integers(number1, number2)