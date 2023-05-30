import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.utils.exceptions import InvalidQueryID
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from btn import *
from all_inf import *
from maps import *
from stats_with_site import *
from weapons import *
import json
import sqlite3

TOKEN = "6116724785:AAGcm_CmDMDyKb9MN74pbh04W1zdUC3olfY"

# TOKEN = "5613158633:AAHCzJB1CZ1Gim6BLtuPJZ9NkDHKlsCm2p0" # токен від володі


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.last_name is None:
        result = message.from_user.first_name
    elif message.from_user.first_name is None:
        result = message.from_user.last_name
    elif message.from_user.first_name is None and message.from_user.last_name is None:
        result = "ХТОСЬ"
    else:
        result = f"{message.from_user.first_name} {message.from_user.last_name}"
    await bot.send_message(message.from_user.id,
                           f"Привіт, <b>{result}</b>, я телеграм бот який допоможе тобі познайомитися із грою VALORANT"
                           f" та дізнатися інформацію про свій прогрес", parse_mode='html')
    await message.delete()
    await bot.send_message(message.from_user.id, "Введіть /help щоб дізнатися мій функціонал")


@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    await bot.send_message(message.from_user.id, "Доступні команди:", reply_markup=kb_help)
    await message.delete()


@dp.message_handler(lambda message: "👶🏼 Для новачків" in message.text)
async def new_people(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer("👶🏼 Для новачків:", reply_markup=new_player)


@dp.message_handler(lambda message: "⬅️ На головну" in message.text)
async def main(messsage: types.Message):
    await messsage.answer("👶🏼 Для новачків:", reply_markup=kb_help)


class Stats(StatesGroup):
    name = State()


class update_Stats(StatesGroup):
    name = State()


@dp.message_handler(lambda message: "📈 Моя статистика" in message.text)
async def my_stats(messsage: types.Message):
    id_user = messsage.from_user.id

    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM users WHERE id = {id_user}")
    result = cursor.fetchone()
    if result is not None:
        await messsage.answer("✅ Ви успішно авторизувалися ✅")
        await messsage.answer("Оберіть потрібну статистику:", reply_markup=stats)
    else:
        await messsage.answer("Введіть повний нікнейм (Name Example#1234):")
        await Stats.name.set()


@dp.message_handler(state=Stats.name)
async def my_staats(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    id_user = message.from_user.id

    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT id FROM users WHERE id = {id_user}")
    result = cursor.fetchone()

    if result is None:
        cursor.execute(f"INSERT INTO users (id, name) VALUES ({id_user}, '{data['name']}')")
        await message.answer("❗Вас додано в базу даних❗")
        await state.finish()
    conn.commit()
    conn.close()
    await message.answer("Оберіть потрібну статистику:", reply_markup=stats)


@dp.message_handler(lambda message: "🔁 Змінити нікнейм" in message.text)
async def update_nickname(message: types.Message):
    await message.answer("Введіть новий нікнейм (Name Example#1234):")
    await update_Stats.name.set()


@dp.message_handler(state=update_Stats.name)
async def update_nickname_confirm(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users SET name = '{data['name']}' WHERE id = {message.from_user.id}")
    conn.commit()
    conn.close()

    await state.finish()
    await message.answer(f"Новий нікнейм збережено: <b>{data['name']}</b>", parse_mode='html', reply_markup=stats)


@dp.message_handler(lambda message: "1️⃣ Статистика за цей акт" in message.text)
async def now_stats(message: types.Message):
    try:
        await message.answer("Завантаження статистики . . .")
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM users WHERE id = {message.from_user.id}")
        res = cursor.fetchone()
        stats_now(res[0])

        q = []
        with open(f'{res[0]}.json', 'r') as f:
            my_dict = json.load(f)
        title_list = list(my_dict)
        for i in range(0, 4):
            q.append(f"{title_list[i]}: <b>{my_dict[title_list[i]]}</b>")

        result = '\n\n'.join(q)
        await message.answer(result, parse_mode='html')
        os.remove(f'{res[0]}.json')
    except:
        await message.answer(text=f"❗Користувача із заданим нікнеймом не існує, або профіль приватний❗")
        os.remove(f'{res[0]}.json')


@dp.message_handler(lambda message: "🔟 Статистика за всі акти" in message.text)
async def now_stats(message: types.Message):
    try:
        await message.answer("Завантаження статистики . . .")
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM users WHERE id = {message.from_user.id}")
        res = cursor.fetchone()
        stats_all(res[0])

        q = []
        with open(f'{res[0]}.json', 'r') as f:
            my_dict = json.load(f)
        title_list = list(my_dict)
        for i in range(0, 4):
            q.append(f"{title_list[i]}: <b>{my_dict[title_list[i]]}</b>")

        result = '\n\n'.join(q)
        await message.answer(result, parse_mode='html')
        os.remove(f'{res[0]}.json')
    except:
        await message.answer(text=f"❗Користувача із заданим нікнеймом не існує, або профіль приватний❗")
        os.remove(f'{res[0]}.json')

@dp.message_handler(lambda message: "⚔ Інформація останнього матчу" in message.text)
async def now_stats(message: types.Message):
    try:
        await message.answer("Завантаження інформації . . .")
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM users WHERE id = {message.from_user.id}")
        res = cursor.fetchone()
        stats_last_game(res[0])

        q = []
        with open(f'{res[0]}.json', 'r') as f:
            my_dict = json.load(f)
        title_list = list(my_dict)

        q.append(f"{title_list[0]}: <b>{my_dict[title_list[0]]}</b> \n\n{title_list[1]}: <b>{my_dict[title_list[1]]}</b> "
                 f"\n\nРахунок: <b>{my_dict[title_list[2]]}:{my_dict[title_list[3]]} {'(Win)' if my_dict[title_list[2]] > my_dict[title_list[3]] else '(Defeat)'}</b> "
                 f"\n\n{title_list[4]}: <b>{my_dict[title_list[4]]}</b> \n\n{title_list[5]}: <b>{my_dict[title_list[5]]}</b>"
                 f"\n\n{title_list[6]}: <b>{my_dict[title_list[6]]}</b> \n\n{title_list[7]}: <b>{my_dict[title_list[7]]}</b>")
        result = '\n\n'.join(q)
        await message.answer(result, parse_mode='html')
        os.remove(f'{res[0]}.json')
    except:
        await message.answer(text=f"❗Користувача із заданим нікнеймом не існує, або профіль приватний❗")

class feedback(StatesGroup):
    text = State()


@dp.message_handler(lambda message: "💬 Відгук" in message.text)
async def feedbacks(message: types.Message):
    await message.answer("Напишіть відгук:")
    await feedback.text.set()


@dp.message_handler(state=feedback.text)
async def send_feedback(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text

    id_user = message.from_user.id
    name_user = message.from_user.first_name

    conn = sqlite3.connect('feedbacks.db')
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO feedbacks (user_id, user_name, text) VALUES ({id_user}, '{name_user}', '{data['text']}')")
    conn.commit()
    conn.close()

    await state.finish()
    await message.answer("✅ Дякуємо за ваш відгук ✅", reply_markup=kb_help)


@dp.message_handler(lambda message: '👫 Агенти' in message.text)
async def new_people(message: types.Message):
    delete = await message.answer('Агенти:')
    await delete.delete()
    await bot.send_message(chat_id=message.from_user.id, text='Оберіть клас агента: ', reply_markup=agents)


@dp.message_handler(lambda message: "💨 СПЕЦІАЛІСТ" in message.text)
async def controllers(message: types.Message):
    delete = await bot.send_message(message.from_user.id, '💨 СПЕЦІАЛІСТ')
    await delete.delete()
    await bot.send_message(chat_id=message.from_user.id, text='Оберіть агента: ', reply_markup=controller)


@dp.message_handler(text=['👑 BRIMSTONE'])
async def brim(message: types.Message):
    photo = types.InputFile('agents_images/brimstone.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_brim)

    @dp.callback_query_handler(text='bio_brim')
    async def bio_brim(callback: types.CallbackQuery):
        Brim_bio = Brim().bio()
        await callback.message.answer(Brim_bio)
        await callback.answer()

    @dp.callback_query_handler(text='abilities_brim')
    async def ab_brim(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()

    @dp.callback_query_handler(text='brim_q')
    async def ab_brim_q(callback: types.CallbackQuery):
        try:
            with open("abilities/brimstone/brim3.mp4", 'rb') as brim:
                await bot.send_video(chat_id=callback.from_user.id, video=brim)
            ab = Brim().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_brim)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='brim_e')
    async def ab_brim_e(callback: types.CallbackQuery):
        try:
            with open("abilities/brimstone/brim1.mp4", 'rb') as brim:
                await bot.send_video(chat_id=callback.from_user.id, video=brim)
            ab = Brim().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_brim)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='brim_c')
    async def ab_brim_c(callback: types.CallbackQuery):
        try:
            with open("abilities/brimstone/brim2.mp4", 'rb') as brim:
                await bot.send_video(chat_id=callback.from_user.id, video=brim)
            ab = Brim().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_brim)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='brim_x')
    async def ab_brim_x(callback: types.CallbackQuery):
        try:
            with open("abilities/brimstone/brim4.mp4", 'rb') as brim:
                await bot.send_video(chat_id=callback.from_user.id, video=brim)
            ab = Brim().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_brim)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🐍 VIPER'])
