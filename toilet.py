from enum import Enum, auto
from functools import partial

class Position(Enum):
    UP = auto()
    DOWN = auto()
class Toilet:
    position: Position
    def __init__(self, position):
        self.position = position

    def flip(self):
        if self.position is Position.UP:
            self.position = Position.DOWN
        elif self.position is Position.DOWN:
            self.position = Position.UP


mapper = {
    "U": Position.UP,
    "D": Position.DOWN,
}



def toilet_sim(ending_positions, positions):
    toilet = Toilet(positions[0])
    flips = 0
    for position in positions[1:]:
        if toilet.position is not position:
            toilet.flip()
            flips += 1
        if toilet.position not in ending_positions:
            toilet.flip()
            flips += 1
    return flips


always_up = partial(toilet_sim, [Position.UP])
always_down = partial(toilet_sim, [Position.DOWN])
always_last = partial(toilet_sim, [Position.UP, Position.DOWN])


def solve(positions):
    print(always_up(positions))
    print(always_down(positions))
    print(always_last(positions))


def main():
    solve([mapper[i] for i in input()])


main()
