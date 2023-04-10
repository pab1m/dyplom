import os
import requests
from aiogram.dispatcher.filters import Text
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InputMediaPhoto
from btn import *
from all_inf import *

TOKEN = "6275163921:AAFvgDqIWHw7Lk0YnaZPBVW2rHJEjrKu_FA"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Привіт, <b>{message.from_user.first_name if message.from_user.last_name is None else message.from_user.first_name + ' ' + message.from_user.last_name}</b>, "
                           f"я телеграм бот який допоможе тобі познайомитися із грою VALORANT та дізнатися "
                           "інформацію про свій прогрес", parse_mode='html')
    # await message.delete()
    await bot.send_message(message.from_user.id, "Введіть /help щоб дізнатися мій функціонал")


@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    await bot.send_message(message.from_user.id, "Доступні команди:", reply_markup=kb_help)
    # await message.delete()


@dp.message_handler(lambda message: "Для новачків" in message.text)
async def new_people(messsage: types.Message):
    await messsage.answer("Для новачків:", reply_markup=new_player)


@dp.message_handler(lambda message: 'Агенти' in message.text)
async def new_people(message: types.Message):
    # await bot.delete_message(message.chat.id, message.message_id - 1)
    # await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    # await bot.delete_message(message.chat.id, message.message_id)

    delete = await message.answer('Агенти:', reply_markup=agents)
    # await delete.delete()
    # await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(lambda message: "СПЕЦІАЛІСТ (CONTROLLER)" in message.text)
async def controllers(messsage: types.Message):
    await bot.send_message(messsage.from_user.id, 'КОНТРОЛЕР (CONTROLLER)', reply_markup=controller)


@dp.message_handler(text=['BRIMSTONE'])
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
        with open("abilities/brimstone/brim3.mp4", 'rb') as brim:
            await bot.send_video(chat_id=callback.from_user.id, video=brim)
        ab = Brim().abilities()
        await callback.message.answer(ab['q'], reply_markup=abilities_brim)
        await callback.answer()

    @dp.callback_query_handler(text='brim_e')
    async def ab_brim_e(callback: types.CallbackQuery):
        with open("abilities/brimstone/brim1.mp4", 'rb') as brim:
            await bot.send_video(chat_id=callback.from_user.id, video=brim)
        ab = Brim().abilities()
        await callback.message.answer(ab['e'], reply_markup=abilities_brim)
        await callback.answer()

    @dp.callback_query_handler(text='brim_c')
    async def ab_brim_c(callback: types.CallbackQuery):
        with open("abilities/brimstone/brim2.mp4", 'rb') as brim:
            await bot.send_video(chat_id=callback.from_user.id, video=brim)
        ab = Brim().abilities()
        await callback.message.answer(ab['c'], reply_markup=abilities_brim)
        await callback.answer()

    @dp.callback_query_handler(text='brim_x')
    async def ab_brim_x(callback: types.CallbackQuery):
        with open("abilities/brimstone/brim4.mp4", 'rb') as brim:
            await bot.send_video(chat_id=callback.from_user.id, video=brim)
        ab = Brim().abilities()
        await callback.message.answer(ab['x'], reply_markup=abilities_brim)
        await callback.answer()


