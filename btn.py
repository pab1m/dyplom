from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn_for_new = KeyboardButton(text="👶🏼 Для новачків")
btn_stats = KeyboardButton(text="📈 Моя статистика")
btn_help = KeyboardButton(text="💬 Відгук")
kb_help = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
kb_help.row(btn_for_new, btn_stats, btn_help)


btn_agents = KeyboardButton(text="👫 Агенти")
btn_maps = KeyboardButton(text="🗺 Карти")
btn_gun = KeyboardButton(text="🔫 Зброя")
btn_lobby = KeyboardButton(text="⬅️ На головну")
new_player = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
new_player.add(btn_agents, btn_maps, btn_gun, btn_lobby)

btn_stats_now = KeyboardButton(text="Статистика за цей акт")
btn_stats_all = KeyboardButton(text="Статистика за всі акти")
btn_last_5_matches = KeyboardButton(text="Інформація останнього матчу")
btn_update_nic = KeyboardButton(text="Змінити нікнейм")
stats = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
stats.add(btn_stats_now, btn_stats_all, btn_last_5_matches, btn_update_nic).add(btn_lobby)

btn_controller = KeyboardButton(text="💨 СПЕЦІАЛІСТ (CONTROLLER)")
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


info_phoenix = InlineKeyboardMarkup(row_width=2)
btn_info_phoenix = InlineKeyboardButton(text="Біографія PHOENIX", callback_data='bio_phoenix')
btn_abilities_phoenix = InlineKeyboardButton(text="Здібності PHOENIX", callback_data='abilities_phoenix')
info_phoenix.add(btn_info_phoenix, btn_abilities_phoenix)

abilities_phoenix = InlineKeyboardMarkup(row_width=2)
btn_phoenix_q = InlineKeyboardButton(text="Кручена подача (Q)", callback_data='phoenix_q')
btn_phoenix_e = InlineKeyboardButton(text="Гарячі руки (E)", callback_data='phoenix_e')
btn_phoenix_c = InlineKeyboardButton(text="Пожежа (C)", callback_data='phoenix_c')
btn_phoenix_x = InlineKeyboardButton(text="Повернення (X)", callback_data='phoenix_x')
abilities_phoenix.add(btn_phoenix_q, btn_phoenix_e, btn_phoenix_c, btn_phoenix_x)


info_reyna = InlineKeyboardMarkup(row_width=2)
btn_info_reyna = InlineKeyboardButton(text="Біографія REYNA", callback_data='bio_reyna')
btn_abilities_reyna = InlineKeyboardButton(text="Здібності REYNA", callback_data='abilities_reyna')
info_reyna.add(btn_info_reyna, btn_abilities_reyna)

abilities_reyna = InlineKeyboardMarkup(row_width=2)
btn_reyna_q = InlineKeyboardButton(text="Поглинання (Q)", callback_data='reyna_q')
btn_reyna_e = InlineKeyboardButton(text="Вигнання (E)", callback_data='reyna_e')
btn_reyna_c = InlineKeyboardButton(text="Злісний погляд (C)", callback_data='reyna_c')
btn_reyna_x = InlineKeyboardButton(text="Імператриця (X)", callback_data='reyna_x')
abilities_reyna.add(btn_reyna_q, btn_reyna_e, btn_reyna_c, btn_reyna_x)


info_jett = InlineKeyboardMarkup(row_width=2)
btn_info_jett = InlineKeyboardButton(text="Біографія JETT", callback_data='bio_jett')
btn_abilities_jett = InlineKeyboardButton(text="Здібності JETT", callback_data='abilities_jett')
info_jett.add(btn_info_jett, btn_abilities_jett)

abilities_jett = InlineKeyboardMarkup(row_width=2)
btn_jett_q = InlineKeyboardButton(text="Підйом (Q)", callback_data='jett_q')
btn_jett_e = InlineKeyboardButton(text="Попутний вітер (E)", callback_data='jett_e')
btn_jett_c = InlineKeyboardButton(text="Вихор (C)", callback_data='jett_c')
btn_jett_x = InlineKeyboardButton(text="Буря кинжалів (X)", callback_data='jett_x')
abilities_jett.add(btn_jett_q, btn_jett_e, btn_jett_c, btn_jett_x)


