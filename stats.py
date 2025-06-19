def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    char_counts = {}

    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def get_sorted_char_frequencies(char_counts):
    """
    Return a list of dictionaries sorted by count in descending order,
    each dictionary containing a character and its frequency.
    Only alphabetical characters are included.
    """
    char_frequencies = []

    for char, count in char_counts.items():
        if char.isalpha():
            char_frequencies.append({"char": char, "num": count})

    char_frequencies.sort(key=lambda item: item["num"], reverse=True)

    return char_frequencies