@dp.message_handler(text=['VIPER'])
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
        with open("abilities/viper/viper2.mp4", 'rb') as viper:
            await bot.send_video(chat_id=callback.from_user.id, video=viper)
        ab = Viper().abilities()
        await callback.message.answer(ab['q'], reply_markup=abilities_viper)
        await callback.answer()

    @dp.callback_query_handler(text='viper_e')
    async def ab_viper_e(callback: types.CallbackQuery):
        with open("abilities/viper/viper1.mp4", 'rb') as viper:
            await bot.send_video(chat_id=callback.from_user.id, video=viper)
        ab = Viper().abilities()
        await callback.message.answer(ab['e'], reply_markup=abilities_viper)
        await callback.answer()

    @dp.callback_query_handler(text='viper_c')
    async def ab_viper_c(callback: types.CallbackQuery):
        with open("abilities/viper/viper3.mp4", 'rb') as viper:
            await bot.send_video(chat_id=callback.from_user.id, video=viper)
        ab = Viper().abilities()
        await callback.message.answer(ab['c'], reply_markup=abilities_viper)
        await callback.answer()

    @dp.callback_query_handler(text='viper_x')
    async def ab_viper_x(callback: types.CallbackQuery):
        with open("abilities/viper/viper4.mp4", 'rb') as viper:
            await bot.send_video(chat_id=callback.from_user.id, video=viper)
        ab = Viper().abilities()
        await callback.message.answer(ab['x'], reply_markup=abilities_viper)
        await callback.answer()


@dp.message_handler(text=['OMEN'])
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
        with open("abilities/omen/omen2.mp4", 'rb') as omen:
            await bot.send_video(chat_id=callback.from_user.id, video=omen)
        ab = Omen().abilities()
        await callback.message.answer(ab['q'], reply_markup=abilities_omen)
        await callback.answer()

    @dp.callback_query_handler(text='omen_e')
    async def ab_omen_e(callback: types.CallbackQuery):
        with open("abilities/omen/omen1.mp4", 'rb') as omen:
            await bot.send_video(chat_id=callback.from_user.id, video=omen)
        ab = Omen().abilities()
        await callback.message.answer(ab['e'], reply_markup=abilities_omen)
        await callback.answer()

    @dp.callback_query_handler(text='omen_c')
    async def ab_omen_c(callback: types.CallbackQuery):
        with open("abilities/omen/omen3.mp4", 'rb') as omen:
            await bot.send_video(chat_id=callback.from_user.id, video=omen)
        ab = Omen().abilities()
        await callback.message.answer(ab['c'], reply_markup=abilities_omen)
        await callback.answer()

    @dp.callback_query_handler(text='omen_x')
    async def ab_omen_x(callback: types.CallbackQuery):
        with open("abilities/omen/omen4.mp4", 'rb') as omen:
            await bot.send_video(chat_id=callback.from_user.id, video=omen)
        ab = Omen().abilities()
        await callback.message.answer(ab['x'], reply_markup=abilities_omen)
        await callback.answer()


@dp.message_handler(text=['ASTRA'])
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
        with open("abilities/astra/astra3.mp4", 'rb') as astra:
            await bot.send_video(chat_id=callback.from_user.id, video=astra)
        ab = Astra().abilities()
        await callback.message.answer(ab['q'], reply_markup=abilities_astra)
        await callback.answer()


    @dp.callback_query_handler(text='astra_e')
    async def ab_astra_e(callback: types.CallbackQuery):
        with open("abilities/astra/astra2.mp4", 'rb') as astra:
            await bot.send_video(chat_id=callback.from_user.id, video=astra)
        ab = Astra().abilities()
        await callback.message.answer(ab['e'], reply_markup=abilities_astra)
        await callback.answer()


    @dp.callback_query_handler(text='astra_c')
    async def ab_astra_c(callback: types.CallbackQuery):
        with open("abilities/astra/astra1.mp4", 'rb') as astra:
            await bot.send_video(chat_id=callback.from_user.id, video=astra)
        ab = Astra().abilities()
        await callback.message.answer(ab['c'], reply_markup=abilities_astra)
        await callback.answer()


    @dp.callback_query_handler(text='astra_x')
    async def ab_astra_x(callback: types.CallbackQuery):
        with open("abilities/astra/astra4.mp4", 'rb') as astra:
            await bot.send_video(chat_id=callback.from_user.id, video=astra)
        ab = Astra().abilities()
        await callback.message.answer(ab['x'], reply_markup=abilities_astra)
        await callback.answer()


