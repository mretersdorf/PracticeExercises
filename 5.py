# Question 5: Given a list of numbers, return True if first and last number of a list is same

def compare_first_and_last(list_of_nums):
    if list_of_nums[0] == list_of_nums[-1]:
        return True
    else:
        return False

nums = [12, 23, 45,34, 236, 65, 34, 76, 12]
if compare_first_and_last(nums):
    print("The first and last numbers of the list are the same")
else:
    print("The first and last numbers of the list are not the same")