async def viper(message: types.Message):
    photo = types.InputFile('agents_images/viper.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_viper)

    @dp.callback_query_handler(text='bio_viper')
    async def bio_viper(callback: types.CallbackQuery):
        Viper_bio = Viper().bio()
        await callback.message.answer(Viper_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_viper')
    async def ab_viper(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_viper)
        await callback.answer()

    @dp.callback_query_handler(text='viper_q')
    async def ab_viper_q(callback: types.CallbackQuery):
        try:
            with open("abilities/viper/viper2.mp4", 'rb') as viper:
                await bot.send_video(chat_id=callback.from_user.id, video=viper)
            ab = Viper().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_viper)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='viper_e')
    async def ab_viper_e(callback: types.CallbackQuery):
        try:
            with open("abilities/viper/viper1.mp4", 'rb') as viper:
                await bot.send_video(chat_id=callback.from_user.id, video=viper)
            ab = Viper().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_viper)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='viper_c')
    async def ab_viper_c(callback: types.CallbackQuery):
        try:
            with open("abilities/viper/viper3.mp4", 'rb') as viper:
                await bot.send_video(chat_id=callback.from_user.id, video=viper)
            ab = Viper().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_viper)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='viper_x')
    async def ab_viper_x(callback: types.CallbackQuery):
        try:
            with open("abilities/viper/viper4.mp4", 'rb') as viper:
                await bot.send_video(chat_id=callback.from_user.id, video=viper)
            ab = Viper().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_viper)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🦑 OMEN'])
async def omen(message: types.Message):
    photo = types.InputFile('agents_images/omen.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_omen)

    @dp.callback_query_handler(text='bio_omen')
    async def bio_omen(callback: types.CallbackQuery):
        Omen_bio = Omen().bio()
        await callback.message.answer(Omen_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_omen')
    async def ab_omen(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_omen)
        await callback.answer()

    @dp.callback_query_handler(text='omen_q')
    async def ab_omen_q(callback: types.CallbackQuery):
        try:
            with open("abilities/omen/omen2.mp4", 'rb') as omen:
                await bot.send_video(chat_id=callback.from_user.id, video=omen)
            ab = Omen().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_omen)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='omen_e')
    async def ab_omen_e(callback: types.CallbackQuery):
        try:
            with open("abilities/omen/omen1.mp4", 'rb') as omen:
                await bot.send_video(chat_id=callback.from_user.id, video=omen)
            ab = Omen().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_omen)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='omen_c')
    async def ab_omen_c(callback: types.CallbackQuery):
        try:
            with open("abilities/omen/omen3.mp4", 'rb') as omen:
                await bot.send_video(chat_id=callback.from_user.id, video=omen)
            ab = Omen().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_omen)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='omen_x')
    async def ab_omen_x(callback: types.CallbackQuery):
        try:
            with open("abilities/omen/omen4.mp4", 'rb') as omen:
                await bot.send_video(chat_id=callback.from_user.id, video=omen)
            ab = Omen().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_omen)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🌟 ASTRA'])