info_raze = InlineKeyboardMarkup(row_width=2)
btn_info_raze = InlineKeyboardButton(text="Біографія RAZE", callback_data='bio_raze')
btn_abilities_raze = InlineKeyboardButton(text="Здібності RAZE", callback_data='abilities_raze')
info_raze.add(btn_info_raze, btn_abilities_raze)

abilities_raze = InlineKeyboardMarkup(row_width=2)
btn_raze_q = InlineKeyboardButton(text="Вибуховий ранець (Q)", callback_data='raze_q')
btn_raze_e = InlineKeyboardButton(text="Касетна граната (E)", callback_data='raze_e')
btn_raze_c = InlineKeyboardButton(text="Бум бот (C)", callback_data='raze_c')
btn_raze_x = InlineKeyboardButton(text="Стоп-кадр (X)", callback_data='raze_x')
abilities_raze.add(btn_raze_q, btn_raze_e, btn_raze_c, btn_raze_x)


info_yoru = InlineKeyboardMarkup(row_width=2)
btn_info_yoru = InlineKeyboardButton(text="Біографія YORU", callback_data='bio_yoru')
btn_abilities_yoru = InlineKeyboardButton(text="Здібності YORU", callback_data='abilities_yoru')
info_yoru.add(btn_info_yoru, btn_abilities_yoru)

abilities_yoru = InlineKeyboardMarkup(row_width=2)
btn_yoru_q = InlineKeyboardButton(text="Осліплена сторона (Q)", callback_data='yoru_q')
btn_yoru_e = InlineKeyboardButton(text="Незваний гість (E)", callback_data='yoru_e')
btn_yoru_c = InlineKeyboardButton(text="Фейк (C)", callback_data='yoru_c')
btn_yoru_x = InlineKeyboardButton(text="Просторовий дрифт (X)", callback_data='yoru_x')
abilities_yoru.add(btn_yoru_q, btn_yoru_e, btn_yoru_c, btn_yoru_x)


info_neon = InlineKeyboardMarkup(row_width=2)
btn_info_neon = InlineKeyboardButton(text="Біографія NEON", callback_data='bio_neon')
btn_abilities_neon = InlineKeyboardButton(text="Здібності NEON", callback_data='abilities_neon')
info_neon.add(btn_info_neon, btn_abilities_neon)

abilities_neon = InlineKeyboardMarkup(row_width=2)
btn_neon_q = InlineKeyboardButton(text="Стрибучий снаряд (Q)", callback_data='neon_q')
btn_neon_e = InlineKeyboardButton(text="Підвищена швидкість (E)", callback_data='neon_e')
btn_neon_c = InlineKeyboardButton(text="Захисний тунель (C)", callback_data='neon_c')
btn_neon_x = InlineKeyboardButton(text="На повну потужність (X)", callback_data='neon_x')
abilities_neon.add(btn_neon_q, btn_neon_e, btn_neon_c, btn_neon_x)


btn_sage = KeyboardButton(text="SAGE")
btn_cypher = KeyboardButton(text="CYPHER")
btn_kj = KeyboardButton(text="KILLJOY")
btn_chamber = KeyboardButton(text="CHAMBER")
sentinel = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
sentinel.add(btn_sage, btn_cypher, btn_kj, btn_chamber).add(btn_agents)


info_sage = InlineKeyboardMarkup(row_width=2)
btn_info_sage = InlineKeyboardButton(text="Біографія SAGE", callback_data='bio_sage')
btn_abilities_sage = InlineKeyboardButton(text="Здібності SAGE", callback_data='abilities_sage')
info_sage.add(btn_info_sage, btn_abilities_sage)

abilities_sage = InlineKeyboardMarkup(row_width=2)
btn_sage_q = InlineKeyboardButton(text="Сфера уповільнення (Q)", callback_data='sage_q')
btn_sage_e = InlineKeyboardButton(text="Сфера лікування (E)", callback_data='sage_e')
btn_sage_c = InlineKeyboardButton(text="Сфера бар'єра (C)", callback_data='sage_c')
btn_sage_x = InlineKeyboardButton(text="Воскресіння (X)", callback_data='sage_x')
abilities_sage.add(btn_sage_q, btn_sage_e, btn_sage_c, btn_sage_x)


