from PartA import tokenize
import sys
import os

"""
This function runs in O(n + m), where n is the number of characters in
the first file after it's inputted and m is the number of characters in 
the second file. 
"""
def compare_tokens(path1, path2):
    # tokenize the text files
    tokens_a = tokenize(path1)
    tokens_b = tokenize(path2)

    # count intersection between the two token lists
    return len(set(tokens_a).intersection(tokens_b))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: Use the format: python PartB.py <file1.txt> <file2.txt>")
        sys.exit(1)

    path1, path2 = sys.argv[1], sys.argv[2]

    for path in (path1, path2):
        if not os.path.isfile(path):
            print(f"Error: file not found: {path}")
            sys.exit(1)

    print(compare_tokens(path1, path2))