# Question 3: Given a string, display only those characters which are present at an even index number.

def even_string(word):
    print("The characters at even index numbers are: ")
    for i in range(0, len(word)-1, 2):
        print("index: " + str(i) + " is: " + word[i])


word = input("Please provide a string: ")
even_string(word)
