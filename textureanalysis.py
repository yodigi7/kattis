def is_even(row):
    if "." not in row:
        return True
    modrow = row.split("*")[1:-1]
    num_dots = len(modrow[0])
    return all(len(x) == num_dots for x in modrow)


def main():
    i = 1
    while True:
        inp = input()
        if inp == "END":
            return
        if is_even(inp):
            print(f"{i} EVEN")
        else:
            print(f"{i} NOT EVEN")
        i += 1


main()