from collections import namedtuple


# TODO: Optimize to only expand the nodes that the desired result will be on
Node = namedtuple("Node", "numerator denominator")


def flatten(full_list: list) -> list:
    return [x for sub_list in full_list for x in sub_list]


def get_left_child(node: Node) -> Node:
    return Node(numerator=node.numerator, denominator=(node.numerator + node.denominator))


def get_right_child(node: Node) -> Node:
    return Node(numerator=(node.numerator + node.denominator), denominator=node.denominator)


def solve_problem():
    inp = input().split()
    num_case = int(inp[0])
    numerator, denominator = inp[1].split('/')
    goal_node = Node(int(numerator), int(denominator))
    current_layer = [Node(1, 1)]
    current_n = 1
    print("{} {}".format(num_case, current_n))


if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        solve_problem()
