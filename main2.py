import telebot
from telebot import types
from all_inf import *

TOKEN = "6275163921:AAFvgDqIWHw7Lk0YnaZPBVW2rHJEjrKu_FA"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     f"Привіт, <b>{message.from_user.first_name if message.from_user.last_name is None else message.from_user.first_name + ' ' + message.from_user.last_name}</b>, я телеграм бот який допоможе тобі познайомитися із грою VALORANT та дізнатися "
                     "інформацію про свій прогрес", parse_mode='html')
    bot.send_message(message.chat.id,
                     "Введіть /help щоб дізнатися мій функціонал")


@bot.message_handler(commands=['help'])
def help_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("Для новачків")
    btn2 = types.KeyboardButton("Моя статистика")
    btn3 = types.KeyboardButton("Допомога")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id,
                     f"Доступні команди:", reply_markup=markup)


@bot.message_handler()
def get_user_text(message):
    if message.text == "Для новачків":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        btn1 = types.KeyboardButton("Агенти")
        btn2 = types.KeyboardButton("Карти")
        btn3 = types.KeyboardButton("Зброя")
        btn4 = types.KeyboardButton("На головну")
        markup.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.chat.id,
                         f"Для новачків:", reply_markup=markup)

    elif message.text == "На головну":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        btn1 = types.KeyboardButton("Для новачків")
        btn2 = types.KeyboardButton("Моя статистика")
        btn3 = types.KeyboardButton("Допомога")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"На головну:", reply_markup=markup)

    elif message.text == "Агенти":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        btn1 = types.KeyboardButton("КОНТРОЛЕР (CONTROLLER)")
        btn2 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        btn3 = types.KeyboardButton("ВАРТОВИЙ/СТРАЖ (SENTINEL)")
        btn4 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        btn5 = types.KeyboardButton("Для новачків")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть клас агентів:", reply_markup=markup)

    elif message.text == "КОНТРОЛЕР (CONTROLLER)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        btn1 = types.KeyboardButton("BRIMSTONE")
        btn2 = types.KeyboardButton("VIPER")
        btn3 = types.KeyboardButton("OMEN")
        btn4 = types.KeyboardButton("ASTRA")
        btn5 = types.KeyboardButton("HARBOR")
        btn6 = types.KeyboardButton("Агенти")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

        bot.send_message(message.chat.id,
                         f"Оберіть агента:", reply_markup=markup)

    elif message.text == "BRIMSTONE":
        photo = open("agents_images/brimstone.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія BRIMSTONE")
        btn2 = types.KeyboardButton("Спеціальні здібності BRIMSTONE")
        btn3 = types.KeyboardButton("КОНТРОЛЕР (CONTROLLER)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія BRIMSTONE":
        Brim_bio = Brim().bio()
        bot.send_message(message.chat.id, Brim_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності BRIMSTONE")
        btn2 = types.KeyboardButton("КОНТРОЛЕР (CONTROLLER)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності BRIMSTONE":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Запалювальна граната (Q)")
        btn2 = types.KeyboardButton("Небесний дим (E)")
        btn3 = types.KeyboardButton("Маячок-стимулятор (C)")
        btn4 = types.KeyboardButton("Орбітальний удар (X)")
        btn5 = types.KeyboardButton("BRIMSTONE")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Запалювальна граната (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/brimstone/brim3.mp4", 'rb') as brim:
            bot.send_video(message.chat.id, brim)
        ab = Brim().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Небесний дим (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/brimstone/brim1.mp4", 'rb') as brim:
            bot.send_video(message.chat.id, brim)
        ab = Brim().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Маячок-стимулятор (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/brimstone/brim2.mp4", 'rb') as brim:
            bot.send_video(message.chat.id, brim)
        ab = Brim().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Орбітальний удар (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/brimstone/brim4.mp4", 'rb') as brim:
            bot.send_video(message.chat.id, brim)
        ab = Brim().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "VIPER":
        photo = open("agents_images/viper.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія VIPER")
        btn2 = types.KeyboardButton("Спеціальні здібності VIPER")
        btn3 = types.KeyboardButton("КОНТРОЛЕР (CONTROLLER)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія VIPER":
        Viper_bio = Viper().bio()
        bot.send_message(message.chat.id, Viper_bio, parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності VIPER")
        btn2 = types.KeyboardButton("КОНТРОЛЕР (CONTROLLER)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності VIPER":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Отруйна хмара (Q)")
        btn2 = types.KeyboardButton("Токсична завіса (E)")
        btn3 = types.KeyboardButton("Укус змії (C)")
        btn4 = types.KeyboardButton("Гніздо гадюки (X)")
        btn5 = types.KeyboardButton("VIPER")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Отруйна хмара (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/viper/viper2.mp4", 'rb') as viper:
            bot.send_video(message.chat.id, viper)
        ab = Viper().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Токсична завіса (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/viper/viper1.mp4", 'rb') as viper:
            bot.send_video(message.chat.id, viper)
        ab = Viper().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Укус змії (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/viper/viper3.mp4", 'rb') as viper:
            bot.send_video(message.chat.id, viper)
        ab = Viper().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Гніздо гадюки (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/viper/viper4.mp4", 'rb') as viper:
            bot.send_video(message.chat.id, viper)
        ab = Viper().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "OMEN":
        with open("agents_images/omen.png", 'rb') as omen:
            bot.send_video(message.chat.id, omen)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія OMEN")
        btn2 = types.KeyboardButton("Спеціальні здібності OMEN")
        btn3 = types.KeyboardButton("КОНТРОЛЕР (CONTROLLER)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія OMEN":
        Omen_bio = Omen().bio()
        bot.send_message(message.chat.id, Omen_bio, parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності OMEN")
        btn2 = types.KeyboardButton("КОНТРОЛЕР (CONTROLLER)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності OMEN":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Параноя (Q)")
        btn2 = types.KeyboardButton("Темний покров (E)")
        btn3 = types.KeyboardButton("Прихований крок (C)")
        btn4 = types.KeyboardButton("З тіні (X)")
        btn5 = types.KeyboardButton("OMEN")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Параноя (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/omen/omen2.mp4", 'rb') as omen:
            bot.send_video(message.chat.id, omen)
        ab = Omen().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Темний покров (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/omen/omen1.mp4", 'rb') as omen:
            bot.send_video(message.chat.id, omen)
        ab = Omen().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Прихований крок (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/omen/omen3.mp4", 'rb') as omen:
            bot.send_video(message.chat.id, omen)
        ab = Omen().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "З тіні (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/omen/omen4.mp4", 'rb') as omen:
            bot.send_video(message.chat.id, omen)
        ab = Omen().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "ASTRA":
        with open("agents_images/astra.png", 'rb') as astra:
            bot.send_photo(message.chat.id, astra)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія ASTRA")
        btn2 = types.KeyboardButton("Спеціальні здібності ASTRA")
        btn3 = types.KeyboardButton("КОНТРОЛЕР (CONTROLLER)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія ASTRA":
        Astra_bio = Astra().bio()
        bot.send_message(message.chat.id, Astra_bio, parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності ASTRA")
        btn2 = types.KeyboardButton("КОНТРОЛЕР (CONTROLLER)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності ASTRA":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Вибух наднової (Q)")
        btn2 = types.KeyboardButton("Туманність (E)")
        btn3 = types.KeyboardButton("Гравітаційний колодязь (C)")
        btn4 = types.KeyboardButton("Космічний розрив (X)")
        btn5 = types.KeyboardButton("ASTRA")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Вибух наднової (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/astra/astra3.mp4", 'rb') as astra:
            bot.send_video(message.chat.id, astra)
        ab = Astra().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Туманність (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/astra/astra2.mp4", 'rb') as astra:
            bot.send_video(message.chat.id, astra)
        ab = Astra().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Гравітаційний колодязь (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/astra/astra1.mp4", 'rb') as astra:
            bot.send_video(message.chat.id, astra)
        ab = Astra().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Космічний розрив (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/astra/astra4.mp4", 'rb') as astra:
            bot.send_video(message.chat.id, astra)
        ab = Astra().abilities()
        bot.send_message(message.chat.id, ab['x'])

    # Агент HARBOR
    elif message.text == "HARBOR":
        with open("agents_images/harbor.png", 'rb') as harbor:
            bot.send_photo(message.chat.id, harbor)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія HARBOR")
        btn2 = types.KeyboardButton("Спеціальні здібності HARBOR")
        btn3 = types.KeyboardButton("КОНТРОЛЕР (CONTROLLER)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія HARBOR":
        Harbor_bio = Harbor().bio()
        bot.send_message(message.chat.id, Harbor_bio, parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності HARBOR")
        btn2 = types.KeyboardButton("КОНТРОЛЕР (CONTROLLER)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності HARBOR":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Залив (Q)")
        btn2 = types.KeyboardButton("Гребень хвилі (E)")
        btn3 = types.KeyboardButton("Каскад (C)")
        btn4 = types.KeyboardButton("Розрахунок курсу (X)")
        btn5 = types.KeyboardButton("HARBOR")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Залив (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/harbor/harbor2.mp4", 'rb') as harbor:
            bot.send_video(message.chat.id, harbor)
        ab = Harbor().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Гребень хвилі (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/harbor/harbor1.mp4", 'rb') as harbor:
            bot.send_video(message.chat.id, harbor)
        ab = Harbor().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Каскад (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/harbor/harbor3.mp4", 'rb') as harbor:
            bot.send_video(message.chat.id, harbor)
        ab = Harbor().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Розрахунок курсу (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/harbor/harbor4.mp4", 'rb') as harbor:
            bot.send_video(message.chat.id, harbor)
        ab = Harbor().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "ДУЕЛЯНТ (DUELIST)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        btn1 = types.KeyboardButton("PHOENIX")
        btn2 = types.KeyboardButton("REYNA")
        btn3 = types.KeyboardButton("JETT")
        btn4 = types.KeyboardButton("RAZE")
        btn5 = types.KeyboardButton("YORU")
        btn6 = types.KeyboardButton("NEON")
        btn7 = types.KeyboardButton("Агенти")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

        bot.send_message(message.chat.id,
                         f"Оберіть агента:", reply_markup=markup)

    elif message.text == "PHOENIX":
        photo = open("agents_images/phoenix.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія PHOENIX")
        btn2 = types.KeyboardButton("Спеціальні здібності PHOENIX")
        btn3 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія PHOENIX":
        Phoenix_bio = Phoenix().bio()
        bot.send_message(message.chat.id, Phoenix_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності PHOENIX")
        btn2 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності PHOENIX":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Кручена подача (Q)")
        btn2 = types.KeyboardButton("Гарячі руки (E)")
        btn3 = types.KeyboardButton("Пожежа (C)")
        btn4 = types.KeyboardButton("Повернення (X)")
        btn5 = types.KeyboardButton("PHOENIX")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Кручена подача (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/phoenix/phoenix2.mp4", 'rb') as phoenix:
            bot.send_video(message.chat.id, phoenix)
        ab = Phoenix().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Гарячі руки (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/phoenix/phoenix1.mp4", 'rb') as phoenix:
            bot.send_video(message.chat.id, phoenix)
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/phoenix/phoenix1.1.mp4", 'rb') as phoenix:
            bot.send_video(message.chat.id, phoenix)
        ab = Phoenix().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Пожежа (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/phoenix/phoenix3.mp4", 'rb') as phoenix:
            bot.send_video(message.chat.id, phoenix)
        ab = Phoenix().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Повернення (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/phoenix/phoenix4.mp4", 'rb') as phoenix:
            bot.send_video(message.chat.id, phoenix)
        ab = Phoenix().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "REYNA":
        photo = open("agents_images/reyna.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія REYNA")
        btn2 = types.KeyboardButton("Спеціальні здібності REYNA")
        btn3 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія REYNA":
        Reyna_bio = Reyna().bio()
        bot.send_message(message.chat.id, Reyna_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності REYNA")
        btn2 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності REYNA":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Поглинання (Q)")
        btn2 = types.KeyboardButton("Вигнання (E)")
        btn3 = types.KeyboardButton("Злісний погляд (C)")
        btn4 = types.KeyboardButton("Імператриця (X)")
        btn5 = types.KeyboardButton("REYNA")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Поглинання (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/reyna/reyna2.mp4", 'rb') as reyna:
            bot.send_video(message.chat.id, reyna)
        ab = Reyna().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Вигнання (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/reyna/reyna3.mp4", 'rb') as reyna:
            bot.send_video(message.chat.id, reyna)
        ab = Reyna().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Злісний погляд (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/reyna/reyna1.mp4", 'rb') as reyna:
            bot.send_video(message.chat.id, reyna)
        ab = Reyna().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Імператриця (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/reyna/reyna4.mp4", 'rb') as reyna:
            bot.send_video(message.chat.id, reyna)
        ab = Reyna().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "JETT":
        photo = open("agents_images/jett.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія JETT")
        btn2 = types.KeyboardButton("Спеціальні здібності JETT")
        btn3 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія JETT":
        Jett_bio = Jett().bio()
        bot.send_message(message.chat.id, Jett_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності JETT")
        btn2 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності JETT":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Підйом (Q)")
        btn2 = types.KeyboardButton("Попутний вітер (E)")
        btn3 = types.KeyboardButton("Вихор (C)")
        btn4 = types.KeyboardButton("Буря кинжалів (X)")
        btn5 = types.KeyboardButton("JETT")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Підйом (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/jett/jett2.mp4", 'rb') as jett:
            bot.send_video(message.chat.id, jett)
        ab = Jett().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Попутний вітер (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/jett/jett1.mp4", 'rb') as jett:
            bot.send_video(message.chat.id, jett)
        ab = Jett().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Вихор (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/jett/jett3.mp4", 'rb') as jett:
            bot.send_video(message.chat.id, jett)
        ab = Jett().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Буря кинжалів (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/jett/jett4.mp4", 'rb') as jett:
            bot.send_video(message.chat.id, jett)
        ab = Jett().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "RAZE":
        photo = open("agents_images/raze.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія RAZE")
        btn2 = types.KeyboardButton("Спеціальні здібності RAZE")
        btn3 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія RAZE":
        Raze_bio = Raze().bio()
        bot.send_message(message.chat.id, Raze_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності RAZE")
        btn2 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності RAZE":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Вибуховий ранець (Q)")
        btn2 = types.KeyboardButton("Касетна граната (E)")
        btn3 = types.KeyboardButton("Бум бот (C)")
        btn4 = types.KeyboardButton("Стоп-кадр (X)")
        btn5 = types.KeyboardButton("RAZE")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Вибуховий ранець (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/raze/raze2.mp4", 'rb') as raze:
            bot.send_video(message.chat.id, raze)
        ab = Raze().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Касетна граната (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/raze/raze1.mp4", 'rb') as raze:
            bot.send_video(message.chat.id, raze)
        ab = Raze().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Бум бот (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/raze/raze3.mp4", 'rb') as raze:
            bot.send_video(message.chat.id, raze)
        ab = Raze().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Стоп-кадр (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/raze/raze4.mp4", 'rb') as raze:
            bot.send_video(message.chat.id, raze)
        ab = Raze().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "YORU":
        photo = open("agents_images/yoru.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія YORU")
        btn2 = types.KeyboardButton("Спеціальні здібності YORU")
        btn3 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія YORU":
        Yoru_bio = Yoru().bio()
        bot.send_message(message.chat.id, Yoru_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності YORU")
        btn2 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності YORU":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Осліплена сторона (Q)")
        btn2 = types.KeyboardButton("Незваний гість (E)")
        btn3 = types.KeyboardButton("Фейк (C)")
        btn4 = types.KeyboardButton("Просторовий дрифт (X)")
        btn5 = types.KeyboardButton("YORU")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Осліплена сторона (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/yoru/yoru3.mp4", 'rb') as yoru:
            bot.send_video(message.chat.id, yoru)
        ab = Yoru().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Незваний гість (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/yoru/yoru1.mp4", 'rb') as yoru:
            bot.send_video(message.chat.id, yoru)
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/yoru/yoru1.1.mp4", 'rb') as yoru:
            bot.send_video(message.chat.id, yoru)
        ab = Yoru().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Фейк (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/yoru/yoru2.mp4", 'rb') as yoru:
            bot.send_video(message.chat.id, yoru)
        ab = Yoru().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Просторовий дрифт (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/yoru/yoru4.mp4", 'rb') as yoru:
            bot.send_video(message.chat.id, yoru)
        ab = Yoru().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "NEON":
        photo = open("agents_images/neon.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія NEON")
        btn2 = types.KeyboardButton("Спеціальні здібності NEON")
        btn3 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія NEON":
        Neon_bio = Neon().bio()
        bot.send_message(message.chat.id, Neon_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності NEON")
        btn2 = types.KeyboardButton("ДУЕЛЯНТ (DUELIST)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності NEON":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Стрибучий снаряд (Q)")
        btn2 = types.KeyboardButton("Підвищена швидкість (E)")
        btn3 = types.KeyboardButton("Захисний тунель (C)")
        btn4 = types.KeyboardButton("На повну потужність (X)")
        btn5 = types.KeyboardButton("NEON")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Стрибучий снаряд (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/neon/neon2.mp4", 'rb') as neon:
            bot.send_video(message.chat.id, neon)
        ab = Neon().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Підвищена швидкість (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/neon/neon1.mp4", 'rb') as neon:
            bot.send_video(message.chat.id, neon)
        ab = Neon().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Захисний тунель (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/neon/neon3.mp4", 'rb') as neon:
            bot.send_video(message.chat.id, neon)
        ab = Neon().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "На повну потужність (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/neon/neon4.mp4", 'rb') as neon:
            bot.send_video(message.chat.id, neon)
        ab = Neon().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "ВАРТОВИЙ/СТРАЖ (SENTINEL)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("SAGE")
        btn2 = types.KeyboardButton("CYPHER")
        btn3 = types.KeyboardButton("KILLJOY")
        btn4 = types.KeyboardButton("CHAMBER")
        btn5 = types.KeyboardButton("Агенти")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть агента:", reply_markup=markup)

    elif message.text == "SAGE":
        photo = open("agents_images/sage.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія SAGE")
        btn2 = types.KeyboardButton("Спеціальні здібності SAGE")
        btn3 = types.KeyboardButton("ВАРТОВИЙ/СТРАЖ (SENTINEL)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія SAGE":
        Sage_bio = Sage().bio()
        bot.send_message(message.chat.id, Sage_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності SAGE")
        btn2 = types.KeyboardButton("ВАРТОВИЙ/СТРАЖ (SENTINEL)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності SAGE":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Сфера уповільнення (Q)")
        btn2 = types.KeyboardButton("Сфера лікування (E)")
        btn3 = types.KeyboardButton("Сфера бар'єра (C)")
        btn4 = types.KeyboardButton("Воскресіння (X)")
        btn5 = types.KeyboardButton("SAGE")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Сфера уповільнення (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/sage/sage2.mp4", 'rb') as sage:
            bot.send_video(message.chat.id, sage)
        ab = Sage().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Сфера лікування (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/sage/sage1.mp4", 'rb') as sage:
            bot.send_video(message.chat.id, sage)
        ab = Sage().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Сфера бар'єра (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/sage/sage3.mp4", 'rb') as sage:
            bot.send_video(message.chat.id, sage)
        ab = Sage().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Воскресіння (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/sage/sage4.mp4", 'rb') as sage:
            bot.send_video(message.chat.id, sage)
        ab = Sage().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "CYPHER":
        photo = open("agents_images/cypher.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія CYPHER")
        btn2 = types.KeyboardButton("Спеціальні здібності CYPHER")
        btn3 = types.KeyboardButton("ВАРТОВИЙ/СТРАЖ (SENTINEL)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія CYPHER":
        Cypher_bio = Cypher().bio()
        bot.send_message(message.chat.id, Cypher_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності CYPHER")
        btn2 = types.KeyboardButton("ВАРТОВИЙ/СТРАЖ (SENTINEL)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності CYPHER":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Кіберклітка (Q)")
        btn2 = types.KeyboardButton("Камера (E)")
        btn3 = types.KeyboardButton("Розтяжка (C)")
        btn4 = types.KeyboardButton("Нейрокражі (X)")
        btn5 = types.KeyboardButton("CYPHER")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Кіберклітка (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/cypher/chypher2.mp4", 'rb') as cypher:
            bot.send_video(message.chat.id, cypher)
        ab = Cypher().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Камера (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/cypher/chypher3.mp4", 'rb') as cypher:
            bot.send_video(message.chat.id, cypher)
        ab = Cypher().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Розтяжка (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/cypher/chypher1.mp4", 'rb') as cypher:
            bot.send_video(message.chat.id, cypher)
        ab = Cypher().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Нейрокражі (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/cypher/chypher4.mp4", 'rb') as cypher:
            bot.send_video(message.chat.id, cypher)
        ab = Cypher().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "KILLJOY":
        photo = open("agents_images/killjoy.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія KILLJOY")
        btn2 = types.KeyboardButton("Спеціальні здібності KILLJOY")
        btn3 = types.KeyboardButton("ВАРТОВИЙ/СТРАЖ (SENTINEL)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія KILLJOY":
        Killjoy_bio = Killjoy().bio()
        bot.send_message(message.chat.id, Killjoy_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності KILLJOY")
        btn2 = types.KeyboardButton("ВАРТОВИЙ/СТРАЖ (SENTINEL)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності KILLJOY":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Тривогобот (Q)")
        btn2 = types.KeyboardButton("Турель (E)")
        btn3 = types.KeyboardButton("Вулик (C)")
        btn4 = types.KeyboardButton("Блокування (X)")
        btn5 = types.KeyboardButton("KILLJOY")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Тривогобот (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/killjoy/kj2.mp4", 'rb') as killjoy:
            bot.send_video(message.chat.id, killjoy)
        ab = Killjoy().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Турель (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/killjoy/kj1.mp4", 'rb') as killjoy:
            bot.send_video(message.chat.id, killjoy)
        ab = Killjoy().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Вулик (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/killjoy/kj3.mp4", 'rb') as killjoy:
            bot.send_video(message.chat.id, killjoy)
        ab = Killjoy().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Блокування (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/killjoy/kj4.mp4", 'rb') as killjoy:
            bot.send_video(message.chat.id, killjoy)
        ab = Killjoy().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "CHAMBER":
        photo = open("agents_images/chamber.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія CHAMBER")
        btn2 = types.KeyboardButton("Спеціальні здібності CHAMBER")
        btn3 = types.KeyboardButton("ВАРТОВИЙ/СТРАЖ (SENTINEL)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія CHAMBER":
        Chamber_bio = Chamber().bio()
        bot.send_message(message.chat.id, Chamber_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності CHAMBER")
        btn2 = types.KeyboardButton("ВАРТОВИЙ/СТРАЖ (SENTINEL)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності CHAMBER":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Мисливець за головами (Q)")
        btn2 = types.KeyboardButton("Рандеву (E)")
        btn3 = types.KeyboardButton("Коронний пройом (C)")
        btn4 = types.KeyboardButton("Демонстрація сили (X)")
        btn5 = types.KeyboardButton("CHAMBER")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Мисливець за головами (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/chamber/chamber2.mp4", 'rb') as chamder:
            bot.send_video(message.chat.id, chamder)
        ab = Chamber().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Рандеву (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/chamber/chamber3.mp4", 'rb') as chamder:
            bot.send_video(message.chat.id, chamder)
        ab = Chamber().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Коронний пройом (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/chamber/chamber1.mp4", 'rb') as chamder:
            bot.send_video(message.chat.id, chamder)
        ab = Chamber().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Демонстрація сили (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/chamber/chamber4.mp4", 'rb') as chamder:
            bot.send_video(message.chat.id, chamder)
        ab = Chamber().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "ІНІЦІАТОР (INITIATOR)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        btn1 = types.KeyboardButton("SOVA")
        btn2 = types.KeyboardButton("BREACH")
        btn3 = types.KeyboardButton("SKYE")
        btn4 = types.KeyboardButton("KAY/O")
        btn5 = types.KeyboardButton("FADE")
        btn6 = types.KeyboardButton("GEKKO")
        btn7 = types.KeyboardButton("Агенти")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

        bot.send_message(message.chat.id,
                         f"Оберіть агента:", reply_markup=markup)

    elif message.text == "SOVA":
        photo = open("agents_images/sova.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія SOVA")
        btn2 = types.KeyboardButton("Спеціальні здібності SOVA")
        btn3 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія SOVA":
        Sova_bio = Sova().bio()
        bot.send_message(message.chat.id, Sova_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності SOVA")
        btn2 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності SOVA":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Шокова стріла (Q)")
        btn2 = types.KeyboardButton("Розвід стріла (E)")
        btn3 = types.KeyboardButton("Дрон-сова (C)")
        btn4 = types.KeyboardButton("Гнів мисливця (X)")
        btn5 = types.KeyboardButton("SOVA")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Шокова стріла (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/sova/sova3.mp4", 'rb') as sova:
            bot.send_video(message.chat.id, sova)
        ab = Sova().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Розвід стріла (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/sova/sova1.mp4", 'rb') as sova:
            bot.send_video(message.chat.id, sova)
        ab = Sova().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Дрон-сова (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/sova/sova2.mp4", 'rb') as sova:
            bot.send_video(message.chat.id, sova)
        ab = Sova().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Гнів мисливця (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/sova/sova4.mp4", 'rb') as sova:
            bot.send_video(message.chat.id, sova)
        ab = Sova().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "BREACH":
        photo = open("agents_images/breach.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія BREACH")
        btn2 = types.KeyboardButton("Спеціальні здібності BREACH")
        btn3 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія BREACH":
        Breach_bio = Breach().bio()
        bot.send_message(message.chat.id, Breach_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності BREACH")
        btn2 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності BREACH":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Сліпучий заряд (Q)")
        btn2 = types.KeyboardButton("Тріщина (E)")
        btn3 = types.KeyboardButton("Пробивний удар (C)")
        btn4 = types.KeyboardButton("Розкочування грому (X)")
        btn5 = types.KeyboardButton("BREACH")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Сліпучий заряд (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/breach/breach2.mp4", 'rb') as breach:
            bot.send_video(message.chat.id, breach)
        ab = Breach().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Тріщина (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/breach/breach3.mp4", 'rb') as breach:
            bot.send_video(message.chat.id, breach)
        ab = Breach().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Пробивний удар (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/breach/breach1.mp4", 'rb') as breach:
            bot.send_video(message.chat.id, breach)
        ab = Breach().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Розкочування грому (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/breach/breach4.mp4", 'rb') as breach:
            bot.send_video(message.chat.id, breach)
        ab = Breach().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "SKYE":
        photo = open("agents_images/skye.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія SKYE")
        btn2 = types.KeyboardButton("Спеціальні здібності SKYE")
        btn3 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія SKYE":
        Skye_bio = Skye().bio()
        bot.send_message(message.chat.id, Skye_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності SKYE")
        btn2 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності SKYE":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Слідопит (Q)")
        btn2 = types.KeyboardButton("Путівне світло (E)")
        btn3 = types.KeyboardButton("Зростання (C)")
        btn4 = types.KeyboardButton("Шукачі (X)")
        btn5 = types.KeyboardButton("SKYE")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Слідопит (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/skye/skye2.mp4", 'rb') as skye:
            bot.send_video(message.chat.id, skye)
        ab = Skye().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Путівне світло (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/skye/skye1.mp4", 'rb') as skye:
            bot.send_video(message.chat.id, skye)
        ab = Skye().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Зростання (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/skye/skye3.mp4", 'rb') as skye:
            bot.send_video(message.chat.id, skye)
        ab = Skye().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Шукачі (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/skye/skye4.mp4", 'rb') as skye:
            bot.send_video(message.chat.id, skye)
        ab = Skye().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "KAY/O":
        photo = open("agents_images/kayo.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія KAY/O")
        btn2 = types.KeyboardButton("Спеціальні здібності KAY/O")
        btn3 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія KAY/O":
        Kayo_bio = Kayo().bio()
        bot.send_message(message.chat.id, Kayo_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності KAY/O")
        btn2 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності KAY/O":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Світло/ва граната (Q)")
        btn2 = types.KeyboardButton("Епі/центр (E)")
        btn3 = types.KeyboardButton("Фраг/мент (C)")
        btn4 = types.KeyboardButton("NULL/cmd (X)")
        btn5 = types.KeyboardButton("KAY/O")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Світло/ва граната (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/kayo/kayo2.mp4", 'rb') as kayo:
            bot.send_video(message.chat.id, kayo)
        ab = Kayo().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Епі/центр (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/kayo/kayo1.mp4", 'rb') as kayo:
            bot.send_video(message.chat.id, kayo)
        ab = Kayo().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Фраг/мент (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/kayo/kayo3.mp4", 'rb') as kayo:
            bot.send_video(message.chat.id, kayo)
        ab = Kayo().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "NULL/cmd (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/kayo/kayo4.mp4", 'rb') as kayo:
            bot.send_video(message.chat.id, kayo)
        ab = Kayo().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "FADE":
        photo = open("agents_images/fade.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія FADE")
        btn2 = types.KeyboardButton("Спеціальні здібності FADE")
        btn3 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія FADE":
        Fade_bio = Fade().bio()
        bot.send_message(message.chat.id, Fade_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності FADE")
        btn2 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності FADE":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Захоплення (Q)")
        btn2 = types.KeyboardButton("Привид (E)")
        btn3 = types.KeyboardButton("Хижак (C)")
        btn4 = types.KeyboardButton("Темрява (X)")
        btn5 = types.KeyboardButton("FADE")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Захоплення (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/fade/fade3.mp4", 'rb') as fade:
            bot.send_video(message.chat.id, fade)
        ab = Fade().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Привид (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/fade/fade1.mp4", 'rb') as fade:
            bot.send_video(message.chat.id, fade)
        ab = Fade().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Хижак (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/fade/fade2.mp4", 'rb') as fade:
            bot.send_video(message.chat.id, fade)
        ab = Fade().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Темрява (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/fade/fade4.mp4", 'rb') as fade:
            bot.send_video(message.chat.id, fade)
        ab = Fade().abilities()
        bot.send_message(message.chat.id, ab['x'])

    elif message.text == "GEKKO":
        photo = open("agents_images/gekko.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Біографія GEKKO")
        btn2 = types.KeyboardButton("Спеціальні здібності GEKKO")
        btn3 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Біографія GEKKO":
        Gekko_bio = Gekko().bio()
        bot.send_message(message.chat.id, Gekko_bio)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Спеціальні здібності GEKKO")
        btn2 = types.KeyboardButton("ІНІЦІАТОР (INITIATOR)")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id,
                         f"Оберіть категорію для ознайомлення:", reply_markup=markup)

    elif message.text == "Спеціальні здібності GEKKO":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn1 = types.KeyboardButton("Wingman (Q)")
        btn2 = types.KeyboardButton("Dizzy (E)")
        btn3 = types.KeyboardButton("Mosh pit (C)")
        btn4 = types.KeyboardButton("Thrash (X)")
        btn5 = types.KeyboardButton("GEKKO")
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"Оберіть здібність:", reply_markup=markup)

    elif message.text == "Wingman (Q)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/gekko/gekko2.mp4", 'rb') as gekko:
            bot.send_video(message.chat.id, gekko)
        ab = Gekko().abilities()
        bot.send_message(message.chat.id, ab['q'])

    elif message.text == "Dizzy (E)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/gekko/gekko1.mp4", 'rb') as gekko:
            bot.send_video(message.chat.id, gekko)
        ab = Gekko().abilities()
        bot.send_message(message.chat.id, ab['e'])

    elif message.text == "Mosh pit (C)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/gekko/gekko3.mp4", 'rb') as gekko:
            bot.send_video(message.chat.id, gekko)
        ab = Gekko().abilities()
        bot.send_message(message.chat.id, ab['c'])

    elif message.text == "Thrash (X)":
        bot.send_message(message.chat.id, "Завантаження...")
        with open("abilities/gekko/gekko4.mp4", 'rb') as gekko:
            bot.send_video(message.chat.id, gekko)
        ab = Gekko().abilities()
        bot.send_message(message.chat.id, ab['x'])




bot.infinity_polling()
