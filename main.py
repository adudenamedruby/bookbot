from stats import character_counter_for
from stats import count_words_in
from stats import split_dict


def pretty_print(filepath):
    count = count_words_in(filepath)
    dict = character_counter_for("./books/frankenstein.txt")
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
    print(pretty_print("books/frankenstein.txt"))


main()
