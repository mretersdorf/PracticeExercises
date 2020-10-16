# Question 9: Reverse a given number and return true if it is the same as the original number


def reverse_num(n):
    reverse_n = ""
    num_str = str(n)
    for i in reversed(num_str):
        reverse_n = reverse_n + i
    return int(reverse_n)


number = int(input("Please provide a number: "))
print("The reverse of that number is: " + str(reverse_num(number)))
