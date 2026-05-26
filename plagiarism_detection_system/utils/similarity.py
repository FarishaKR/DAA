
def calculate_similarity(text, pattern):

    total_words = len(text.split())

    matched_words = text.count(pattern)

    if total_words == 0:
        return 0

    similarity = (matched_words / total_words) * 100

    return round(similarity, 2)