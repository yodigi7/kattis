def word_score(word):
    if len(word) <= 1:
        return 0
    score = 0
    if word[0] == word[1] and word[0] in "aeiouy":
        score += 1
    return word_score(word[1:]) + score


def solve(words):
    return max(words, key=word_score)


def main():
    while True:
        words = []
        num_words = int(input())
        if num_words == 0: return
        for _ in range(num_words):
            words.append(input())
        print(solve(words))


main()