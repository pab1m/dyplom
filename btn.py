from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn_for_new = KeyboardButton(text="Для новачків")
btn_stats = KeyboardButton(text="Моя статистика")
btn_help = KeyboardButton(text="Допомога")
kb_help = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
kb_help.row(btn_for_new, btn_stats, btn_help)


btn_agents = KeyboardButton(text="Агенти")
btn_maps = KeyboardButton(text="Карти")
btn_gun = KeyboardButton(text="Зброя")
btn_lobby = KeyboardButton(text="На головну")
new_player = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
new_player.add(btn_agents, btn_maps, btn_gun, btn_lobby)


btn_controller = KeyboardButton(text="СПЕЦІАЛІСТ (CONTROLLER)")
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


info_viper = InlineKeyboardMarkup(row_width=2)
btn_info_viper = InlineKeyboardButton(text="Біографія VIPER", callback_data='bio_viper')
btn_abilities_viper = InlineKeyboardButton(text="Здібності VIPER", callback_data='abilities_viper')
info_viper.add(btn_info_viper, btn_abilities_viper)


abilities_viper = InlineKeyboardMarkup(row_width=2)
btn_viper_q = InlineKeyboardButton(text="Отруйна хмара (Q)", callback_data='viper_q')
btn_viper_e = InlineKeyboardButton(text="Токсична завіса (E)", callback_data='viper_e')
btn_viper_c = InlineKeyboardButton(text="Укус змії (C)", callback_data='viper_c')
btn_viper_x = InlineKeyboardButton(text="Гніздо гадюки (X)", callback_data='viper_x')
abilities_viper.add(btn_viper_q, btn_viper_e, btn_viper_c, btn_viper_x)


info_omen = InlineKeyboardMarkup(row_width=2)
btn_info_omen = InlineKeyboardButton(text="Біографія OMEN", callback_data='bio_omen')
btn_abilities_omen = InlineKeyboardButton(text="Здібності OMEN", callback_data='abilities_omen')
info_omen.add(btn_info_omen, btn_abilities_omen)


abilities_omen = InlineKeyboardMarkup(row_width=2)
btn_omen_q = InlineKeyboardButton(text="Параноя (Q)", callback_data='omen_q')
btn_omen_e = InlineKeyboardButton(text="Темний покров (E)", callback_data='omen_e')
btn_omen_c = InlineKeyboardButton(text="Прихований крок (C)", callback_data='omen_c')
btn_omen_x = InlineKeyboardButton(text="З тіні (X)", callback_data='omen_x')
abilities_omen.add(btn_omen_q, btn_omen_e, btn_omen_c, btn_omen_x)


info_astra = InlineKeyboardMarkup(row_width=2)
btn_info_astra = InlineKeyboardButton(text="Біографія ASTRA", callback_data='bio_astra')
btn_abilities_astra = InlineKeyboardButton(text="Здібності ASTRA", callback_data='abilities_astra')
info_astra.add(btn_info_astra, btn_abilities_astra)


abilities_astra = InlineKeyboardMarkup(row_width=2)
btn_astra_q = InlineKeyboardButton(text="Вибух наднової (Q)", callback_data='astra_q')
btn_astra_e = InlineKeyboardButton(text="Туманність (E)", callback_data='astra_e')
btn_astra_c = InlineKeyboardButton(text="Гравітаційний колодязь (C)", callback_data='astra_c')
btn_astra_x = InlineKeyboardButton(text="Космічний розрив (X)", callback_data='astra_x')
abilities_astra.add(btn_astra_q, btn_astra_e, btn_astra_c, btn_astra_x)


info_harbor = InlineKeyboardMarkup(row_width=2)
btn_info_harbor = InlineKeyboardButton(text="Біографія HARBOR", callback_data='bio_harbor')
btn_abilities_harbor = InlineKeyboardButton(text="Здібності HARBOR", callback_data='abilities_harbor')
info_harbor.add(btn_info_harbor, btn_abilities_harbor)


abilities_harbor = InlineKeyboardMarkup(row_width=2)
btn_harbor_q = InlineKeyboardButton(text="Залив (Q)", callback_data='harbor_q')
btn_harbor_e = InlineKeyboardButton(text="Гребень хвилі (E)", callback_data='harbor_e')
btn_harbor_c = InlineKeyboardButton(text="Каскад (C)", callback_data='harbor_c')
btn_harbor_x = InlineKeyboardButton(text="Розрахунок курсу (X)", callback_data='harbor_x')
abilities_harbor.add(btn_harbor_q, btn_harbor_e, btn_harbor_c, btn_harbor_x)


btn_phoenix = KeyboardButton(text="PHOENIX")
btn_reyna = KeyboardButton(text="REYNA")
btn_jett = KeyboardButton(text="JETT")
btn_raze = KeyboardButton(text="RAZE")
btn_yoru = KeyboardButton(text="YORU")
btn_neon = KeyboardButton(text="NEON")
duelist = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
duelist.add(btn_phoenix, btn_reyna, btn_jett, btn_raze, btn_yoru, btn_neon).add(btn_agents)