from queue import Queue


class CarData:
    def __init__(self, arrival_time, arrival_side):
        self.arrival_time = arrival_time
        self.arrival_side = arrival_side

    def __str__(self):
        return f'Arrival time: {self.arrival_time}, arrival_side: {self.arrival_side}'

    def __repr__(self):
        return str(self)


class Car:
    wait_time: int
    location: str


class Ferry:
    location: str
    time_to_shore: int
    cargo: list

    def __init__(self, capacity: int, travel_time: int):
        self.capacity = capacity
        self.travel_time = travel_time

    def leave(self):
        self.location = 'left' if self.location == 'right' else 'right'

    def load(self, car: Car):
        self.cargo.append(car)

    def has_room(self):
        return True if len(self.cargo) < self.capacity else False


class Game:
    current_time: int
    left_cars: list
    right_cars: list
    all_cars: list
    left_bank: list
    right_bank: list

    def solve_problem(self):
        self.current_time = 0
        self.left_bank = []
        self.right_bank = []
        capacity, travel_time, num_cars = [int(x) for x in input().split()]
        car_data = [input().split() for _ in range(num_cars)]
        car_data = [[int(item[0]), item[1]] for item in car_data]
        self.all_cars = [CarData(item[0], item[1]) for item in car_data]
        self.left_cars = [x for x in self.all_cars if x.arrival_side == 'left']
        self.right_cars = [x for x in self.all_cars if x.arrival_side == 'right']
        while not self.finished():
            self.step()

    def step(self):
        # Add newly arrived cars
        for car in self.left_cars:
            if car.wait_time == self.current_time:
                if car.location == 'left':
                    self.left_cars.append(car)
                else:
                    self.right_cars.append(car)
        # If ferry is on dock, unload and load cars

    def finished(self):
        return True if len(self.left_cars) is 0 and len(self.right_cars) is 0 else False


if __name__ == '__main__':
    for _ in range(int(input())):
        Game().solve_problem()
