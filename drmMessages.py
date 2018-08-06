import string


class Problem:
    """
        Problem class
    """

    def __init__(self, input_message):
        """ Constructor for Problem """
        self.message = input_message

    def solve(self):
        self._merge(self._rotate(self._divide()))
        return self.message

    def _divide(self):
        return self.message[:(len(self.message)//2)], self.message[len(self.message)//2:]

    def _rotate(self, divided_message):
        return_group = list(divided_message)

        counter = 0
        for part in divided_message:
            offset = self._calculate_offset(part)
            rotated_part = self._rotate_around(part, offset)
            return_group[counter] = rotated_part
            counter += 1

        return return_group

    def _merge(self, divided_message):
        merged_message = ""
        for index in range(len(divided_message[0])):
            merged_message += self._rotate_around(divided_message[0][index], ord(divided_message[1][index]) - ord('A'))
        self.message = merged_message
        return merged_message

    @staticmethod
    def _rotate_around(input_string, amount):
        return_string = ""
        for letter in input_string:
            letter = chr(ord(letter) + amount)
            while letter not in string.ascii_uppercase:
                letter = chr(ord(letter) - 26)
            return_string += letter
        return return_string

    @staticmethod
    def _calculate_offset(message):
        return_num = 0
        for letter in message:
            return_num += ord(letter) - ord('A')
        return return_num


if __name__ == '__main__':
    print(Problem(input()).solve())
