import telebot
from GameWord import GameWord
from game_control import replay, send_gif, send_gallows_state


with open("token.txt") as f:
    token = f.readline()

bot = telebot.TeleBot(token)

# Хранит айди пользователей и их сессии игрыы.
games = {}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        with open("start_text.txt") as f:
            start_text = "".join(f.readlines())

        games[message.from_user.id] = GameWord()

        bot.send_message(message.from_user.id, start_text)
        bot.send_message(message.from_user.id, games[message.from_user.id].get_actual_word())

        print(games[message.from_user.id].word)

    elif message.text == "/start_game":
        games[message.from_user.id].reload_gameword()
        bot.send_message(message.from_user.id,
                         "Игра началась! Напиши букву! Чтобы начать новую игру, напиши /start_game!")
        bot.send_message(message.from_user.id, games[message.from_user.id].get_actual_word())

    elif len(message.text) > 1:
        bot.send_message(message.from_user.id,
                         "Пиши только 1 букву!")

    else:
        response = games[message.from_user.id].process_answer(message.text)

        bot.send_message(message.from_user.id,
                         games[message.from_user.id].get_actual_word())

        response_process(response, message)


# Обрабатывает игровые ситуации (прав./не прав. ответы, победа, поражение)
def response_process(response, message):
    if response == "win":
        bot.send_message(message.from_user.id,
                         "Ты победил!")

        replay(bot, message, games[message.from_user.id])

    elif response == "lose":
        send_gallows_state(bot, message, games[message.from_user.id].mistakes_num)

        bot.send_message(message.from_user.id,
                         "Ты проиграл :(")

        replay(bot, message, games[message.from_user.id])

    elif response == "right":
        bot.send_message(message.from_user.id,
                         "Правильно")
        send_gif(bot, message, True)

    elif response == "wrong":
        bot.send_message(message.from_user.id,
                         "Неверно")
        send_gallows_state(bot, message, games[message.from_user.id].mistakes_num)


bot.polling(none_stop=True, interval=0)
