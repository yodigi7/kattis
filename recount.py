from collections import Counter


if __name__ == "__main__":
    counter = Counter()
    votes = []
    while True:
        name = input()
        if name == "***":
            break
        votes.append(name)
    first, second = Counter(votes).most_common(2)
    if first[1] == second[1]:
        print("Runoff!")
    else:
        print(first[0])
