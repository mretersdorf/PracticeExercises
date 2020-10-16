# Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

def remove_chars(string, number):
    new_str = ""
    for i in range(0, len(string)-1, 1):
        if i > number - 1:
            new_str = new_str + string[i]
    return new_str

def remove_chars2(word, n):
    return word[n:]

word = input("Please provide a string: ")
number = int(input("Please provide an integer number: "))
new_str = remove_chars2(word, number)
print("The new string with " + str(number) + "characters removed from the beginning is: " + new_str)
