# Question 11: Write a code to extract each digit from an integer, in the reverse order

def revers_digits(n):
    str_n = str(n)
    new_str = ""
    for i in reversed(str_n):
        new_str = new_str + i + " "
    return new_str


number = int(input("Please provide a number to reverse:"))
reverse = revers_digits(number)
print("The reversed number is: " + reverse)