info_cypher = InlineKeyboardMarkup(row_width=2)
btn_info_cypher = InlineKeyboardButton(text="Біографія CYPHER", callback_data='bio_cypher')
btn_abilities_cypher = InlineKeyboardButton(text="Здібності CYPHER", callback_data='abilities_cypher')
info_cypher.add(btn_info_cypher, btn_abilities_cypher)

abilities_cypher = InlineKeyboardMarkup(row_width=2)
btn_cypher_q = InlineKeyboardButton(text="Кіберклітка (Q)", callback_data='cypher_q')
btn_cypher_e = InlineKeyboardButton(text="Камера (E)", callback_data='cypher_e')
btn_cypher_c = InlineKeyboardButton(text="Розтяжка (C)", callback_data='cypher_c')
btn_cypher_x = InlineKeyboardButton(text="Нейрокражі (X)", callback_data='cypher_x')
abilities_cypher.add(btn_cypher_q, btn_cypher_e, btn_cypher_c, btn_cypher_x)


info_kj = InlineKeyboardMarkup(row_width=2)
btn_info_kj = InlineKeyboardButton(text="Біографія KILLJOY", callback_data='bio_kj')
btn_abilities_kj = InlineKeyboardButton(text="Здібності KILLJOY", callback_data='abilities_kj')
info_kj.add(btn_info_kj, btn_abilities_kj)

abilities_kj = InlineKeyboardMarkup(row_width=2)
btn_kj_q = InlineKeyboardButton(text="Тривогобот (Q)", callback_data='kj_q')
btn_kj_e = InlineKeyboardButton(text="Турель (E)", callback_data='kj_e')
btn_kj_c = InlineKeyboardButton(text="Вулик (C)", callback_data='kj_c')
btn_kj_x = InlineKeyboardButton(text="Блокування (X)", callback_data='kj_x')
abilities_kj.add(btn_kj_q, btn_kj_e, btn_kj_c, btn_kj_x)


info_chamber = InlineKeyboardMarkup(row_width=2)
btn_info_chamber = InlineKeyboardButton(text="Біографія CHAMBER", callback_data='bio_chamber')
btn_abilities_chamber = InlineKeyboardButton(text="Здібності CHAMBER", callback_data='abilities_chamber')
info_chamber.add(btn_info_chamber, btn_abilities_chamber)

abilities_chamber = InlineKeyboardMarkup(row_width=2)
btn_chamber_q = InlineKeyboardButton(text="Мисливець за головами (Q)", callback_data='chamber_q')
btn_chamber_e = InlineKeyboardButton(text="Рандеву (E)", callback_data='chamber_e')
btn_chamber_c = InlineKeyboardButton(text="Коронний пройом (C)", callback_data='chamber_c')
btn_chamber_x = InlineKeyboardButton(text="Демонстрація сили (X)", callback_data='chamber_x')
abilities_chamber.add(btn_chamber_q, btn_chamber_e, btn_chamber_c, btn_chamber_x)


btn_sova = KeyboardButton(text="SOVA")
btn_breach = KeyboardButton(text="BREACH")
btn_skye = KeyboardButton(text="SKYE")
btn_kayo = KeyboardButton(text="KAY/O")
btn_fade = KeyboardButton(text="FADE")
btn_gekko = KeyboardButton(text="GEKKO")
initiator = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
initiator.add(btn_sova, btn_breach, btn_skye, btn_kayo, btn_fade, btn_gekko).add(btn_agents)


info_sova = InlineKeyboardMarkup(row_width=2)
btn_info_sova = InlineKeyboardButton(text="Біографія SOVA", callback_data='bio_sova')
btn_abilities_sova = InlineKeyboardButton(text="Здібності SOVA", callback_data='abilities_sova')
info_sova.add(btn_info_sova, btn_abilities_sova)

