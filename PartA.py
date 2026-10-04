def tokenize(path : str) -> list[str]:
    tokens = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # tokenize curr line
                cleaned = ''.join(c if c.isalnum() else ' ' for c in line.lower())

                tokens.extend(cleaned.split())

    except:
        raise FileNotFoundError("Could not find file")

    return tokens

def computeWordFrequencies(tokens : list[str]) -> dict[str, int] :
    result = {}
    for token in tokens:
        if token not in result.keys():
            result[token] = 1
        else:
            result[token] += 1

    result = dict(sorted(result.items(), key=lambda item: (-item[1], item[0])))

    return result


def print_map(map : dict[str, int]) -> None :
    for token, freq in map.items():
        print(token + "\t" + str(freq))