async def astra(message: types.Message):
    photo = types.InputFile('agents_images/astra.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_astra)

    @dp.callback_query_handler(text='bio_astra')
    async def bio_astra(callback: types.CallbackQuery):
        Astra_bio = Astra().bio()
        await callback.message.answer(Astra_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_astra')
    async def ab_astra(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_astra)
        await callback.answer()

    @dp.callback_query_handler(text='astra_q')
    async def ab_astra_q(callback: types.CallbackQuery):
        try:
            with open("abilities/astra/astra3.mp4", 'rb') as astra:
                await bot.send_video(chat_id=callback.from_user.id, video=astra)
            ab = Astra().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_astra)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='astra_e')
    async def ab_astra_e(callback: types.CallbackQuery):
        try:
            with open("abilities/astra/astra2.mp4", 'rb') as astra:
                await bot.send_video(chat_id=callback.from_user.id, video=astra)
            ab = Astra().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_astra)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='astra_c')
    async def ab_astra_c(callback: types.CallbackQuery):
        try:
            with open("abilities/astra/astra1.mp4", 'rb') as astra:
                await bot.send_video(chat_id=callback.from_user.id, video=astra)
            ab = Astra().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_astra)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='astra_x')
    async def ab_astra_x(callback: types.CallbackQuery):
        try:
            with open("abilities/astra/astra4.mp4", 'rb') as astra:
                await bot.send_video(chat_id=callback.from_user.id, video=astra)
            ab = Astra().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_astra)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🌊 HARBOR'])
async def harbor(message: types.Message):
    photo = types.InputFile('agents_images/harbor.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_harbor)

    @dp.callback_query_handler(text='bio_harbor')
    async def bio_harbor(callback: types.CallbackQuery):
        Harbor_bio = Harbor().bio()
        await callback.message.answer(Harbor_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_harbor')
    async def ab_harbor(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_harbor)
        await callback.answer()

    @dp.callback_query_handler(text='harbor_q')
    async def ab_harbor_q(callback: types.CallbackQuery):
        try:
            with open("abilities/harbor/harbor2.mp4", 'rb') as harbor:
                await bot.send_video(chat_id=callback.from_user.id, video=harbor)
            ab = Harbor().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_harbor)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='harbor_e')
    async def ab_harbor_e(callback: types.CallbackQuery):
        try:
            with open("abilities/harbor/harbor1.mp4", 'rb') as harbor:
                await bot.send_video(chat_id=callback.from_user.id, video=harbor)
            ab = Harbor().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_harbor)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='harbor_c')
    async def ab_harbor_c(callback: types.CallbackQuery):
        try:
            with open("abilities/harbor/harbor3.mp4", 'rb') as harbor:
                await bot.send_video(chat_id=callback.from_user.id, video=harbor)
            ab = Harbor().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_harbor)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='harbor_x')
    async def ab_harbor_x(callback: types.CallbackQuery):
        try:
            with open("abilities/harbor/harbor4.mp4", 'rb') as harbor:
                await bot.send_video(chat_id=callback.from_user.id, video=harbor)
            ab = Harbor().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_harbor)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(lambda message: "⚔ ДУЕЛЯНТ" in message.text)
async def duelists(message: types.Message):
    delete = await bot.send_message(message.from_user.id, "⚔ ДУЕЛЯНТ")
    await delete.delete()
    await bot.send_message(chat_id=message.from_user.id, text='Оберіть агента: ', reply_markup=duelist)


@dp.message_handler(text=['🔥 PHOENIX'])
async def phoenix(message: types.Message):
    photo = types.InputFile('agents_images/phoenix.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_phoenix)

    @dp.callback_query_handler(text='bio_phoenix')
    async def bio_phoenix(callback: types.CallbackQuery):
        Phoenix_bio = Phoenix().bio()
        await callback.message.answer(Phoenix_bio)
        await callback.answer()

    @dp.callback_query_handler(text='abilities_phoenix')
    async def ab_phoenix(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_phoenix)
        await callback.answer()

    @dp.callback_query_handler(text='phoenix_q')
    async def ab_phoenix_q(callback: types.CallbackQuery):
        try:
            with open("abilities/phoenix/phoenix2.mp4", 'rb') as phoenix:
                await bot.send_video(chat_id=callback.from_user.id, video=phoenix)
            ab = Phoenix().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_phoenix)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='phoenix_e')
    async def ab_phoenix_e(callback: types.CallbackQuery):
        try:
            with open("abilities/phoenix/phoenix1.mp4", 'rb') as phoenix:
                await bot.send_video(chat_id=callback.from_user.id, video=phoenix)
            with open("abilities/phoenix/phoenix1.1.mp4", 'rb') as phoenix:
                await bot.send_video(chat_id=callback.from_user.id, video=phoenix)
            ab = Phoenix().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_phoenix)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='phoenix_c')
    async def ab_phoenix_c(callback: types.CallbackQuery):
        try:
            with open("abilities/phoenix/phoenix3.mp4", 'rb') as phoenix:
                await bot.send_video(chat_id=callback.from_user.id, video=phoenix)
            ab = Phoenix().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_phoenix)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='phoenix_x')
    async def ab_phoenix_x(callback: types.CallbackQuery):
        try:
            with open("abilities/phoenix/phoenix4.mp4", 'rb') as phoenix:
                await bot.send_video(chat_id=callback.from_user.id, video=phoenix)
            ab = Phoenix().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_phoenix)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['👁 REYNA'])
