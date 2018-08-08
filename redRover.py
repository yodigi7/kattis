def net_characters(message: str, macro: str) -> int:
    bonus = len(macro) - 1
    count_shows = message.count(macro)
    score = len(message) - (bonus*count_shows - len(macro))
    return score


if __name__ == '__main__':
    message = input()
    best_score = len(message)
    for i in range(len(message)-2):
        for j in range(i+2, len(message)):
            curr_score = net_characters(message, message[i:j])
            best_score = min(curr_score, best_score)
    print(best_score)
