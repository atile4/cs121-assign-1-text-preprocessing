from PartA import tokenize

def compare_tokens():
    flag = True
    tokens_a = []
    path1 = input("Please input the first file's path: ")
    while (flag):
        try:
            tokens_a = tokenize(path1)
            flag = False
        except FileNotFoundError:
            input("Invalid path. Please try again.")

    flag = True
    path2 = input("Please input the second file's path: ")
    while (flag):
        try:
            tokens_b = tokenize(path2)
            flag = False
        except:
            input("Invalid path. Please try again.")

    count = len(set(tokens_a).intersection(tokens_b))

    return count