@dp.message_handler(text=['HARBOR'])
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
        with open("abilities/harbor/harbor2.mp4", 'rb') as harbor:
            await bot.send_video(chat_id=callback.from_user.id, video=harbor)
        ab = Harbor().abilities()
        await callback.message.answer(ab['q'], reply_markup=abilities_harbor)
        await callback.answer()

    @dp.callback_query_handler(text='harbor_e')
    async def ab_harbor_e(callback: types.CallbackQuery):
        with open("abilities/harbor/harbor1.mp4", 'rb') as harbor:
            await bot.send_video(chat_id=callback.from_user.id, video=harbor)
        ab = Harbor().abilities()
        await callback.message.answer(ab['e'], reply_markup=abilities_harbor)
        await callback.answer()

    @dp.callback_query_handler(text='harbor_c')
    async def ab_harbor_c(callback: types.CallbackQuery):
        with open("abilities/harbor/harbor3.mp4", 'rb') as harbor:
            await bot.send_video(chat_id=callback.from_user.id, video=harbor)
        ab = Harbor().abilities()
        await callback.message.answer(ab['c'], reply_markup=abilities_harbor)
        await callback.answer()

    @dp.callback_query_handler(text='harbor_x')
    async def ab_harbor_x(callback: types.CallbackQuery):
        with open("abilities/harbor/harbor4.mp4", 'rb') as harbor:
            await bot.send_video(chat_id=callback.from_user.id, video=harbor)
        ab = Harbor().abilities()
        await callback.message.answer(ab['x'], reply_markup=abilities_harbor)
        await callback.answer()


@dp.message_handler(lambda message: "ДУЕЛЯНТ (DUELIST)" in message.text)
async def duelists(messsage: types.Message):
    await bot.send_message(messsage.from_user.id, "ДУЕЛЯНТ (DUELIST)", reply_markup=duelist)


@dp.message_handler(text=['PHOENIX'])
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
        with open("abilities/phoenix/phoenix2.mp4", 'rb') as phoenix:
            await bot.send_video(chat_id=callback.from_user.id, video=phoenix)
        ab = Phoenix().abilities()
        await callback.message.answer(ab['q'], reply_markup=abilities_phoenix)
        await callback.answer()

    @dp.callback_query_handler(text='phoenix_e')
    async def ab_phoenix_e(callback: types.CallbackQuery):
        with open("abilities/phoenix/phoenix1.mp4", 'rb') as phoenix:
            await bot.send_video(chat_id=callback.from_user.id, video=phoenix)
        with open("abilities/phoenix/phoenix1.1.mp4", 'rb') as phoenix:
            await bot.send_video(chat_id=callback.from_user.id, video=phoenix)
        ab = Phoenix().abilities()
        await callback.message.answer(ab['e'], reply_markup=abilities_phoenix)
        await callback.answer()

    @dp.callback_query_handler(text='phoenix_c')
    async def ab_phoenix_c(callback: types.CallbackQuery):
        with open("abilities/phoenix/phoenix3.mp4", 'rb') as phoenix:
            await bot.send_video(chat_id=callback.from_user.id, video=phoenix)
        ab = Phoenix().abilities()
        await callback.message.answer(ab['c'], reply_markup=abilities_phoenix)
        await callback.answer()

    @dp.callback_query_handler(text='phoenix_x')
    async def ab_phoenix_x(callback: types.CallbackQuery):
        with open("abilities/phoenix/phoenix4.mp4", 'rb') as phoenix:
            await bot.send_video(chat_id=callback.from_user.id, video=phoenix)
        ab = Phoenix().abilities()
        await callback.message.answer(ab['x'], reply_markup=abilities_phoenix)
        await callback.answer()


