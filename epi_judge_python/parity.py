from test_framework import generic_test

# brute-force approach (time complexity: O(x))
def parity(x):
    # if the number of 1 is odd it's 1 else 0
    result = 0
    while x:
        result = result ^ (x & 1)
        x >>= 1

    return result


# let k be the number of bits set to 1 in a particular word, time complexity of the algorithm is O(k)
def parity_v2(x):
    # if the number of 1 is odd it's 1 else 0
    result = 0
    while x:
        result = result ^ 1
        x &= x - 1  # Drops the lowest set bit of x

    return result


def build_parity_cache(n):
    cache = []
    for i in range(pow(2, n)):
        cache.append(parity_v2(i))
    return cache


# Let L be the width of the words for which we cache the results, and n the word size. Since there are n/L terms,
# the time complexity is O(n/L), assuming word-level operations, such as shifting, take 0(1)
def parity_v3(x, pc):
    # explanation: https://www.youtube.com/watch?v=USsyntRZRxc

    # 16-bit mask
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF

    return (
            pc[x >> (3 * MASK_SIZE)] ^
            pc[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            pc[(x >> MASK_SIZE) & BIT_MASK] ^ pc[x & BIT_MASK]
    )


# refinement that exploits the XOR capability of being associative and commutative.
# i.e. parity(11010111) =  parity(1101) XOR parity(0111) = parity(11) XOR parity(01) XOR parity(01) XOR parity(11)
# time complexity is O(log(n)) where n is the word size
# works for a 64-bit long word
def parity(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
