import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from get import get_picture, tomorrow_picture, get_picture_dweek
from datatime import get_week

API_TOKEN = ''


# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
  """
  This handler will be called when user sends /start or /help command
  """

  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  buttons = [
      types.KeyboardButton("Расписание обедов"),
      types.KeyboardButton("Меню столовой"),
      types.KeyboardButton("Неделя"),
      types.KeyboardButton('Пары')
    
  ]
  keyboard.add(*buttons) 

  await message.reply("Привет!\nЯ покажу тебе расписание и меню обеда группы CA-420.", reply_markup=keyboard)




@dp.message_handler(Text(equals="Расписание обедов"))
async def rasp(message: types.Message):
  # await message.reply("пример текста")
  keyboard = types.InlineKeyboardMarkup()
  # keyboard.add(types.InlineKeyboardButton(text="Понедельник", callback_data="Понедельник"),
  #              types.InlineKeyboardButton(text="Вторник", callback_data="Вторник"),
  #              types.InlineKeyboardButton(text="Вторник", callback_data="Вторник"),
  #              types.InlineKeyboardButton(text="Вторник", callback_data="Вторник"))
  days=["Понедельник","Вторник","Среда","Четверг","Пятница"]
  for day in days:
      keyboard.add(types.InlineKeyboardButton(text=day, callback_data=day))

  await message.answer("День недели", reply_markup=keyboard)


@dp.callback_query_handler(text=["Понедельник","Вторник","Среда","Четверг","Пятница"])
async def send_rasp(call: types.CallbackQuery): 
  # days=["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"]
  days = {
  "Понедельник" : "С 11:00 до 11:20",
  "Вторник" : "С 16:00 до 16:10",
  "Среда" : "С 10:30 до 10:50",
  "Четверг" : "С 12:20 до 12:40",
  "Пятница" : "С 12:20 до 12:40",
  # "Суббота" : "капец ты лох"
  }

  for day in days:
    if day == call.data:
      await call.message.answer(f"{day} \n{days[day]}")

  # await call.message.reply(str('Понедельник'))




@dp.message_handler(Text(equals="Меню столовой"))
async def menu(message: types.Message):
  # await message.reply_photo(await get_picture())

  keyboard = types.InlineKeyboardMarkup()

  days=["Сегодня", "Завтра"]
  for day in days:
    keyboard.add(types.InlineKeyboardButton(text=day, callback_data=day))
  await message.answer("Вам на ...", reply_markup=keyboard)
  
@dp.callback_query_handler(text=["Сегодня","Завтра"])
async def send_menu(call: types.CallbackQuery): 
  menu = {
    "Сегодня" : await get_picture(),
    "Завтра" : await tomorrow_picture()
  }
  try:
    for day in menu:
      if day == call.data:
        if type(menu[day]) == str:
          await call.message.answer(menu[day]) 
        else:
          await call.message.answer_photo(menu[day])
  except Exception:
    await call.message.answer('Меню не выложили!')



@dp.message_handler(Text(equals="Неделя"))
async def week(message: types.Message):
  tweek = await get_week()
  if tweek % 2 == 0:
    await message.answer("Четная(синяя)")
  else:
    await message.answer("Нечетная(красная)")

# @dp.message_handler(Text(equals="Пары"))
# async def pari(message: types.Message):
#   pari = await pari_picture()
#   await message.answer_photo(pari)

@dp.message_handler(Text(equals="Пары"))
async def pari(message: types.Message):
  dweekpic = await get_picture_dweek()
  await message.answer_photo(dweekpic)




































































# @dp.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
# async def send_time(message: types.Message):
#   commands=['/monday', '/tuesday', '/wednesday', '/thursday', '/friday']
#   answers = {
#   "/monday" : "С 14:40 до 15:00",
#   "/tuesday" : "С 10:30 до 10:50",
#   "/wednesday" : "С 12:20 до 12:40",
#   "/thursday" : "С 16:00 до 16:10",
#   "/friday" : "С 10:30 до 10:50"
#   }
  
  # for command in commands:
  #       if command == message.get_command():
  #         await message.reply(answers[command])



# @dp.message_handler(commands="rasp")
# async def cmd_random(message: types.Message):
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton(text="Расписание", callback_data="random_value"))
#     await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)

# @dp.callback_query_handler(text="random_value")
# async def send_random_value(call: types.CallbackQuery):
#     await call.message.answer(str('random'))


























if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)