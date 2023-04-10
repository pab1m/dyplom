from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn_for_new = KeyboardButton(text="Для новачків")
btn_stats = KeyboardButton(text="Моя статистика")
btn_help = KeyboardButton(text="Допомога")

# kb_help = InlineKeyboardMarkup(row_width=1)
# btn4 = InlineKeyboardButton(text="Test", callback_data='test')
# kb_help.row(btn4)

kb_help = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
kb_help.row(btn_for_new, btn_stats, btn_help)



btn_agents = KeyboardButton(text="Агенти")
btn_maps = KeyboardButton(text="Карти")
btn_gun = KeyboardButton(text="Зброя")
btn_lobby = KeyboardButton(text="На головну")
new_player = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
new_player.add(btn_agents, btn_maps, btn_gun, btn_lobby)




btn_controller = KeyboardButton(text="КОНТРОЛЕР (CONTROLLER)")
btn_duelist = KeyboardButton(text="ДУЕЛЯНТ (DUELIST)")
btn3_sentinel = KeyboardButton(text="ВАРТОВИЙ/СТРАЖ (SENTINEL)")
btn_initiator = KeyboardButton(text="ІНІЦІАТОР (INITIATOR)")
agents = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
agents.add(btn_controller, btn_duelist, btn3_sentinel, btn_initiator, btn_for_new)




btn_brim = KeyboardButton(text="BRIMSTONE")
btn_viper = KeyboardButton(text="VIPER")
btn_omen = KeyboardButton(text="OMEN")
btn_astra = KeyboardButton(text="ASTRA")
btn_harbor = KeyboardButton(text="HARBOR")
controller = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
controller.add(btn_brim, btn_viper, btn_omen, btn_astra, btn_harbor).add(btn_agents)


info_brim = InlineKeyboardMarkup(row_width=2)
btn_info_brim = InlineKeyboardButton(text="Біографія BRIMSTONE", callback_data='bio_brim')
btn_abilities_brim = InlineKeyboardButton(text="Здібності BRIMSTONE", callback_data='abilities_brim')

info_brim.add(btn_info_brim, btn_abilities_brim)


abilities_brim = InlineKeyboardMarkup(row_width=2)
btn_brim_q = InlineKeyboardButton(text="Запалювальна граната (Q)", callback_data='brim_q')
btn_brim_e = InlineKeyboardButton(text="Небесний дим (E)", callback_data='brim_e')
btn_brim_c = InlineKeyboardButton(text="Маячок-стимулятор (C)", callback_data='brim_c')
btn_brim_x = InlineKeyboardButton(text="Орбітальний удар (X)", callback_data='brim_x')

abilities_brim.add(btn_brim_q, btn_brim_e, btn_brim_c, btn_brim_x)


abilities_viper = InlineKeyboardMarkup(row_width=2)
btn_viper_q = InlineKeyboardButton(text="Отруйна хмара (Q)", callback_data='viper_q')
btn_viper_e = InlineKeyboardButton(text="Токсична завіса (E)", callback_data='viper_e')
btn_viper_c = InlineKeyboardButton(text="Укус змії (C)", callback_data='viper_c')
btn_viper_x = InlineKeyboardButton(text="Гніздо гадюки (X)", callback_data='viper_x')

abilities_brim.add(btn_viper_q, btn_viper_e, btn_viper_c, btn_viper_x)


