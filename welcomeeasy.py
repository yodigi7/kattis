def solve(sentence, sub_sentence):
    if len(sub_sentence) > len(sentence):
        return 0
    for char in sub_sentence:
        if char not in sentence:
            return 0
    if len(sub_sentence) == 1:
        return sentence.count(sub_sentence)
    curr_char = sub_sentence[0]
    count = 0
    curr_sentence = sentence
    for _ in range(sentence.count(curr_char)):
        idx = curr_sentence.index(curr_char)
        count += solve(curr_sentence[idx+1:], sub_sentence[1:])
        curr_sentence = curr_sentence[idx+1:]
    return count


def main():
    for i in range(1, int(input())+1):
        solution = solve(input(), "welcome to code jam") % 10000
        print(f"Case #{i}: {str(solution).zfill(4)}")


main()