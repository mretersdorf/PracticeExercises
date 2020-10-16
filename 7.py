# Question 7: Return the total count of sub-string “Emma” appears in the given string


def string_counter(prime_string, sub_string):
    return primary_string.count(sub_string)

primary_string = input("Please provide a primary string: ")
sub_string = input("Please provide a sub string: ")

print("The number of instances the sub-string is in the primary string is: "
      + str(string_counter(primary_string, sub_string)))

