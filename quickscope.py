from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Var:
    name: str
    type: str
    depth: str


class MultipleDeclarationException(Exception):
    pass


def get_typeof(var, all_vars):
    return all_vars[var]


def add_var(var, type, depth, full_vars, vars_by_depth):
    if full_vars[var]:
        if full_vars[var][-1].depth is depth:
            raise MultipleDeclarationException()
    full_vars[var].append(Var(name=var, type=type, depth=depth))
    vars_by_depth[depth].append(var)


def close_scope(depth, all_vars, full_vars, vars_by_depth):
    for var in vars_by_depth[depth]:
        val = full_vars[var]
        val.pop()
        all_vars[var] = val[-1].type if val else "UNDECLARED"
        full_vars[var] = val
    vars_by_depth[depth] = []


def solve(n):
    full_vars = defaultdict(list)
    all_vars = defaultdict(lambda: "UNDECLARED")
    vars_by_depth = defaultdict(list)
    depth = 0
    for _ in range(n):
        command = input().split()
        if command[0] == "TYPEOF":
            var = command[1]
            print(get_typeof(var, all_vars))
        elif command[0] == "DECLARE":
            var, type = command[1:]
            all_vars[var] = type
            try:
                add_var(var, type, depth, full_vars, vars_by_depth)
            except MultipleDeclarationException:
                print("MULTIPLE DECLARATION")
                return
        elif command == ["{"]:
            depth += 1
        elif command == ["}"]:
            close_scope(depth, all_vars, full_vars, vars_by_depth)
            depth -= 1


if __name__ == "__main__":
    n = int(input())
    solve(n)