async def reyna(message: types.Message):
    photo = types.InputFile('agents_images/reyna.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_reyna)

    @dp.callback_query_handler(text='bio_reyna')
    async def bio_reyna(callback: types.CallbackQuery):
        Reyna_bio = Reyna().bio()
        await callback.message.answer(Reyna_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_reyna')
    async def ab_reyna(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_reyna)
        await callback.answer()

    @dp.callback_query_handler(text='reyna_q')
    async def ab_reyna_q(callback: types.CallbackQuery):
        try:
            with open("abilities/reyna/reyna2.mp4", 'rb') as reyna:
                await bot.send_video(chat_id=callback.from_user.id, video=reyna)
            ab = Reyna().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_reyna)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='reyna_e')
    async def ab_reyna_e(callback: types.CallbackQuery):
        try:
            with open("abilities/reyna/reyna3.mp4", 'rb') as reyna:
                await bot.send_video(chat_id=callback.from_user.id, video=reyna)
            ab = Reyna().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_reyna)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='reyna_c')
    async def ab_reyna_c(callback: types.CallbackQuery):
        try:
            with open("abilities/reyna/reyna1.mp4", 'rb') as reyna:
                await bot.send_video(chat_id=callback.from_user.id, video=reyna)
            ab = Reyna().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_reyna)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='reyna_x')
    async def ab_reyna_x(callback: types.CallbackQuery):
        try:
            with open("abilities/reyna/reyna4.mp4", 'rb') as reyna:
                await bot.send_video(chat_id=callback.from_user.id, video=reyna)
            ab = Reyna().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_reyna)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🌪 JETT'])
async def jett(message: types.Message):
    photo = types.InputFile('agents_images/jett.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_jett)

    @dp.callback_query_handler(text='bio_jett')
    async def bio_jett(callback: types.CallbackQuery):
        Jett_bio = Jett().bio()
        await callback.message.answer(Jett_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_jett')
    async def ab_jett(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_jett)
        await callback.answer()

    @dp.callback_query_handler(text='jett_q')
    async def ab_jett_q(callback: types.CallbackQuery):
        try:
            with open("abilities/jett/jett2.mp4", 'rb') as jett:
                await bot.send_video(chat_id=callback.from_user.id, video=jett)
            ab = Jett().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_jett)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='jett_e')
    async def ab_jett_e(callback: types.CallbackQuery):
        try:
            with open("abilities/jett/jett1.mp4", 'rb') as jett:
                await bot.send_video(chat_id=callback.from_user.id, video=jett)
            ab = Jett().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_jett)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='jett_c')
    async def ab_jett_c(callback: types.CallbackQuery):
        try:
            with open("abilities/jett/jett3.mp4", 'rb') as jett:
                await bot.send_video(chat_id=callback.from_user.id, video=jett)
            ab = Jett().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_jett)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='jett_x')
    async def ab_jett_x(callback: types.CallbackQuery):
        try:
            with open("abilities/jett/jett4.mp4", 'rb') as jett:
                await bot.send_video(chat_id=callback.from_user.id, video=jett)
            ab = Jett().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_jett)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['💣 RAZE'])
async def raze(message: types.Message):
    photo = types.InputFile('agents_images/raze.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_raze)

    @dp.callback_query_handler(text='bio_raze')
    async def bio_raze(callback: types.CallbackQuery):
        Raze_bio = Raze().bio()
        await callback.message.answer(Raze_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_raze')
    async def ab_raze(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_raze)
        await callback.answer()

    @dp.callback_query_handler(text='raze_q')
    async def ab_raze_q(callback: types.CallbackQuery):
        try:
            with open("abilities/raze/raze2.mp4", 'rb') as raze:
                await bot.send_video(chat_id=callback.from_user.id, video=raze)
            ab = Raze().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_raze)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='raze_e')
    async def ab_raze_e(callback: types.CallbackQuery):
        try:
            with open("abilities/raze/raze1.mp4", 'rb') as raze:
                await bot.send_video(chat_id=callback.from_user.id, video=raze)
            ab = Raze().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_raze)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='raze_c')
    async def ab_raze_c(callback: types.CallbackQuery):
        try:
            with open("abilities/raze/raze3.mp4", 'rb') as raze:
                await bot.send_video(chat_id=callback.from_user.id, video=raze)
            ab = Raze().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_raze)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='raze_x')
    async def ab_raze_x(callback: types.CallbackQuery):
        try:
            with open("abilities/raze/raze4.mp4", 'rb') as raze:
                await bot.send_video(chat_id=callback.from_user.id, video=raze)
            ab = Raze().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_raze)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['👥 YORU'])
async def yoru(message: types.Message):
    photo = types.InputFile('agents_images/yoru.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_yoru)

    @dp.callback_query_handler(text='bio_yoru')
    async def bio_yoru(callback: types.CallbackQuery):
        Yoru_bio = Yoru().bio()
        await callback.message.answer(Yoru_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_yoru')
    async def ab_yoru(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_yoru)
        await callback.answer()

    @dp.callback_query_handler(text='yoru_q')
    async def ab_yoru_q(callback: types.CallbackQuery):
        try:
            with open("abilities/yoru/yoru3.mp4", 'rb') as yoru:
                await bot.send_video(chat_id=callback.from_user.id, video=yoru)
            ab = Yoru().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_yoru)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='yoru_e')
    async def ab_yoru_e(callback: types.CallbackQuery):
        try:
            with open("abilities/yoru/yoru1.mp4", 'rb') as yoru:
                await bot.send_video(chat_id=callback.from_user.id, video=yoru)
            with open("abilities/yoru/yoru1.1.mp4", 'rb') as yoru:
                await bot.send_video(chat_id=callback.from_user.id, video=yoru)
            ab = Yoru().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_yoru)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='yoru_c')
    async def ab_yoru_c(callback: types.CallbackQuery):
        try:
            with open("abilities/yoru/yoru2.mp4", 'rb') as yoru:
                await bot.send_video(chat_id=callback.from_user.id, video=yoru)
            ab = Yoru().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_yoru)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='yoru_x')
    async def ab_yoru_x(callback: types.CallbackQuery):
        try:
            with open("abilities/yoru/yoru4.mp4", 'rb') as yoru:
                await bot.send_video(chat_id=callback.from_user.id, video=yoru)
            ab = Yoru().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_yoru)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['⚡ NEON'])
