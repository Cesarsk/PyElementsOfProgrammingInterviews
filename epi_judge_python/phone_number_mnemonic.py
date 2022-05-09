from typing import List

from test_framework import generic_test, test_utils

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

# "26" # O(n*4**n) space O(4**n)
def phone_mnemonic(phone_number: str) -> List[str]:
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            mnemonics.append("".join(partial))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                partial[digit] = c
                phone_mnemonic_helper(digit + 1)

    mnemonics, partial = [], [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
