import sys

from stats import (
    get_num_words,
    get_char_count,
    get_sorted_char_frequencies,
)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def print_report(filepath, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


def main(filepath):
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    counter = get_char_count(text)
    sorted_chars = get_sorted_char_frequencies(counter)
    print_report(filepath, num_words, sorted_chars)

   
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    main(filepath)
