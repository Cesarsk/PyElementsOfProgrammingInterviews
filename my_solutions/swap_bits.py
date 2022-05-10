from test_framework import generic_test


# brute-force approach
# time complexity is O(1) independent of the word size
def swap_bits(x, i, j):
    # Extract the i-th and j-th bits, and see if they differ
    if (x >> i) & 1 != (x >> j) & 1:
        # i-th and j-th differ. Let's swap them by flipping their values

        # select the bit to flips with the bit mask
        bit_mask = (1 << i) | (1 << j)

        # flip the bits using the XOR operation
        x = x ^ bit_mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
