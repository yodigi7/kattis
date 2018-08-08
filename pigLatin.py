import sys


def is_vowel(letter: chr) -> bool:
    if letter in 'aeiouy':
        return True
    return False


def get_first_vowel_idx(word: str) -> int:
    for i in range(len(word)):
        if is_vowel(word[i]):
            return i
    raise RuntimeError()


def move_beginning_consontants(word: str) -> str:
    return word[get_first_vowel_idx(word):] + word[:get_first_vowel_idx(word)]


def to_pig_latin(word: str) -> str:
    if is_vowel(word[0]):
        return word + 'yay'
    return move_beginning_consontants(word) + 'ay'


if __name__ == '__main__':
    for line in sys.stdin:
        print(" ".join([to_pig_latin(x) for x in line.split()]))
