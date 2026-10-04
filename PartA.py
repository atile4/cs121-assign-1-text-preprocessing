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