async def neon(message: types.Message):
    photo = types.InputFile('agents_images/neon.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_neon)

    @dp.callback_query_handler(text='bio_neon')
    async def bio_neon(callback: types.CallbackQuery):
        Neon_bio = Neon().bio()
        await callback.message.answer(Neon_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_neon')
    async def ab_neon(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_neon)
        await callback.answer()

    @dp.callback_query_handler(text='neon_q')
    async def ab_neon_q(callback: types.CallbackQuery):
        try:
            with open("abilities/neon/neon2.mp4", 'rb') as neon:
                await bot.send_video(chat_id=callback.from_user.id, video=neon)
            ab = Neon().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_neon)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='neon_e')
    async def ab_neon_e(callback: types.CallbackQuery):
        try:
            with open("abilities/neon/neon1.mp4", 'rb') as neon:
                await bot.send_video(chat_id=callback.from_user.id, video=neon)
            ab = Neon().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_neon)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='neon_c')
    async def ab_neon_c(callback: types.CallbackQuery):
        try:
            with open("abilities/neon/neon3.mp4", 'rb') as neon:
                await bot.send_video(chat_id=callback.from_user.id, video=neon)
            ab = Neon().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_neon)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='neon_x')
    async def ab_neon_x(callback: types.CallbackQuery):
        try:
            with open("abilities/neon/neon4.mp4", 'rb') as neon:
                await bot.send_video(chat_id=callback.from_user.id, video=neon)
            ab = Neon().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_neon)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(lambda message: "📸 ВАРТОВИЙ" in message.text)
async def sentinels(message: types.Message):
    delete = await bot.send_message(message.from_user.id, "📸 ВАРТОВИЙ")
    await delete.delete()
    await bot.send_message(chat_id=message.from_user.id, text='Оберіть агента: ', reply_markup=sentinel)


@dp.message_handler(text=['💊 SAGE'])
async def sage(message: types.Message):
    photo = types.InputFile('agents_images/sage.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_sage)

    @dp.callback_query_handler(text='bio_sage')
    async def bio_sage(callback: types.CallbackQuery):
        Sage_bio = Sage().bio()
        await callback.message.answer(Sage_bio)
        await callback.answer()

    @dp.callback_query_handler(text='abilities_sage')
    async def ab_sage(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_sage)
        await callback.answer()

    @dp.callback_query_handler(text='sage_q')
    async def ab_sage_q(callback: types.CallbackQuery):
        try:
            with open("abilities/sage/sage2.mp4", 'rb') as sage:
                await bot.send_video(chat_id=callback.from_user.id, video=sage)
            ab = Sage().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_sage)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='sage_e')
    async def ab_sage_e(callback: types.CallbackQuery):
        try:
            with open("abilities/sage/sage1.mp4", 'rb') as sage:
                await bot.send_video(chat_id=callback.from_user.id, video=sage)
            ab = Sage().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_sage)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='sage_c')
    async def ab_sage_c(callback: types.CallbackQuery):
        try:
            with open("abilities/sage/sage3.mp4", 'rb') as sage:
                await bot.send_video(chat_id=callback.from_user.id, video=sage)
            ab = Sage().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_sage)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='sage_x')
    async def ab_sage_x(callback: types.CallbackQuery):
        try:
            with open("abilities/sage/sage4.mp4", 'rb') as sage:
                await bot.send_video(chat_id=callback.from_user.id, video=sage)
            ab = Sage().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_sage)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['📷 CYPHER'])
async def cypher(message: types.Message):
    photo = types.InputFile('agents_images/cypher.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_cypher)

    @dp.callback_query_handler(text='bio_cypher')
    async def bio_cypher(callback: types.CallbackQuery):
        Cypher_bio = Cypher().bio()
        await callback.message.answer(Cypher_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_cypher')
    async def ab_cypher(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_cypher)
        await callback.answer()

    @dp.callback_query_handler(text='cypher_q')
    async def ab_cypher_q(callback: types.CallbackQuery):
        try:
            with open("abilities/cypher/chypher2.mp4", 'rb') as cypher:
                await bot.send_video(chat_id=callback.from_user.id, video=cypher)
            ab = Cypher().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_cypher)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='cypher_e')
    async def ab_cypher_e(callback: types.CallbackQuery):
        try:
            with open("abilities/cypher/chypher3.mp4", 'rb') as cypher:
                await bot.send_video(chat_id=callback.from_user.id, video=cypher)
            ab = Cypher().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_cypher)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='cypher_c')
    async def ab_cypher_c(callback: types.CallbackQuery):
        try:
            with open("abilities/cypher/chypher1.mp4", 'rb') as cypher:
                await bot.send_video(chat_id=callback.from_user.id, video=cypher)
            ab = Cypher().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_cypher)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='cypher_x')
    async def ab_cypher_x(callback: types.CallbackQuery):
        try:
            with open("abilities/cypher/chypher4.mp4", 'rb') as cypher:
                await bot.send_video(chat_id=callback.from_user.id, video=cypher)
            ab = Cypher().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_cypher)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🕹 KILLJOY'])
async def killjoy(message: types.Message):
    photo = types.InputFile('agents_images/killjoy.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_kj)

    @dp.callback_query_handler(text='bio_kj')
    async def bio_kj(callback: types.CallbackQuery):
        Killjoy_bio = Killjoy().bio()
        await callback.message.answer(Killjoy_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_kj')
    async def ab_kj(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_kj)
        await callback.answer()

    @dp.callback_query_handler(text='kj_q')
    async def ab_kj_q(callback: types.CallbackQuery):
        try:
            with open("abilities/killjoy/kj2.mp4", 'rb') as kj:
                await bot.send_video(chat_id=callback.from_user.id, video=kj)
            ab = Killjoy().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_kj)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='kj_e')
    async def ab_kj_e(callback: types.CallbackQuery):
        try:
            with open("abilities/killjoy/kj1.mp4", 'rb') as kj:
                await bot.send_video(chat_id=callback.from_user.id, video=kj)
            ab = Killjoy().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_kj)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='kj_c')
    async def ab_kj_c(callback: types.CallbackQuery):
        try:
            with open("abilities/killjoy/kj3.mp4", 'rb') as kj:
                await bot.send_video(chat_id=callback.from_user.id, video=kj)
            ab = Killjoy().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_kj)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='kj_x')
    async def ab_kj_x(callback: types.CallbackQuery):
        try:
            with open("abilities/killjoy/kj4.mp4", 'rb') as kj:
                await bot.send_video(chat_id=callback.from_user.id, video=kj)
            ab = Killjoy().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_kj)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🔫 CHAMBER'])
