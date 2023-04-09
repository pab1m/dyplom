    # elif message.text == "":
#         photo = open("agents_images/", 'rb')
#         bot.send_photo(message.chat.id, photo)
#         photo.close()
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#
#         btn1 = types.KeyboardButton("Біографія ")
#         btn2 = types.KeyboardButton("Спеціальні здібності ")
#         btn3 = types.KeyboardButton("ВАРТОВИЙ/СТРАЖ (SENTINEL)")
#         markup.add(btn1, btn2, btn3)
#
#         bot.send_message(message.chat.id,
#                          f"Оберіть категорію для ознайомлення:", reply_markup=markup)
    #
    # elif message.text == "Біографія ":
    #     _bio = ().bio()
    #     bot.send_message(message.chat.id, _bio)
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    #
    #     btn1 = types.KeyboardButton("Спеціальні здібності ")
    #     btn2 = types.KeyboardButton("ВАРТОВИЙ/СТРАЖ (SENTINEL)")
    #     markup.add(btn1, btn2)
    #
    #     bot.send_message(message.chat.id,
    #                      f"Оберіть категорію для ознайомлення:", reply_markup=markup)
    #
    # elif message.text == "Спеціальні здібності ":
    #
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    #
    #     btn1 = types.KeyboardButton(" (Q)")
    #     btn2 = types.KeyboardButton(" (E)")
    #     btn3 = types.KeyboardButton(" (C)")
    #     btn4 = types.KeyboardButton(" (X)")
    #     btn5 = types.KeyboardButton("")
    #     markup.add(btn1, btn2, btn3, btn4, btn5)
    #
    #     bot.send_message(message.chat.id,
    #                      f"Оберіть здібність:", reply_markup=markup)
    #
    # elif message.text == " (Q)":
    #     bot.send_message(message.chat.id, "Завантаження...")
    #     with open("abilities/", 'rb') as :
    #         bot.send_video(message.chat.id, )
    #     ab = ().abilities()
    #     bot.send_message(message.chat.id, ab['q'])
    #
    # elif message.text == " (E)":
    #     bot.send_message(message.chat.id, "Завантаження...")
    #     with open("abilities/", 'rb') as :
    #         bot.send_video(message.chat.id, )
    #     ab = ().abilities()
    #     bot.send_message(message.chat.id, ab['e'])
    #
    # elif message.text == " (C)":
    #     bot.send_message(message.chat.id, "Завантаження...")
    #     with open("abilities/", 'rb') as :
    #         bot.send_video(message.chat.id, )
    #     ab = ().abilities()
    #     bot.send_message(message.chat.id, ab['c'])
    #
    # elif message.text == " (X)":
    #     bot.send_message(message.chat.id, "Завантаження...")
    #     with open("abilities/", 'rb') as :
    #         bot.send_video(message.chat.id, )
    #     ab = ().abilities()
    #     bot.send_message(message.chat.id, ab['x'])
