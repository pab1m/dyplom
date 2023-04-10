import os
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
                           f"Привіт, <b>{message.from_user.first_name if message.from_user.last_name is None else message.from_user.first_name + ' ' + message.from_user.last_name}</b>, я телеграм бот який допоможе тобі познайомитися із грою VALORANT та дізнатися "
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
async def new_people(messsage: types.Message):
    await bot.send_message(messsage.from_user.id, 'СПЕЦІАЛІСТ (CONTROLLER)', reply_markup=controller)
    # await messsage.answer('КОНТРОЛЕР (CONTROLLER)', reply_markup=controller)


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
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)
        ab = Brim().abilities()
        await callback.message.answer(ab['q'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()

    @dp.callback_query_handler(text='brim_e')
    async def ab_brim_e(callback: types.CallbackQuery):
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)
        ab = Brim().abilities()
        await callback.message.answer(ab['e'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()

    @dp.callback_query_handler(text='brim_c')
    async def ab_brim_c(callback: types.CallbackQuery):
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)
        ab = Brim().abilities()
        await callback.message.answer(ab['c'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()

    @dp.callback_query_handler(text='brim_x')
    async def ab_brim_x(callback: types.CallbackQuery):
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)
        ab = Brim().abilities()
        await callback.message.answer(ab['x'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
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
        with open("agents_images/viper.png", 'rb') as viper:
            await bot.send_photo(chat_id=callback.from_user.id, photo=viper)
        ab = Viper().abilities()
        await callback.message.answer(ab['q'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_viper)
        await callback.answer()


    @dp.callback_query_handler(text='viper_e')
    async def ab_viper_e(callback: types.CallbackQuery):
        with open("agents_images/viper.png", 'rb') as viper:
            await bot.send_photo(chat_id=callback.from_user.id, photo=viper)
        ab = Viper().abilities()
        await callback.message.answer(ab['e'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_viper)
        await callback.answer()


    @dp.callback_query_handler(text='viper_c')
    async def ab_viper_c(callback: types.CallbackQuery):
        with open("agents_images/viper.png", 'rb') as viper:
            await bot.send_photo(chat_id=callback.from_user.id, photo=viper)
        ab = Viper().abilities()
        await callback.message.answer(ab['c'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_viper)
        await callback.answer()


    @dp.callback_query_handler(text='viper_x')
    async def ab_viper_x(callback: types.CallbackQuery):
        with open("agents_images/viper.png", 'rb') as viper:
            await bot.send_photo(chat_id=callback.from_user.id, photo=viper)
        ab = Viper().abilities()
        await callback.message.answer(ab['x'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_viper)
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
        with open("agents_images/omen.png", 'rb') as omen:
            await bot.send_photo(chat_id=callback.from_user.id, photo=omen)
        ab = Omen().abilities()
        await callback.message.answer(ab['q'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_omen)
        await callback.answer()


    @dp.callback_query_handler(text='omen_e')
    async def ab_omen_e(callback: types.CallbackQuery):
        with open("agents_images/omen.png", 'rb') as omen:
            await bot.send_photo(chat_id=callback.from_user.id, photo=omen)
        ab = Omen().abilities()
        await callback.message.answer(ab['e'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_omen)
        await callback.answer()


    @dp.callback_query_handler(text='omen_c')
    async def ab_omen_c(callback: types.CallbackQuery):
        with open("agents_images/omen.png", 'rb') as omen:
            await bot.send_photo(chat_id=callback.from_user.id, photo=omen)
        ab = Omen().abilities()
        await callback.message.answer(ab['c'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_omen)
        await callback.answer()


    @dp.callback_query_handler(text='omen_x')
    async def ab_omen_x(callback: types.CallbackQuery):
        with open("agents_images/omen.png", 'rb') as omen:
            await bot.send_photo(chat_id=callback.from_user.id, photo=omen)
        ab = Omen().abilities()
        await callback.message.answer(ab['x'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_omen)
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
        with open("agents_images/astra.png", 'rb') as astra:
            await bot.send_photo(chat_id=callback.from_user.id, photo=astra)
        ab = Astra().abilities()
        await callback.message.answer(ab['q'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_astra)
        await callback.answer()


    @dp.callback_query_handler(text='astra_e')
    async def ab_astra_e(callback: types.CallbackQuery):
        with open("agents_images/astra.png", 'rb') as astra:
            await bot.send_photo(chat_id=callback.from_user.id, photo=astra)
        ab = Astra().abilities()
        await callback.message.answer(ab['e'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_astra)
        await callback.answer()


    @dp.callback_query_handler(text='astra_c')
    async def ab_astra_c(callback: types.CallbackQuery):
        with open("agents_images/astra.png", 'rb') as astra:
            await bot.send_photo(chat_id=callback.from_user.id, photo=astra)
        ab = Astra().abilities()
        await callback.message.answer(ab['c'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_astra)
        await callback.answer()


    @dp.callback_query_handler(text='astra_x')
    async def ab_astra_x(callback: types.CallbackQuery):
        with open("agents_images/astra.png", 'rb') as astra:
            await bot.send_photo(chat_id=callback.from_user.id, photo=astra)
        ab = Astra().abilities()
        await callback.message.answer(ab['x'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_astra)
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
        with open("agents_images/harbor.png", 'rb') as harbor:
            await bot.send_photo(chat_id=callback.from_user.id, photo=harbor)
        ab = Harbor().abilities()
        await callback.message.answer(ab['q'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_harbor)
        await callback.answer()

    @dp.callback_query_handler(text='harbor_e')
    async def ab_harbor_e(callback: types.CallbackQuery):
        with open("agents_images/harbor.png", 'rb') as harbor:
            await bot.send_photo(chat_id=callback.from_user.id, photo=harbor)
        ab = Harbor().abilities()
        await callback.message.answer(ab['e'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_harbor)
        await callback.answer()

    @dp.callback_query_handler(text='harbor_c')
    async def ab_harbor_c(callback: types.CallbackQuery):
        with open("agents_images/harbor.png", 'rb') as harbor:
            await bot.send_photo(chat_id=callback.from_user.id, photo=harbor)
        ab = Harbor().abilities()
        await callback.message.answer(ab['c'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_harbor)
        await callback.answer()

    @dp.callback_query_handler(text='harbor_x')
    async def ab_harbor_x(callback: types.CallbackQuery):
        with open("agents_images/harbor.png", 'rb') as harbor:
            await bot.send_photo(chat_id=callback.from_user.id, photo=harbor)
        ab = Harbor().abilities()
        await callback.message.answer(ab['x'])
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_harbor)
        await callback.answer()


@dp.message_handler(lambda message: "ДУЕЛЯНТ (DUELIST)" in message.text)
async def new_people(messsage: types.Message):
    await bot.send_message(messsage.from_user.id, "ДУЕЛЯНТ (DUELIST)", reply_markup=duelist)
    # await messsage.answer('КОНТРОЛЕР (CONTROLLER)', reply_markup=controller)






executor.start_polling(dp, skip_updates=True)
