# Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the
# current number and previous number


def sum_range(number):
    for current in range(number):
        if current <= 0:
            previous = 0
        else:
            previous = current - 1
        last_2_sum = current + previous
        print("Current: " + str(current) + " Previous: " + str(previous) + " Sum: " + str(last_2_sum))


sum_range(10)
