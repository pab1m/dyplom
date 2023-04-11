class EditAmountOfPost(StatesGroup):
    edit_user_id = State()
    available_amount = State()
    ed_start_date = State()
    ed_end_date = State()


# function to edit amount of post from users
@dp.callback_query_handler(text='edit_amount_post')
async def edit_amount_of_post(call: types.CallbackQuery):
    await call.message.answer("Send users id which you want to edit", reply_markup=get_cancel_inb())
    await EditAmountOfPost.edit_user_id.set()


# function to get users id that change the amount of post
@dp.message_handler(state=EditAmountOfPost.edit_user_id)
async def get_users_id(message: types.Message, state: FSMContext) -> None:
    await message.answer("Send a new amount of post ", reply_markup=get_cancel_inb())
    async with state.proxy() as data:
        data['edit_user_id'] = message.text
    await EditAmountOfPost.next()


# function change amount of post to user
@dp.message_handler(state=EditAmountOfPost.available_amount)
async def get_amount_post(message: types.Message, state: FSMContext) -> None:
    await message.answer("New start date?", reply_markup=get_cancel_inb())
    async with state.proxy() as data:
        data['available_amount'] = message.text
    await EditAmountOfPost.next()


@dp.message_handler(state=EditAmountOfPost.ed_start_date)
async def get_mew_start_date(message: types.Message, state: FSMContext) -> None:
    await message.answer("New end date?", reply_markup=get_cancel_inb())
    async with state.proxy() as data:
        data['ed_start_date'] = message.text
    await EditAmountOfPost.next()


@dp.message_handler(state=EditAmountOfPost.ed_end_date)
async def get_mew_start_date(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['ed_end_date'] = message.text
    await database.edit_amount_post(state)
    await message.answer('Save change success')
    await state.finish()
    loger.info(f"Admin {message.chat.username} {message.chat.id} change amount of post for user {data['edit_user_id']} "
               f"new amount of post {data['available_amount']} and change the post date {data['ed_start_date']},{data['ed_end_date']}")
    await message.answer("Choose options", reply_markup=get_start_inb())