from itertools import product


def K(w1: bool, w2: bool) -> bool:
    return w1 and w2


def A(w1: bool, w2: bool) -> bool:
    return w1 or w2


def N(w: bool):
    return not w


def C(w1: bool, w2: bool) -> bool:
    return w1 != True and w2 != False


def E(w1: bool, w2: bool) -> bool:
    return w1 == w2


mapping = {"K": K, "A": A, "N": N, "C": C, "E": E}


def eval_tautology(original_str: str) -> tuple[bool, str]:
    s = original_str
    n_fn = s[0] == "N"
    fn = mapping[s[0]]
    s = s[1:]
    if s[0] == "0":
        w1 = 0
        s = s[1:]
    elif s[0] == "1":
        w1 = 1
        s = s[1:]
    else:
        w1, s = eval_tautology(s[0:])
    if n_fn:
        return N(w1), s
    if s[0] == "0":
        w2 = 0
        s = s[1:]
    elif s[0] == "1":
        w2 = 1
        s = s[1:]
    else:
        w2, s = eval_tautology(s[0:])
    return fn(w1, w2), s


def solve(string: str) -> bool:
    for p, q, r, s, t in product((0, 1), repeat=5):
        if "p" not in string and p == 1:
            continue
        if "q" not in string and q == 1:
            continue
        if "r" not in string and r == 1:
            continue
        if "s" not in string and s == 1:
            continue
        if "t" not in string and t == 1:
            continue
        case = (
            string.replace("p", str(p))
            .replace("q", str(q))
            .replace("r", str(r))
            .replace("s", str(s))
            .replace("t", str(t))
        )
        if not eval_tautology(case)[0]:
            return False
    return True


while True:
    inp = input()
    if inp == "0":
        break
    if solve(inp):
        print("tautology")
    else:
        print("not")
