def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
        return file_text


def count_words_in(filepath):
    text = get_book_text(filepath)
    return len(text.split())


def character_counter_for(filepath):
    text = get_book_text(filepath)
    counter_dict = {}
    for character in list(text.lower()):
        if character in counter_dict.keys():
            counter_dict[character] += 1
        else:
            counter_dict[character] = 1

    return counter_dict


def split_dict(input_dict):
    new_list = []
    for key, value in input_dict.items():
        new_list.append({"char": key, "num": value})
    new_list.sort(reverse=True, key=lambda x: x["num"])
    return new_list