async def chamber(message: types.Message):
    photo = types.InputFile('agents_images/chamber.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_chamber)

    @dp.callback_query_handler(text='bio_chamber')
    async def bio_chamber(callback: types.CallbackQuery):
        Chamber_bio = Chamber().bio()
        await callback.message.answer(Chamber_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_chamber')
    async def ab_chamber(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_chamber)
        await callback.answer()

    @dp.callback_query_handler(text='chamber_q')
    async def ab_chamber_q(callback: types.CallbackQuery):
        try:
            with open("abilities/chamber/chamber2.mp4", 'rb') as chamber:
                await bot.send_video(chat_id=callback.from_user.id, video=chamber)
            ab = Chamber().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_chamber)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='chamber_e')
    async def ab_chamber_e(callback: types.CallbackQuery):
        try:
            with open("abilities/chamber/chamber3.mp4", 'rb') as chamber:
                await bot.send_video(chat_id=callback.from_user.id, video=chamber)
            ab = Chamber().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_chamber)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='chamber_c')
    async def ab_chamber_c(callback: types.CallbackQuery):
        try:
            with open("abilities/chamber/chamber1.mp4", 'rb') as chamber:
                await bot.send_video(chat_id=callback.from_user.id, video=chamber)
            ab = Chamber().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_chamber)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='chamber_x')
    async def ab_chamber_x(callback: types.CallbackQuery):
        try:
            with open("abilities/chamber/chamber4.mp4", 'rb') as chamber:
                await bot.send_video(chat_id=callback.from_user.id, video=chamber)
            ab = Chamber().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_chamber)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(lambda message: "🎯 ІНІЦІАТОР" in message.text)
async def initiators(message: types.Message):
    delete = await bot.send_message(message.from_user.id, "🎯 ІНІЦІАТОР")
    await delete.delete()
    await bot.send_message(chat_id=message.from_user.id, text='Оберіть агента: ', reply_markup=initiator)


@dp.message_handler(text=['🏹 SOVA'])
async def sova(message: types.Message):
    photo = types.InputFile('agents_images/sova.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_sova)

    @dp.callback_query_handler(text='bio_sova')
    async def bio_sova(callback: types.CallbackQuery):
        Sova_bio = Sova().bio()
        await callback.message.answer(Sova_bio)
        await callback.answer()

    @dp.callback_query_handler(text='abilities_sova')
    async def ab_sova(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_sova)
        await callback.answer()

    @dp.callback_query_handler(text='sova_q')
    async def ab_sova_q(callback: types.CallbackQuery):
        try:
            with open("abilities/sova/sova3.mp4", 'rb') as sova:
                await bot.send_video(chat_id=callback.from_user.id, video=sova)
            ab = Sova().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_sova)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='sova_e')
    async def ab_sova_e(callback: types.CallbackQuery):
        try:
            with open("abilities/sova/sova1.mp4", 'rb') as sova:
                await bot.send_video(chat_id=callback.from_user.id, video=sova)
            ab = Sova().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_sova)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='sova_c')
    async def ab_sova_c(callback: types.CallbackQuery):
        try:
            with open("abilities/sova/sova2.mp4", 'rb') as sova:
                await bot.send_video(chat_id=callback.from_user.id, video=sova)
            ab = Sova().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_sova)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='sova_x')
    async def ab_sova_x(callback: types.CallbackQuery):
        try:
            with open("abilities/sova/sova4.mp4", 'rb') as sova:
                await bot.send_video(chat_id=callback.from_user.id, video=sova)
            ab = Sova().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_sova)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['💫 BREACH'])
async def breach(message: types.Message):
    photo = types.InputFile('agents_images/breach.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_breach)

    @dp.callback_query_handler(text='bio_breach')
    async def bio_breach(callback: types.CallbackQuery):
        Breach_bio = Breach().bio()
        await callback.message.answer(Breach_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_breach')
    async def ab_breach(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_breach)
        await callback.answer()

    @dp.callback_query_handler(text='breach_q')
    async def ab_breach_q(callback: types.CallbackQuery):
        try:
            with open("abilities/breach/breach2.mp4", 'rb') as breach:
                await bot.send_video(chat_id=callback.from_user.id, video=breach)
            ab = Breach().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_breach)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='breach_e')
    async def ab_breach_e(callback: types.CallbackQuery):
        try:
            with open("abilities/breach/breach3.mp4", 'rb') as breach:
                await bot.send_video(chat_id=callback.from_user.id, video=breach)
            ab = Breach().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_breach)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='breach_c')
    async def ab_breach_c(callback: types.CallbackQuery):
        try:
            with open("abilities/breach/breach1.mp4", 'rb') as breach:
                await bot.send_video(chat_id=callback.from_user.id, video=breach)
            ab = Breach().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_breach)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='breach_x')
    async def ab_breach_x(callback: types.CallbackQuery):
        try:
            with open("abilities/breach/breach4.mp4", 'rb') as breach:
                await bot.send_video(chat_id=callback.from_user.id, video=breach)
            ab = Breach().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_breach)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🦜 SKYE'])
async def skye(message: types.Message):
    photo = types.InputFile('agents_images/skye.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_skye)

    @dp.callback_query_handler(text='bio_skye')
    async def bio_skye(callback: types.CallbackQuery):
        Skye_bio = Skye().bio()
        await callback.message.answer(Skye_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_skye')
    async def ab_skye(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_skye)
        await callback.answer()

    @dp.callback_query_handler(text='skye_q')
    async def ab_skye_q(callback: types.CallbackQuery):
        try:
            with open("abilities/skye/skye2.mp4", 'rb') as skye:
                await bot.send_video(chat_id=callback.from_user.id, video=skye)
            ab = Skye().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_skye)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='skye_e')
    async def ab_skye_e(callback: types.CallbackQuery):
        try:
            with open("abilities/skye/skye1.mp4", 'rb') as skye:
                await bot.send_video(chat_id=callback.from_user.id, video=skye)
            ab = Skye().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_skye)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='skye_c')
    async def ab_skye_c(callback: types.CallbackQuery):
        try:
            with open("abilities/skye/skye3.mp4", 'rb') as skye:
                await bot.send_video(chat_id=callback.from_user.id, video=skye)
            ab = Skye().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_skye)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='skye_x')
    async def ab_skye_x(callback: types.CallbackQuery):
        try:
            with open("abilities/skye/skye4.mp4", 'rb') as skye:
                await bot.send_video(chat_id=callback.from_user.id, video=skye)
            ab = Skye().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_skye)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🤖 KAY/O'])
