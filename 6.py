# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

def iterate_list(list_of_nums):
    for x in list_of_nums:
        if x % 5 == 0:
            print(x)


nums = [23, 45, 76, 12, 11, 10, 125, 6655, 90, 93]
iterate_list(nums)