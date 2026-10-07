from PartA import tokenize

"""
This function runes in O(n + m), where n is the number of characters in
the first file after it's inputted and m is the number of characters in 
the second file. 

tokenize(), assuming the user inputs correct file paths, runs in linear time,
and the functions within tokenize(), extend() and split() are also linear relative
to the length of each line. 
Across all of this, it's O(# of chararcters in file) complexity. tokenize() is called
twice, so it would be the count of characters for both files.

When intersecting the tokens, converting tokens_a to a set takes O(len(tokens_a)), and intersecting
into tokens_b would take O(len(tokens_b)). These operations rae dominated by the tokenize() functions, so
they will be negligble.
"""
def compare_tokens():
    flag = True
    tokens_a = []
    path1 = input("Please input the first file's path: ")
    while (flag):
        try:
            tokens_a = tokenize(path1)
            flag = False
        except FileNotFoundError:
            path1 = input("Invalid path. Please try again: ")

    flag = True
    path2 = input("Please input the second file's path: ")
    while (flag):
        try:
            tokens_b = tokenize(path2)
            flag = False
        except:
            path2 = input("Invalid path. Please try again: ")

    count = len(set(tokens_a).intersection(tokens_b))

    return count
