def get_input_data():
    in_data = list(input())
    return in_data


def calculate_seat_up_or_down(up_or_down, in_data):
    seat_changes = 0
    if (not(in_data[0] == in_data[1])) and up_or_down == in_data[1]:
        seat_changes += 1
    elif in_data[0] == in_data[1] and up_or_down == in_data[1]:
        seat_changes -= 1
    for index in range(1, len(in_data)):
        if in_data[index] == up_or_down:
            seat_changes += 2
    return seat_changes


def calculate_seat_as_is(in_data):
    seat_changes = 0
    for index in range(len(in_data)-1):
        if not(in_data[index] == in_data[index+1]):
            seat_changes += 1
    return seat_changes


if __name__ == "__main__":
    input_data = get_input_data()
    print(calculate_seat_up_or_down('D', input_data))
    print(calculate_seat_up_or_down('U', input_data))
    print(calculate_seat_as_is(input_data))