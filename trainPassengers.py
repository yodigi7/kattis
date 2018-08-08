def is_possible() -> str:
    cap, stops = [int(x) for x in input().split()]
    people_on_train = 0
    for _ in range(stops):
        left, entered, stay = [int(x) for x in input().split()]
        if _ is 0 and left is not 0 or \
                people_on_train - left < 0 or \
                people_on_train + entered - left < cap and stay is not 0 or \
                people_on_train + entered - left < 0 or \
                people_on_train + entered - left > cap:
            return "impossible"
        people_on_train += entered - left
    if people_on_train is not 0:
        return "impossible"
    return "possible"


if __name__ == '__main__':
    print(is_possible())
