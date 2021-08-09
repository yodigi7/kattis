from collections import defaultdict


def set(people, person, val):
    people[person] = val
    return people


def print_comm(people, person):
    print(people[person])


def restart(val):
    return defaultdict(lambda: val)


def solve(people):
    while True:
        try:
            command, person, *val = input().split()
            person = int(person)
            if command == "SET":
                people = set(people, person, int(val[0]))
            elif command == "PRINT":
                print_comm(people, person)
            elif command == "RESTART":
                people = restart(person)
        except EOFError:
            return


def main():
    n, q = [int(x) for x in input().split()]
    people = defaultdict(int)
    solve(people)
main()