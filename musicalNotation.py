from copy import deepcopy


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


def get_input_notes():
    _ = input()
    return input().split()


def generate_starting_dictionary():
    dictionary = dict()
    for letter in char_range('A', 'G'):
        dictionary[letter] = []
    for letter in char_range('a', 'g'):
        dictionary[letter] = []
    return dictionary


def input_to_dict():
    return_dict = generate_starting_dictionary()
    input_list = get_input_notes()
    for index in range(len(input_list)):
        note = input_list[index]
        return_dict = update_dict_with_note(note, return_dict)
        if index < len(input_list)-1:
            return_dict = update_dict_with_space(return_dict)
    return return_dict


def update_dict_with_note(input_note, input_dictionary):
    dictionary = deepcopy(input_dictionary)
    note = input_note[0]
    dictionary = update_dict_with_one_note(note, dictionary)
    if len(input_note) > 1:
        for _ in range(int(input_note[1])-1):
            dictionary = update_dict_with_one_note(note, dictionary)
    return dictionary


def update_dict_with_one_note(input_note, input_dictionary):
    dash_notes = ['F', 'D', 'B', 'g', 'e', 'a']
    dictionary = deepcopy(input_dictionary)
    input_note_letter = input_note[0]
    for note, note_list in dictionary.items():
        if note == input_note_letter:
            note_list.append('*')
        elif note in dash_notes:
            note_list.append('-')
        else:
            note_list.append(' ')
    return dictionary


def update_dict_with_space(input_dictionary):
    dash_notes = ['F', 'D', 'B', 'g', 'e', 'a']
    dictionary = deepcopy(input_dictionary)
    for note, note_list in dictionary.items():
        if note in dash_notes:
            note_list.append('-')
        else:
            note_list.append(' ')
    return dictionary


def output_song(song_dictionary):
    note_output_order = ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    for note in note_output_order:
        print('{}: {}'.format(note, ''.join(song_dictionary[note])))


if __name__ == "__main__":
    song_dict = input_to_dict()
    output_song(song_dict)