abilities_sova = InlineKeyboardMarkup(row_width=2)
btn_sova_q = InlineKeyboardButton(text="Шокова стріла (Q)", callback_data='sova_q')
btn_sova_e = InlineKeyboardButton(text="Розвід стріла (E)", callback_data='sova_e')
btn_sova_c = InlineKeyboardButton(text="Дрон-сова (C)", callback_data='sova_c')
btn_sova_x = InlineKeyboardButton(text="Гнів мисливця (X)", callback_data='sova_x')
abilities_sova.add(btn_sova_q, btn_sova_e, btn_sova_c, btn_sova_x)


info_breach = InlineKeyboardMarkup(row_width=2)
btn_info_breach = InlineKeyboardButton(text="Біографія BREACH", callback_data='bio_breach')
btn_abilities_breach = InlineKeyboardButton(text="Здібності BREACH", callback_data='abilities_breach')
info_breach.add(btn_info_breach, btn_abilities_breach)

abilities_breach = InlineKeyboardMarkup(row_width=2)
btn_breach_q = InlineKeyboardButton(text="Сліпучий заряд (Q)", callback_data='breach_q')
btn_breach_e = InlineKeyboardButton(text="Тріщина (E)", callback_data='breach_e')
btn_breach_c = InlineKeyboardButton(text="Пробивний удар (C)", callback_data='breach_c')
btn_breach_x = InlineKeyboardButton(text="Розкочування грому (X)", callback_data='breach_x')
abilities_breach.add(btn_breach_q, btn_breach_e, btn_breach_c, btn_breach_x)


info_skye = InlineKeyboardMarkup(row_width=2)
btn_info_skye = InlineKeyboardButton(text="Біографія SKYE", callback_data='bio_skye')
btn_abilities_skye = InlineKeyboardButton(text="Здібності SKYE", callback_data='abilities_skye')
info_skye.add(btn_info_skye, btn_abilities_skye)

abilities_skye = InlineKeyboardMarkup(row_width=2)
btn_skye_q = InlineKeyboardButton(text="Слідопит (Q)", callback_data='skye_q')
btn_skye_e = InlineKeyboardButton(text="Путівне світло (E)", callback_data='skye_e')
btn_skye_c = InlineKeyboardButton(text="Зростання (C)", callback_data='skye_c')
btn_skye_x = InlineKeyboardButton(text="Шукачі (X)", callback_data='skye_x')
abilities_skye.add(btn_skye_q, btn_skye_e, btn_skye_c, btn_skye_x)


info_kayo = InlineKeyboardMarkup(row_width=2)
btn_info_kayo = InlineKeyboardButton(text="Біографія KAY/O", callback_data='bio_kayo')
btn_abilities_kayo = InlineKeyboardButton(text="Здібності KAY/O", callback_data='abilities_kayo')
info_kayo.add(btn_info_kayo, btn_abilities_kayo)

abilities_kayo = InlineKeyboardMarkup(row_width=2)
btn_kayo_q = InlineKeyboardButton(text="Світло/ва граната (Q)", callback_data='kayo_q')
btn_kayo_e = InlineKeyboardButton(text="Епі/центр (E)", callback_data='kayo_e')
btn_kayo_c = InlineKeyboardButton(text="Фраг/мент (C)", callback_data='kayo_c')
btn_kayo_x = InlineKeyboardButton(text="NULL/cmd (X)", callback_data='kayo_x')
abilities_kayo.add(btn_kayo_q, btn_kayo_e, btn_kayo_c, btn_kayo_x)


info_fade = InlineKeyboardMarkup(row_width=2)
btn_info_fade = InlineKeyboardButton(text="Біографія FADE", callback_data='bio_fade')
btn_abilities_fade = InlineKeyboardButton(text="Здібності FADE", callback_data='abilities_fade')
info_fade.add(btn_info_fade, btn_abilities_fade)

abilities_fade = InlineKeyboardMarkup(row_width=2)
btn_fade_q = InlineKeyboardButton(text="Захоплення (Q)", callback_data='fade_q')
btn_fade_e = InlineKeyboardButton(text="Привид (E)", callback_data='fade_e')
btn_fade_c = InlineKeyboardButton(text="Хижак (C)", callback_data='fade_c')
btn_fade_x = InlineKeyboardButton(text="Темрява (X)", callback_data='fade_x')
abilities_fade.add(btn_fade_q, btn_fade_e, btn_fade_c, btn_fade_x)


