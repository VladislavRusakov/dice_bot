from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import user
from asyncio import sleep


bot = Bot('1092581025:AAH0jngIMqeH0UceSctthJJHLDERt8zIQvA')
dp = Dispatcher(bot)


@dp.message_handler(commands=['roll'])
async def on_roll_message(message: types.Message):
    """Хендлер сообщения /roll. Запускает цикл бросков кубика. Ничья запускает рекурсию."""
 #   await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}')
 #   await sleep(1)

    await bot.send_message(message.from_user.id, 'Бросает бот')
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(2)
    
    await bot.send_message(message.from_user.id, f'Бросает {message.from_user.username}')
    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(4)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, 'Побеждает бот')
    elif user_data > bot_data:
        await bot.send_message(message.from_user.id, f'Побеждает {message.from_user.username}')
    else:
        await on_roll_message(message)

        
@dp.message_handler(commands=['whoami'])
async def on_whoami_message(message: types.Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAEEMvRiNIYXOCd7MRyqf8Fy1PkeDsMUcgACfxAAAvlWYEuWGlMqVhX_xyME')
        
        
@dp.message_handler()
async def on_help_messaage(message: types.Message):
    """Отвечает на любое текстовое сообщение информацией о том, как играть."""
    if message:
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}')
        await bot.send_message(message.from_user.id, 'Для начала напиши /roll')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
