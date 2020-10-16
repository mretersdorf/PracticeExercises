# Question 14: Print downward Half-Pyramid Pattern with Star (asterisk)

def print_asterisks(num):
    for i in range(num, 0, -1):
        print(("* ")*i)


asterisk_num = int(input("How many asterisks would like in your first line: "))
print_asterisks(asterisk_num)