@dp.message_handler(text=['REYNA'])
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
        with open("abilities/reyna/reyna2.mp4", 'rb') as reyna:
            await bot.send_video(chat_id=callback.from_user.id, video=reyna)
        ab = Reyna().abilities()
        await callback.message.answer(ab['q'], reply_markup=abilities_reyna)
        await callback.answer()

    @dp.callback_query_handler(text='reyna_e')
    async def ab_reyna_e(callback: types.CallbackQuery):
        with open("abilities/reyna/reyna3.mp4", 'rb') as reyna:
            await bot.send_video(chat_id=callback.from_user.id, video=reyna)
        ab = Reyna().abilities()
        await callback.message.answer(ab['e'], reply_markup=abilities_reyna)
        await callback.answer()

    @dp.callback_query_handler(text='reyna_c')
    async def ab_reyna_c(callback: types.CallbackQuery):
        with open("abilities/reyna/reyna1.mp4", 'rb') as reyna:
            await bot.send_video(chat_id=callback.from_user.id, video=reyna)
        ab = Reyna().abilities()
        await callback.message.answer(ab['c'], reply_markup=abilities_reyna)
        await callback.answer()

    @dp.callback_query_handler(text='reyna_x')
    async def ab_reyna_x(callback: types.CallbackQuery):
        with open("abilities/reyna/reyna4.mp4", 'rb') as reyna:
            await bot.send_video(chat_id=callback.from_user.id, video=reyna)
        ab = Reyna().abilities()
        await callback.message.answer(ab['x'], reply_markup=abilities_reyna)
        await callback.answer()


@dp.message_handler(text=['JETT'])
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
        with open("abilities/jett/jett2.mp4", 'rb') as jett:
            await bot.send_video(chat_id=callback.from_user.id, video=jett)
        ab = Jett().abilities()
        await callback.message.answer(ab['q'], reply_markup=abilities_jett)
        await callback.answer()

    @dp.callback_query_handler(text='jett_e')
    async def ab_jett_e(callback: types.CallbackQuery):
        with open("abilities/jett/jett1.mp4", 'rb') as jett:
            await bot.send_video(chat_id=callback.from_user.id, video=jett)
        ab = Jett().abilities()
        await callback.message.answer(ab['e'], reply_markup=abilities_jett)
        await callback.answer()

    @dp.callback_query_handler(text='jett_c')
    async def ab_jett_c(callback: types.CallbackQuery):
        with open("abilities/jett/jett3.mp4", 'rb') as jett:
            await bot.send_video(chat_id=callback.from_user.id, video=jett)
        ab = Jett().abilities()
        await callback.message.answer(ab['c'], reply_markup=abilities_jett)
        await callback.answer()

    @dp.callback_query_handler(text='jett_x')
    async def ab_jett_x(callback: types.CallbackQuery):
        with open("abilities/jett/jett4.mp4", 'rb') as jett:
            await bot.send_video(chat_id=callback.from_user.id, video=jett)
        ab = Jett().abilities()
        await callback.message.answer(ab['x'], reply_markup=abilities_jett)
        await callback.answer()


@dp.message_handler(text=['RAZE'])
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
        with open("abilities/raze/raze2.mp4", 'rb') as raze:
            await bot.send_video(chat_id=callback.from_user.id, video=raze)
        ab = Raze().abilities()
        await callback.message.answer(ab['q'], reply_markup=abilities_raze)
        await callback.answer()

    @dp.callback_query_handler(text='raze_e')
    async def ab_raze_e(callback: types.CallbackQuery):
        with open("abilities/raze/raze1.mp4", 'rb') as raze:
            await bot.send_video(chat_id=callback.from_user.id, video=raze)
        ab = Raze().abilities()
        await callback.message.answer(ab['e'], reply_markup=abilities_raze)
        await callback.answer()

    @dp.callback_query_handler(text='raze_c')
    async def ab_raze_c(callback: types.CallbackQuery):
        with open("abilities/raze/raze3.mp4", 'rb') as raze:
            await bot.send_video(chat_id=callback.from_user.id, video=raze)
        ab = Raze().abilities()
        await callback.message.answer(ab['c'], reply_markup=abilities_raze)
        await callback.answer()

    @dp.callback_query_handler(text='raze_x')
    async def ab_raze_x(callback: types.CallbackQuery):
        with open("abilities/raze/raze4.mp4", 'rb') as raze:
            await bot.send_video(chat_id=callback.from_user.id, video=raze)
        ab = Raze().abilities()
        await callback.message.answer(ab['x'], reply_markup=abilities_raze)
        await callback.answer()