async def kayo(message: types.Message):
    photo = types.InputFile('agents_images/kayo.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_kayo)

    @dp.callback_query_handler(text='bio_kayo')
    async def bio_kayo(callback: types.CallbackQuery):
        Kayo_bio = Kayo().bio()
        await callback.message.answer(Kayo_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_kayo')
    async def ab_kayo(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_kayo)
        await callback.answer()

    @dp.callback_query_handler(text='kayo_q')
    async def ab_kayo_q(callback: types.CallbackQuery):
        try:
            with open("abilities/kayo/kayo2.mp4", 'rb') as kayo:
                await bot.send_video(chat_id=callback.from_user.id, video=kayo)
            ab = Kayo().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_kayo)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='kayo_e')
    async def ab_kayo_e(callback: types.CallbackQuery):
        try:
            with open("abilities/kayo/kayo1.mp4", 'rb') as kayo:
                await bot.send_video(chat_id=callback.from_user.id, video=kayo)
            ab = Kayo().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_kayo)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='kayo_c')
    async def ab_kayo_c(callback: types.CallbackQuery):
        try:
            with open("abilities/kayo/kayo3.mp4", 'rb') as kayo:
                await bot.send_video(chat_id=callback.from_user.id, video=kayo)
            ab = Kayo().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_kayo)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='kayo_x')
    async def ab_kayo_x(callback: types.CallbackQuery):
        try:
            with open("abilities/kayo/kayo4.mp4", 'rb') as kayo:
                await bot.send_video(chat_id=callback.from_user.id, video=kayo)
            ab = Kayo().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_kayo)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🧿 FADE'])
async def fade(message: types.Message):
    photo = types.InputFile('agents_images/fade.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_fade)

    @dp.callback_query_handler(text='bio_fade')
    async def bio_fade(callback: types.CallbackQuery):
        Fade_bio = Fade().bio()
        await callback.message.answer(Fade_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_fade')
    async def ab_fade(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_fade)
        await callback.answer()

    @dp.callback_query_handler(text='fade_q')
    async def ab_fade_q(callback: types.CallbackQuery):
        try:
            with open("abilities/fade/fade3.mp4", 'rb') as fade:
                await bot.send_video(chat_id=callback.from_user.id, video=fade)
            ab = Fade().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_fade)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='fade_e')
    async def ab_fade_e(callback: types.CallbackQuery):
        try:
            with open("abilities/fade/fade1.mp4", 'rb') as fade:
                await bot.send_video(chat_id=callback.from_user.id, video=fade)
            ab = Fade().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_fade)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='fade_c')
    async def ab_fade_c(callback: types.CallbackQuery):
        try:
            with open("abilities/fade/fade2.mp4", 'rb') as fade:
                await bot.send_video(chat_id=callback.from_user.id, video=fade)
            ab = Fade().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_fade)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='fade_x')
    async def ab_fade_x(callback: types.CallbackQuery):
        try:
            with open("abilities/fade/fade4.mp4", 'rb') as fade:
                await bot.send_video(chat_id=callback.from_user.id, video=fade)
            ab = Fade().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_fade)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🐾 GEKKO'])
async def gekko(message: types.Message):
    photo = types.InputFile('agents_images/gekko.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_gekko)

    @dp.callback_query_handler(text='bio_gekko')
    async def bio_gekko(callback: types.CallbackQuery):
        Gekko_bio = Gekko().bio()
        await callback.message.answer(Gekko_bio, parse_mode='html')
        await callback.answer()

    @dp.callback_query_handler(text='abilities_gekko')
    async def ab_gekko(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_gekko)
        await callback.answer()

    @dp.callback_query_handler(text='gekko_q')
    async def ab_gekko_q(callback: types.CallbackQuery):
        try:
            with open("abilities/gekko/gekko2.mp4", 'rb') as gekko:
                await bot.send_video(chat_id=callback.from_user.id, video=gekko)
            ab = Gekko().abilities()
            await callback.message.answer(ab['q'], reply_markup=abilities_gekko)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='gekko_e')
    async def ab_gekko_e(callback: types.CallbackQuery):
        try:
            with open("abilities/gekko/gekko1.mp4", 'rb') as gekko:
                await bot.send_video(chat_id=callback.from_user.id, video=gekko)
            ab = Gekko().abilities()
            await callback.message.answer(ab['e'], reply_markup=abilities_gekko)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='gekko_c')
    async def ab_gekko_c(callback: types.CallbackQuery):
        try:
            with open("abilities/gekko/gekko3.mp4", 'rb') as gekko:
                await bot.send_video(chat_id=callback.from_user.id, video=gekko)
            ab = Gekko().abilities()
            await callback.message.answer(ab['c'], reply_markup=abilities_gekko)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')

    @dp.callback_query_handler(text='gekko_x')
    async def ab_gekko_x(callback: types.CallbackQuery):
        try:
            with open("abilities/gekko/gekko4.mp4", 'rb') as gekko:
                await bot.send_video(chat_id=callback.from_user.id, video=gekko)
            ab = Gekko().abilities()
            await callback.message.answer(ab['x'], reply_markup=abilities_gekko)
            await callback.answer()
        except InvalidQueryID:
            await callback.message.answer(text=f"❗Потрібне краще підключення до інтернету❗", parse_mode='html')


@dp.message_handler(text=['🗺 Карти'])
async def list_maps(messsage: types.Message):
    await messsage.answer("Оберіть карту:", reply_markup=maps)


