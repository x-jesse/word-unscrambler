from itertools import permutations
from enchant import Dict


def unscramble(word):
    d = Dict("en_US")
    perms = set(permutations(list(word)))
    unscram = [''.join(p) for p in perms if d.check(''.join(p))]
    return unscram


def main():
    s = "fcienan"
    print(unscramble(s))
    return None


if __name__ == '__main__':
    main()
