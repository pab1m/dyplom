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
    await bot.delete_message(message.chat.id, message.message_id - 1)
    # await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.delete_message(message.chat.id, message.message_id)

    await message.answer('Агенти:', reply_markup=agents)




@dp.message_handler(lambda message: "КОНТРОЛЕР (CONTROLLER)" in message.text)
async def new_people(messsage: types.Message):
    await bot.send_message(messsage.from_user.id, 'КОНТРОЛЕР (CONTROLLER)', reply_markup=controller)
    # await messsage.answer('КОНТРОЛЕР (CONTROLLER)', reply_markup=controller)


# @dp.message_handler(lambda message: "BRIMSTONE" in message.text)

# @dp.callback_query_handler(text='BRIMSTONE')
# async def new_people(call: types.CallbackQuery):
#     photo = types.InputFile('brimstone.png')
#     # await bot.send_photo(chat_id=messsage.from_user.id, photo=photo)
#
#     await call.answer('good')
#
#     # await bot.send_message(messsage.from_user.id, 'КОНТРОЛЕР (CONTROLLER)', reply_markup=controller)
#     # await call.answer(call.from_user.id, reply_markup=btn_info_brim)
#     await call.answer('test0', reply_markup=tt())


@dp.message_handler(text=['BRIMSTONE'])
async def test(message: types.Message):
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
    async def bio_brim(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()


    @dp.callback_query_handler(text='brim_q')
    async def bio_brim(callback: types.CallbackQuery):
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)

        await callback.message.answer(text='опис абілки')
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()


    @dp.callback_query_handler(text='brim_e')
    async def bio_brim(callback: types.CallbackQuery):
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)

        await callback.message.answer(text='опис aбілки')
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()


    @dp.callback_query_handler(text='brim_c')
    async def bio_brim(callback: types.CallbackQuery):
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)

        await callback.message.answer(text='опис aбілки')
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()


    @dp.callback_query_handler(text='brim_x')
    async def bio_brim(callback: types.CallbackQuery):
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)

        await callback.message.answer(text='опис ульти')
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()


@dp.message_handler(text=['VIPER'])
async def test(message: types.Message):
    photo = types.InputFile('agents_images/viper.png.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    photo.clean()
    await message.answer('Оберіть категорію для ознайомлення:', reply_markup=info_brim)

    @dp.callback_query_handler(text='bio_brim')
    async def bio_brim(callback: types.CallbackQuery):
        Brim_bio = Brim().bio()
        await callback.message.answer(Brim_bio)
        await callback.answer()

    @dp.callback_query_handler(text='abilities_brim')
    async def bio_brim(callback: types.CallbackQuery):
        await callback.message.answer('Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()


    @dp.callback_query_handler(text='brim_q')
    async def bio_brim(callback: types.CallbackQuery):
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)

        await callback.message.answer(text='опис абілки')
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()


    @dp.callback_query_handler(text='brim_e')
    async def bio_brim(callback: types.CallbackQuery):
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)

        await callback.message.answer(text='опис aбілки')
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()


    @dp.callback_query_handler(text='brim_c')
    async def bio_brim(callback: types.CallbackQuery):
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)

        await callback.message.answer(text='опис aбілки')
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()


    @dp.callback_query_handler(text='brim_x')
    async def bio_brim(callback: types.CallbackQuery):
        with open("agents_images/brimstone.png", 'rb') as brim:
            await bot.send_photo(chat_id=callback.from_user.id, photo=brim)

        await callback.message.answer(text='опис ульти erghjegheruhghreiuhiuehveuihviuh')
        await callback.message.answer(text='Оберіть здібність:', reply_markup=abilities_brim)
        await callback.answer()




# @dp.callback_query_handler(text=['test'])
# async def test(callback: types.CallbackQuery):
#     await callback.message.answer('sho ty?')
#     await callback.answer()


executor.start_polling(dp, skip_updates=True)