info_gekko = InlineKeyboardMarkup(row_width=2)
btn_info_gekko = InlineKeyboardButton(text="Біографія GEKKO", callback_data='bio_gekko')
btn_abilities_gekko = InlineKeyboardButton(text="Здібності GEKKO", callback_data='abilities_gekko')
info_gekko.add(btn_info_gekko, btn_abilities_gekko)

abilities_gekko = InlineKeyboardMarkup(row_width=2)
btn_gekko_q = InlineKeyboardButton(text="Wingman (Q)", callback_data='gekko_q')
btn_gekko_e = InlineKeyboardButton(text="Dizzy (E)", callback_data='gekko_e')
btn_gekko_c = InlineKeyboardButton(text="Mosh pit (C)", callback_data='gekko_c')
btn_gekko_x = InlineKeyboardButton(text="Thrash (X)", callback_data='gekko_x')
abilities_gekko.add(btn_gekko_q, btn_gekko_e, btn_gekko_c, btn_gekko_x)


btn_lotus = KeyboardButton(text="LOTUS")
btn_pearl = KeyboardButton(text="PEARL")
btn_fracture = KeyboardButton(text="FRACTURE")
btn_breeze = KeyboardButton(text="BREEZE")
btn_icebox = KeyboardButton(text="ICEBOX")
btn_bind = KeyboardButton(text="BIND")
btn_haven = KeyboardButton(text="HAVEN")
btn_split = KeyboardButton(text="SPLIT")
btn_ascent = KeyboardButton(text="ASCENT")
maps = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
maps.add(btn_lotus, btn_pearl, btn_fracture, btn_breeze, btn_icebox, btn_bind, btn_haven, btn_split, btn_ascent).add(btn_for_new)


btn_sidearms = KeyboardButton(text="Пістолети")
btn_smgs = KeyboardButton(text="Пістолети-кулемети")
btn_snipers = KeyboardButton(text="Снайперські гвинтівки")
btn_heavies = KeyboardButton(text="Важка зброя")
btn_shotguns = KeyboardButton(text="Дробовики")
btn_rifles = KeyboardButton(text="Гвинтівки")
btn_melee = KeyboardButton(text="Холодна зброя")
weapons = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
weapons.add(btn_sidearms, btn_smgs, btn_snipers, btn_heavies).row(btn_shotguns, btn_rifles, btn_melee).add(btn_for_new)



btn_classic = KeyboardButton(text="CLASSIC")
btn_shorty = KeyboardButton(text="SHORTY")
btn_frenzy = KeyboardButton(text="FRENZY")
btn_ghost = KeyboardButton(text="GHOST")
btn_sheriff = KeyboardButton(text="SHERIFF")
sidearms = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
sidearms.add(btn_classic, btn_shorty, btn_frenzy, btn_ghost, btn_sheriff).add(btn_gun)


btn_stinger = KeyboardButton(text="STINGER")
btn_spectre = KeyboardButton(text="SPECTRE")
smgs = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
smgs.add(btn_stinger, btn_spectre).add(btn_gun)


btn_bucky = KeyboardButton(text="BUCKY")
btn_judge = KeyboardButton(text="JUDGE")
shotguns = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
shotguns.add(btn_bucky, btn_judge).add(btn_gun)


btn_bulldog = KeyboardButton(text="BULLDOG")
btn_guardian = KeyboardButton(text="GUARDIAN")
btn_phantom = KeyboardButton(text="PHANTOM")
btn_vandal = KeyboardButton(text="VANDAL")
rifles = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
rifles.add(btn_bulldog, btn_guardian, btn_phantom, btn_vandal).add(btn_gun)


btn_marshal = KeyboardButton(text="MARSHAL")
btn_operator = KeyboardButton(text="OPERATOR")
snipers = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
snipers.add(btn_marshal, btn_operator).add(btn_gun)


btn_ares = KeyboardButton(text="ARES")
btn_odin = KeyboardButton(text="ODIN")
heavies = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
heavies.add(btn_ares, btn_odin).add(btn_gun)

btn_knife = KeyboardButton(text="Тактичний ніж")
melee = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
melee.add(btn_knife).add(btn_gun)