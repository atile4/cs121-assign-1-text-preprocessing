"""
tokenize(path : str) -> list[str]

This function runs in O(n) time, where n is the number of lines in the file. 


"""
def tokenize(path : str) -> list[str]:
    # list containing all resulting tokens
    tokens = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # tokenize curr line
                cleaned = ''.join(c if c.isalnum() else ' ' for c in line.lower())

                # add tokens in the current line to tokens list
                tokens.extend(cleaned.split())

    except:
        raise FileNotFoundError("Could not find file")

    return tokens

"""
This function, computeWordFrequencies(), runs in O(n + m log m), where
n is the length of tokens and k is the number of unique tokens, and k <= n.
The for loop runs once for each token and sorting the dictionary 
takes O(k log k time). 

The function would be in its worst case if all tokens are unique, in 
which case k = n and the runtime would be O(n + nlogn).

"""
def computeWordFrequencies(tokens : list[str]) -> dict[str, int] :
    # resulting freq map
    result = {}

    # add tokens to frequency map
    for token in tokens:
        result[token] = result.get(token, 0) + 1

    # sort dictionary by value desc and alphabetically
    result = dict(sorted(result.items(), key=lambda item: (-item[1], item[0])))

    return result

"""
The function runs in O(n) time, where n is the number of key value pairs 
in the dictionary. It loops through each pair once to print out
its contents. 
"""
def print_map(map : dict[str, int]) -> None :
    for token, freq in map.items():
        print(token + "\t" + str(freq))