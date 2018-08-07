def get_winning_candidate(ballot_list: list) -> int:
    largest_vote = max(ballot_list)
    if ballot_list.count(largest_vote) > 1:
        return 0
    else:
        return ballot_list.index(largest_vote) + 1


def is_majority(ballot_list: list) -> list:
    largest_vote = max(ballot_list)
    if largest_vote/sum(ballot_list) > .5:
        return "majority"
    return "minority"


if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        num_candidates = int(input())
        ballot_list = [int(input()) for x in range(num_candidates)]
        winner = get_winning_candidate(ballot_list)
        if winner is 0:
            print("no winner")
        else:
            win_by = is_majority(ballot_list)
            print("{} winner {}".format(win_by, winner))
