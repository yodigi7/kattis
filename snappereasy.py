def solve(n, k):
    req_num = pow(2, n)
    k %= req_num
    if k == req_num-1:
        return "ON"
    else:
        return "OFF"


def main():
    for i in range(1, int(input())+1):
        n, k = ( int(x) for x in input().split() )
        print(f"Case #{i}: {solve(n, k)}")


main()