
def naive_search(text, pattern):

    positions = []

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):

        if text[i:i+m] == pattern:
            positions.append(i)

    return positions