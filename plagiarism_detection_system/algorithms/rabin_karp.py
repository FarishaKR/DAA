
def rabin_karp(text, pattern):

    positions = []

    n = len(text)
    m = len(pattern)

    pattern_hash = hash(pattern)

    for i in range(n - m + 1):

        window = text[i:i+m]

        if hash(window) == pattern_hash:

            if window == pattern:
                positions.append(i)

    return positions