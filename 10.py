# Question 10: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list


def combine_lists(list1, list2):
    new_list = []
    for i in list1:
        if i % 2 == 1:
            new_list.append(i)
    for x in list2:
        if x % 2 == 0:
            new_list.append(x)
    return new_list


list1 = [2, 12, 3456, 43, 23, 56, 78, 33, 77]
list2 = [4, 34, 56, 78, 55, 34, 78, 55, 99, 87]

print("List 1: ", list1)
print("List 2: ", list2)
print("New list with odds from list1 and evens from list2: ", combine_lists(list1, list2))
