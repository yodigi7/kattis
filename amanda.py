from dataclasses import dataclass
from itertools import combinations


class ImpossibleException(Exception):
    pass


@dataclass
class Requirement:
    ports: tuple
    lounges: int


def get_requirement():
    p1, p2, lounges = [int(x) for x in input().split()]
    return Requirement(ports=(p1, p2), lounges=lounges)


def valid_solution(ports, requirements):
    if -1 in ports.values():
        return False

    for requirement in requirements:
        if requirement.lounges == 2:
            if ports[requirement.ports[0]] == 0 or ports[requirement.ports[1]] == 0:
                return False
        elif requirement.lounges == 0:
            if ports[requirement.ports[0]] == 1 or ports[requirement.ports[1]] == 1:
                return False
        elif requirement.lounges == 1:
            if (
                ports[requirement.ports[0]] == 1 and ports[requirement.ports[1]] == 1
            ) or (
                ports[requirement.ports[0]] == 0 and ports[requirement.ports[1]] == 0
            ):
                return False
    return True


def solve(ports, requirements):
    for requirement in requirements:
        if requirement.lounges == 2:
            if ports[requirement.ports[0]] == 0 or ports[requirement.ports[1]] == 0:
                raise ImpossibleException()
            ports[requirement.ports[0]] = 1
            ports[requirement.ports[1]] = 1
        elif requirement.lounges == 0:
            if ports[requirement.ports[0]] == 1 or ports[requirement.ports[1]] == 1:
                raise ImpossibleException()
            ports[requirement.ports[0]] = 0
            ports[requirement.ports[1]] = 0
        elif requirement.lounges == 1:
            if (
                ports[requirement.ports[0]] == 1 and ports[requirement.ports[1]] == 1
            ) or (
                ports[requirement.ports[0]] == 0 and ports[requirement.ports[1]] == 0
            ):
                raise ImpossibleException()
            elif ports[requirement.ports[0]] == -1 or ports[requirement.ports[1]] == -1:
                if ports[requirement.ports[0]] == 1:
                    ports[requirement.ports[1]] = 0
                elif ports[requirement.ports[0]] == 0:
                    ports[requirement.ports[1]] = 1
                elif ports[requirement.ports[1]] == 1:
                    ports[requirement.ports[0]] = 0
                elif ports[requirement.ports[1]] == 0:
                    ports[requirement.ports[0]] = 1

    maybe_ports = {key: -1 for key, val in ports.items() if val == -1}
    maybe_ports_count = len(maybe_ports)
    for i in range(0, maybe_ports_count + 1):
        possible_ports_list = combinations(maybe_ports, i)
        for possible_port in possible_ports_list:
            copy_ports = ports.copy()
            copy_ports.update({key: 1 for key in possible_port})
            copy_ports.update(
                {key: 0 for key, val in maybe_ports.items() if key not in possible_port}
            )
            if valid_solution(copy_ports, requirements):
                return list(ports.values()).count(1)

    if -1 in ports.values():
        raise ImpossibleException()

    return list(ports.values()).count(1)


if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    requirements = [get_requirement() for _ in range(m)]
    ports = {x: -1 for x in range(1, n + 1)}
    try:
        print(solve(ports, requirements))
    except ImpossibleException:
        print("impossible")
