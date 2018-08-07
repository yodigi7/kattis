import math
from decimal import *


def make_final_velocity_fn(ACCEL_CONST):
    def get_final_velocity(init_vel: int, dist: int, angle: int) -> Decimal:
        return Decimal(math.sqrt(Decimal(init_vel**2) + Decimal(2*ACCEL_CONST*math.cos(math.radians(angle))*dist)))
    return get_final_velocity


def get_velocity(final_vel_fn, segments: list):
    velocity = 0
    for segment in segments:
        velocity = final_vel_fn(velocity, segment[0], segment[1])
    return velocity


if __name__ == '__main__':
    segments, accel_const = input().split()
    final_vel_fn = make_final_velocity_fn(float(accel_const))
    with localcontext() as context:
        context.prec = 10
        trails = [[float(x) for x in input().split()] for trail in range(int(segments))]
        for i in range(len(trails)):
            print(get_velocity(final_vel_fn, trails[i:]))
