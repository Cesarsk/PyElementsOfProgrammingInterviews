from test_framework import generic_test


def snake_string(s: str) -> str:
    l1, l2, l3 = [], [], []
    in_l1 = True
    for i in range(len(s)):
        if i % 2 == 0:
            l2.append(s[i])
        else:
            if in_l1:
                l1.append(s[i])
            else:
                l3.append(s[i])
            in_l1 = not in_l1

    print(l1, l2, l3)
    return "".join(l1 + l2 + l3)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