@dp.message_handler(text=['YORU'])
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
        with open("abilities/yoru/yoru3.mp4", 'rb') as yoru:
            await bot.send_video(chat_id=callback.from_user.id, video=yoru)
        ab = Yoru().abilities()
        await callback.message.answer(ab['q'], reply_markup=abilities_yoru)
        await callback.answer()

    @dp.callback_query_handler(text='yoru_e')
    async def ab_yoru_e(callback: types.CallbackQuery):
        with open("abilities/yoru/yoru1.mp4", 'rb') as yoru:
            await bot.send_video(chat_id=callback.from_user.id, video=yoru)
        with open("abilities/yoru/yoru1.1.mp4", 'rb') as yoru:
            await bot.send_video(chat_id=callback.from_user.id, video=yoru)
        ab = Yoru().abilities()
        await callback.message.answer(ab['e'], reply_markup=abilities_yoru)
        await callback.answer()

    @dp.callback_query_handler(text='yoru_c')
    async def ab_yoru_c(callback: types.CallbackQuery):
        with open("abilities/yoru/yoru2.mp4", 'rb') as yoru:
            await bot.send_video(chat_id=callback.from_user.id, video=yoru)
        ab = Yoru().abilities()
        await callback.message.answer(ab['c'], reply_markup=abilities_yoru)
        await callback.answer()

    @dp.callback_query_handler(text='yoru_x')
    async def ab_yoru_x(callback: types.CallbackQuery):
        with open("abilities/yoru/yoru4.mp4", 'rb') as yoru:
            await bot.send_video(chat_id=callback.from_user.id, video=yoru)
        ab = Yoru().abilities()
        await callback.message.answer(ab['x'], reply_markup=abilities_yoru)
        await callback.answer()


@dp.message_handler(text=['NEON'])
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
        with open("abilities/neon/neon2.mp4", 'rb') as neon:
            await bot.send_video(chat_id=callback.from_user.id, video=neon)
        ab = Neon().abilities()
        await callback.message.answer(ab['q'], reply_markup=abilities_neon)
        await callback.answer()

    @dp.callback_query_handler(text='neon_e')
    async def ab_neon_e(callback: types.CallbackQuery):
        with open("abilities/neon/neon1.mp4", 'rb') as neon:
            await bot.send_video(chat_id=callback.from_user.id, video=neon)
        ab = Neon().abilities()
        await callback.message.answer(ab['e'], reply_markup=abilities_neon)
        await callback.answer()

    @dp.callback_query_handler(text='neon_c')
    async def ab_neon_c(callback: types.CallbackQuery):
        with open("abilities/neon/neon3.mp4", 'rb') as neon:
            await bot.send_video(chat_id=callback.from_user.id, video=neon)
        ab = Neon().abilities()
        await callback.message.answer(ab['c'], reply_markup=abilities_neon)
        await callback.answer()

    @dp.callback_query_handler(text='neon_x')
    async def ab_neon_x(callback: types.CallbackQuery):
        with open("abilities/neon/neon4.mp4", 'rb') as neon:
            await bot.send_video(chat_id=callback.from_user.id, video=neon)
        ab = Neon().abilities()
        await callback.message.answer(ab['x'], reply_markup=abilities_neon)
        await callback.answer()


@dp.message_handler(lambda message: "ВАРТОВИЙ/СТРАЖ (SENTINEL)" in message.text)
async def sentinels(messsage: types.Message):
    await bot.send_message(messsage.from_user.id, "ВАРТОВИЙ/СТРАЖ (SENTINEL)", reply_markup=sentinel)



executor.start_polling(dp, skip_updates=True)
