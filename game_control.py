import random
import os

gifs_folder = "gifs/"
right_answer_gifs_folder = gifs_folder + "right_answer/"
wrong_answer_gifs_folder = gifs_folder + "wrong_answer/"
gallows_states_image_folder = "gallows_states/"


# После победы или проигрыша предлагает продолжить игру.
def replay(bot, message, game_word):
    game_word.reload_gameword()
    bot.send_message(message.from_user.id,
                     "Попробуй теперь угадать это слово!")
    bot.send_message(message.from_user.id,
                     game_word.get_actual_word())


# Отправляет гиф на правильные и неправильные ответы.
def send_gif(bot, message, is_right_answer):

    if is_right_answer:
        image_names = os.listdir(right_answer_gifs_folder)
        bot.send_animation(message.from_user.id,
                           open(right_answer_gifs_folder + random.choice(image_names), 'rb'))

    elif not is_right_answer:
        image_names = os.listdir(wrong_answer_gifs_folder)

        bot.send_animation(message.from_user.id,
                           open(wrong_answer_gifs_folder + random.choice(image_names), 'rb'))


# Отправляет текущее состояние виселицы.
def send_gallows_state(bot, message, mistakes_num):
    bot.send_photo(message.from_user.id,
                       open(gallows_states_image_folder + str(mistakes_num) + ".png", 'rb'))


