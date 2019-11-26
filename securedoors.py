
def convert_action(action):
    if "entry" in action:
        return "entered"
    return "exited"


def is_anomaly(inside, outside, person, action):
    if "entry" in action:
        if person in inside:
            return True
    else:
        if person not in inside:
            return True
    return False


def move(inside, outside, person, action):
    if "entry" in action:
        if person in outside:
            outside.remove(person)
        if person not in inside:
            inside.append(person)
    else:
        if person in inside:
            inside.remove(person)
        if person not in outside:
            outside.append(person)
    return inside, outside


if __name__ == '__main__':
    inside = []
    outside = []
    results = []
    for _ in range(int(input())):
        event = input()
        split_event = event.split()
        person = split_event[1]
        action = split_event[0]
        temp_result = person + " " + convert_action(action)
        if is_anomaly(inside, outside, person, action):
            temp_result += " (ANOMALY)"
        results.append(temp_result)
        inside, outside = move(inside, outside, person, action)
    print("\n".join(results))
