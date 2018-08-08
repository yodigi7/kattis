if __name__ == '__main__':
    parts, days = [int(x) for x in input().split()]
    replaced = []
    for day in range(days):
        part = input()
        if part not in replaced:
            replaced.append(part)
            if len(replaced) >= parts:
                print(day + 1)
                exit()
    print("paradox avoided")
