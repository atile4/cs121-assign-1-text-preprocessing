def tokenize(path : str) -> list[str]:
    tokens = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                curr_line = line

                # tokenize curr line
                cleaned = ''.join(c if c.isalnum() else ' ' for c in curr_line)
                words = cleaned.split()

                for word in words: tokens.append(word.lower().strip())

    except:
        raise FileNotFoundError("Could not find file")

    return tokens