def min_dist(num_cars_between: int, dec_const: int) -> int:
    return dec_const*(num_cars_between+1)


if __name__ == '__main__':
    num_cars, dec_const = [int(x) for x in input().split()]
    car_dists = sorted([int(x) for x in input().split()])
    dist = 0
    for i in range(num_cars):
        minimum_dist = min_dist(i, dec_const) - (car_dists[i] - car_dists[0])
        if minimum_dist > dist:
            dist = minimum_dist
    print(dist)
