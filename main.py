from stats import character_counter_for
from stats import count_words_in
from stats import split_dict

import sys


def pretty_print(filepath):
    count = count_words_in(filepath)
    dict = character_counter_for(filepath)
    count_string = ""
    for item in split_dict(dict):
        count_string += f"{item['char']}: {item['num']}\n"

    final_string = (
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {filepath}...\n"
        "----------- Word Count ----------\n"
        f"Found {count} total words\n"
        "--------- Character Count -------\n"
        f"{count_string}"
    )

    return final_string


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print(pretty_print(filepath))


main()
