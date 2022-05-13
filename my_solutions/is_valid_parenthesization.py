from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    part = []
    match = {
        '(': ')', ')': '(',
        '[': ']', ']': '[',
        '{': '}', '}': '{'
    }

    for token in s:
        if not len(part):
            part.append(token)
        else:
            if part[-1] == match[token]:
                part.pop()
            else:
                part.append(token)

    return len(part) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
