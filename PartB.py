from PartA import tokenize

"""
This function runs in O(n + m), where n is the number of characters in
the first file after it's inputted and m is the number of characters in 
the second file. 
"""
def compare_tokens():
    flag = True
    tokens_a = []
    tokens_b = []

    # retrieve file inputs and tokenize the text files
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
        except FileNotFoundError:
            path2 = input("Invalid path. Please try again: ")

    # count intersection between the two token lists
    count = len(set(tokens_a).intersection(tokens_b))

    return count