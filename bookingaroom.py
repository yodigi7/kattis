def solve(r, booked_rooms):
    if r == len(booked_rooms):
        return "too late"
    for i in range(1, r+1):
        if i not in booked_rooms:
            return i
    return "too late"


def main():
    r, n = [int(x) for x in input().split()]
    booked_rooms = [int(input()) for _ in range(n)]
    print(solve(r, booked_rooms))

main()