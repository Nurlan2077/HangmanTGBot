import random
import json


class GameWord:
    def __init__(self):
        self.word = self.__get_random_word("words.json")

        self.actual_game_word = [" _"] * len(self.word)
        self.open_random_letters()

        self.mistakes_num = 0

    def reload_gameword(self):
        self.__init__()

    @staticmethod
    def __get_random_word(file_name):
        with open(file_name) as json_file:
            json_word_array = json.load(json_file)["words"]
            return json_word_array[random.randrange(0, len(json_word_array))]

    def process_answer(self, letter):
        if self.is_right_letter(letter):
            self.open_letters(letter)

            if self.is_word_fully_opened():
                return "win"

            return "right"

        else:
            self.mistakes_num += 1
            if self.is_mistakes_num_over():
                return "lose"

            return "wrong"

    def is_right_letter(self, letter):
        if letter in self.word:
            return True
        else:
            return False

    def open_letters(self, letter):
        open_letter_indices = self.get_letter_indices(letter)
        for index in open_letter_indices:
            self.actual_game_word[index] = self.word[index]

    def get_letter_indices(self, letter):
        letter_occurances = [i for i, x in enumerate(self.word) if x == letter]
        return letter_occurances

    def get_actual_word(self):
        return "".join(self.actual_game_word)

    def is_word_fully_opened(self):
        if " _" in self.actual_game_word:
            return False
        else:
            return True

    def is_mistakes_num_over(self):
        if self.mistakes_num >= 6:
            return True
        else:
            return False

    def open_random_letters(self):
        for index in random.sample(range(0, len(self.word)), 2):
            letter_indices = self.get_letter_indices(self.word[index])

            for letter_index in letter_indices:
                self.actual_game_word[letter_index] = self.word[index]



