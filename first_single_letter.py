import collections


def get_first_single_letter(s):
    letter_dict = collections.defaultdict(int)
    for item in s:
        letter_dict[item] += 1

    for item in s:
        if letter_dict[item] == 1:
            return item

    return None



