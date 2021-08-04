from operator import eq, gt, lt


def solve(lines):
    output = []
    vars = {}
    for line in lines:
        line = line.split()
        if line[0] == "define":
            vars[line[2]] = int(line[1])
        elif line[0] == "eval":
            var1 = line[1]
            var2 = line[3]
            if var1 not in vars or var2 not in vars:
                output.append("undefined")
                continue
            if line[2] == ">":
                op = gt
            elif line[2] == "<":
                op = lt
            elif line[2] == "=":
                op = eq
            output.append(str(op(vars[var1], vars[var2])).lower())
    return output


def main():
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    print("\n".join(solve(lines)))


main()