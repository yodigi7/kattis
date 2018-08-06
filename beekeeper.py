class Problem:
    def __init__(self, num_words):
        self.num_words = num_words
        self.word_list = self.get_words()

    def get_words(self):
        word_list = []
        for _ in range(self.num_words):
            word_list.append(input())
        return word_list

    def get_best_word(self):
        best_score = 0
        best_word = None
        for word in self.word_list:
            curr_score = self.score_word(word)
            if curr_score > best_score:
                best_score = curr_score
                best_word = word
        return best_word

    @staticmethod
    def score_word(word):
        score = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        word_as_list = list(word)
        for index in range(len(word_as_list)-1):
            if word_as_list[index] == word_as_list[index+1] and word_as_list[index] in vowels:
                score += 1
        return score


if __name__ == "__main__":
    num_words = int(input())
    while num_words:
        problem = Problem(num_words)
        print(problem.get_best_word())
        print(problem.score_word(problem.get_best_word()))
        num_words = int(input())
