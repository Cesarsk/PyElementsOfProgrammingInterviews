from typing import List

from test_framework import generic_test


# <2,0,1>
# switch 1 with 0
# <2,1,0>

# <1,3,2> # move 2 to 1
# <2,1,3> 1,2,3, 2,1,3
def next_permutation(perm: List[int]) -> List[int]:
    # -1 because it's the length of array and -1 because it's the last but one element
    # it indicates the point you reverse the array
    inversion_point = len(perm) - 1 - 1

    # determine the inversion point which is the starting of the longest decreasing suffix
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
        inversion_point -= 1

    if inversion_point == -1:
        return []

    # scroll through the longest decreasing suffix
    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            # swap the two elements
            perm[i], perm[inversion_point] = perm[inversion_point], perm[i]
            break

    # finally resort decreasing the new longest decreasing suffix
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
