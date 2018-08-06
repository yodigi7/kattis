def solve(case_number):
    message, alien_alphabet, target_alphabet = input().split()
    message_as_number = message_to_number(message, alien_alphabet)
    converted_message = convert_message(message_as_number, target_alphabet)
    return format_answer(converted_message, case_number)


def message_to_number(message, alphabet):
    message_as_number = []
    for char in message:
        message_as_number.append(alphabet.index(char))
    return message_as_number


def convert_message(message_as_number, alien_language, target_alphabet):
    message_as_number_string = "".join([str(x) for x in message_as_number])
    int(message_as_number_string, len(alien_language))
    message_as_number_string = message_as_number_string[2:]

    message_as_number_list = [int(x) for x in message_as_number_string]

    new_message = ""
    for i in range(len(message_as_number_list)):
        new_message += target_alphabet[i]

    return new_message


def format_answer(message, case_number):
    return "Case #{}: {}".format(case_number, message)


if __name__ == '__main__':
    for i in range(int(input())):
        print(solve(i))
