# Question 13: Print multiplication table form 1 to 10

for i in range(1, 11):
    num_string = ""
    for x in range(1, 11):
        num_string = num_string + (str(i*x) + " ")
    print(num_string)