@dp.message_handler(text=['🟢 LOTUS'])
async def lotus(messsage: types.Message):
    photo = Lotus().photos()
    text = Lotus().inf()
    await bot.send_media_group(chat_id=messsage.from_user.id, media=photo[:])
    await bot.send_message(chat_id=messsage.from_user.id, text=text)


@dp.message_handler(text=['🔵 PEARL'])
async def pearl(messsage: types.Message):
    photo = Pearl().photos()
    text = Pearl().inf()
    await bot.send_media_group(chat_id=messsage.from_user.id, media=photo[:])
    await bot.send_message(chat_id=messsage.from_user.id, text=text)


@dp.message_handler(text=['🟠 FRACTURE'])
async def fracture(messsage: types.Message):
    photo = Fracture().photos()
    text = Fracture().inf()
    await bot.send_media_group(chat_id=messsage.from_user.id, media=photo[:])
    await bot.send_message(chat_id=messsage.from_user.id, text=text)


@dp.message_handler(text=['⚪ ICEBOX'])
async def icebox(messsage: types.Message):
    photo = Icebox().photos()
    text = Icebox().inf()
    await bot.send_media_group(chat_id=messsage.from_user.id, media=photo[:])
    await bot.send_message(chat_id=messsage.from_user.id, text=text)


@dp.message_handler(text=['🟢 BREEZE'])
async def breeze(messsage: types.Message):
    photo = Breeze().photos()
    text = Breeze().inf()
    await bot.send_media_group(chat_id=messsage.from_user.id, media=photo[:])
    await bot.send_message(chat_id=messsage.from_user.id, text=text)


@dp.message_handler(text=['🟡 BIND'])
async def bind(messsage: types.Message):
    photo = Bind().photos()
    text = Bind().inf()
    await bot.send_media_group(chat_id=messsage.from_user.id, media=photo[:])
    await bot.send_message(chat_id=messsage.from_user.id, text=text)


@dp.message_handler(text=['🟤 SPLIT'])
async def split(messsage: types.Message):
    photo = Split().photos()
    text = Split().inf()
    await bot.send_media_group(chat_id=messsage.from_user.id, media=photo[:])
    await bot.send_message(chat_id=messsage.from_user.id, text=text)


@dp.message_handler(text=['🟠 ASCENT'])
async def ascent(messsage: types.Message):
    photo = Ascent().photos()
    text = Ascent().inf()
    await bot.send_media_group(chat_id=messsage.from_user.id, media=photo[:])
    await bot.send_message(chat_id=messsage.from_user.id, text=text)


@dp.message_handler(text=['🟢 HAVEN'])
async def haven(messsage: types.Message):
    photo = Haven().photos()
    text = Haven().inf()
    await bot.send_media_group(chat_id=messsage.from_user.id, media=photo[:])
    await bot.send_message(chat_id=messsage.from_user.id, text=text)


@dp.message_handler(text=['🔫 Зброя'])
async def list_maps(message: types.Message):
    await message.answer("Оберіть клас зброї:", reply_markup=weapons)


@dp.message_handler(text=['Пістолети'])
async def ascent(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Оберіть зброю:", reply_markup=sidearms)


@dp.message_handler(text=['CLASSIC'])
async def ascent(message: types.Message):
    photo = Classic().photo()
    text = Classic().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['SHORTY'])
async def ascent(message: types.Message):
    photo = Shorty().photo()
    text = Shorty().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['FRENZY'])
async def ascent(message: types.Message):
    photo = Frenzy().photo()
    text = Frenzy().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['GHOST'])
async def ascent(message: types.Message):
    photo = Ghost().photo()
    text = Ghost().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['SHERIFF'])
async def ascent(message: types.Message):
    photo = Sheriff().photo()
    text = Sheriff().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['Пістолети-кулемети'])
async def ascent(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Оберіть зброю:", reply_markup=smgs)


@dp.message_handler(text=['STINGER'])
async def ascent(message: types.Message):
    photo = Stinger().photo()
    text = Stinger().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['SPECTRE'])
async def ascent(message: types.Message):
    photo = Spectre().photo()
    text = Spectre().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['Снайперські гвинтівки'])
async def ascent(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Оберіть зброю:", reply_markup=snipers)


@dp.message_handler(text=['MARSHAL'])
async def ascent(message: types.Message):
    photo = Marshal().photo()
    text = Marshal().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['OPERATOR'])
async def ascent(message: types.Message):
    photo = Operator().photo()
    text = Operator().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['Важка зброя'])
async def ascent(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Оберіть зброю:", reply_markup=heavies)


@dp.message_handler(text=['ARES'])
async def ascent(message: types.Message):
    photo = Ares().photo()
    text = Ares().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['ODIN'])
async def ascent(message: types.Message):
    photo = Odin().photo()
    text = Odin().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['Дробовики'])
async def ascent(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Оберіть зброю:", reply_markup=shotguns)


@dp.message_handler(text=['BUCKY'])
async def ascent(message: types.Message):
    photo = Bucky().photo()
    text = Bucky().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['JUDGE'])
async def ascent(message: types.Message):
    photo = Judge().photo()
    text = Judge().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['Гвинтівки'])
async def ascent(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Оберіть зброю:", reply_markup=rifles)


@dp.message_handler(text=['BULLDOG'])
async def ascent(message: types.Message):
    photo = Bulldog().photo()
    text = Bulldog().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['GUARDIAN'])
async def ascent(message: types.Message):
    photo = Guardian().photo()
    text = Guardian().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['PHANTOM'])
async def ascent(message: types.Message):
    photo = Phantom().photo()
    text = Phantom().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['VANDAL'])
async def ascent(message: types.Message):
    photo = Vandal().photo()
    text = Vandal().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


@dp.message_handler(text=['Холодна зброя'])
async def ascent(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Оберіть зброю:", reply_markup=melee)


@dp.message_handler(text=['Тактичний ніж'])
async def ascent(message: types.Message):
    photo = Knife().photo()
    text = Knife().inf()
    await bot.send_media_group(chat_id=message.from_user.id, media=photo[:])
    await bot.send_message(chat_id=message.from_user.id, text=text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)