from typing import List

from test_framework import generic_test


def minimum_messiness(words, line_length):
    #
    num_remaining_blanks = line_length - len(words[0])
    # set messiness of the first word and the other word to inf, i.e. [64, inf, ..., inf]
    min_messiness = ([num_remaining_blanks ** 2] + [float('inf')] * (len(words) - 1))

    # scroll starting from the second word
    for i in range(1, len(words)):
        print()
        # a messiness of the word i is given by the messiness of the previous word + (line_length - len(words[i]))**2
        num_remaining_blanks = line_length - len(words[i])
        min_messiness[i] = min_messiness[i - 1] + num_remaining_blanks ** 2

        # try adding next words starting from the last word added
        for j in reversed(range(i)):
            print(words[j])
            num_remaining_blanks -= len(words[j]) + 1

            if num_remaining_blanks < 0:  # no space left on the line
                break

            first_j_messiness = 0 if j - 1 < 0 else min_messiness[j - 1]
            current_line_messiness = num_remaining_blanks ** 2
            min_messiness[i] = min(min_messiness[i], first_j_messiness + current_line_messiness)

    return min_messiness[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
