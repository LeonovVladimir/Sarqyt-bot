import logging # для создания единого журнала логов в приложении. Нужен для aiogram

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

# импорт токена, конекта бд сообщения в отдельном файле
import keyboards as kb # кнопки для телеграма
from config import TOKEN # токен
from DBconfig import HOST, USER, PASSWD, PORT, DATABASE # конект к бд
from messages_ru import MESSAGES # сообщения в отдельном файле
# from utils import TestStates

#/ импорт стандартных библиотек
import os # для создания папок
import random # рандом для создания случайного имени фотографии
import datetime

import asyncio
from aiogram.dispatcher import Dispatcher

flag_group_id = None
# /


# mysql подключение
import mysql.connector
from mysql.connector import errorcode
try:
    db = mysql.connector.connect(
      host=HOST,
      user=USER,
      passwd=PASSWD,
      port=PORT,
      database=DATABASE
    )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
    sys.exit()
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
    sys.exit()
  else:
    print(err)
    sys.exit()

cursor = db.cursor()
# /

bot = Bot(token=TOKEN)
# For example use simple MemoryStorage for Dispatcher.
logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class reg(StatesGroup):
    lang = State() 
    fname = State()
    lname = State()
    fname_waiting_response = State()
    lname_waiting_response = State()
    waiting_inquiry = State()
    err_login = State()
    # reg
@dp.message_handler(state=reg.err_login)
async def name_step233(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Выбор языка s', reply_markup=kb.markup_lang)
    print("lol")    
    await reg.lang.set() #Стейт 

# жмём старт начинается регестрация 
@dp.message_handler(commands='start', commands_prefix='!/')
async def start_step(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Выбор языка', reply_markup=kb.markup_lang)    
    await reg.lang.set() #Стейт 

# =================================================================== lang
# Стейт lang
# выбор языка
# проверяем нажатые кнопки если они верны идем дальше ставим следующий стейт

@dp.message_handler(lambda message: message.text in ["Қазақша 🇰🇿", "Русский 🇷🇺", "English 🇬🇧"], state=reg.lang, content_types=types.ContentTypes.TEXT)
async def lang_true(message: types.Message, state: FSMContext):
    async with state.proxy() as data:    #вытаскиваем сообщение
        data['lang_date'] = message.text #присваиваем переменой    
    await message.answer(text=MESSAGES['greeting_fname'].format(name_in_mes=message.chat.first_name), reply_markup=kb.markup_yes_no)
    await reg.fname.set() #Стейт
# обрабатываем ошибку

@dp.message_handler(lambda message: message.text not in ["Қазақша 🇰🇿", "Русский 🇷🇺", "English 🇬🇧"], state=reg.lang)
async def lang_er(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Ошибка')
# =================================================================== fname
# Стейт fname

# при нажатии "нет" стави стейт fname_waiting_response
# ждём имя
@dp.message_handler(lambda message: message.text in ["Нет"], state=reg.fname)
async def fname_no(message: types.Message):
    await bot.send_message(message.from_user.id, 'Напиши свою фамилию', reply_markup=types.ReplyKeyboardRemove())    
    await reg.fname_waiting_response.set()

# ожидаем имя от пользователя
@dp.message_handler(state=reg.fname_waiting_response)
async def fname_no_waiting_answer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:    #вытаскиваем сообщение
        data['fname_date'] = message.text #присваиваем переменой     
    await message.answer(text=MESSAGES['greeting_lname'].format(name_in_mes=message.text, lname_in_mes=message.chat.last_name), reply_markup=kb.markup_yes_no)
    await reg.lname.set()
# -------------------------------

# если пользователь жмет да
# идем на нескс стейт
@dp.message_handler(lambda message: message.text in ["Да"], state=reg.fname)
async def fname_yes(message: types.Message, state: FSMContext):
    async with state.proxy() as data:    #вытаскиваем сообщение
        data['fname_date'] = message.chat.first_name #присваиваем переменой     
    await message.answer(text=MESSAGES['greeting_lname'].format(name_in_mes=message.chat.first_name, lname_in_mes=message.chat.last_name), reply_markup=kb.markup_yes_no)
    await reg.lname.set() #Стейт 
    # await state.finish()

# обробатываем ошибку
@dp.message_handler(lambda message: message.text not in ["Нет", "Да"], state=reg.fname)
async def fname_er(message: types.Message):
    await bot.send_message(message.from_user.id, MESSAGES['error_yes_and_no'], reply_markup=kb.markup_yes_no)    
# =================================================================== lname
# Стейт lname

# при нажатии "нет" стави стейт lname_waiting_response
# ждём фамилию
@dp.message_handler(lambda message: message.text in ["Нет"], state=reg.lname)
async def process_gender_invalid22(message: types.Message):
    await bot.send_message(message.from_user.id, MESSAGES['send_name'], reply_markup=types.ReplyKeyboardRemove())    
    await reg.lname_waiting_response.set()

# ожидаем фамилии от пользователя
# выводим ответ 
# заканчиваем скрипт 
# убираем стейт
@dp.message_handler(state=reg.lname_waiting_response)
async def name_step233333(message: types.Message, state: FSMContext):
    async with state.proxy() as data:    #вытаскиваем сообщение
        data['lname_date'] = message.text #присваиваем переменой     

        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Ваш язык:,', (data['lang_date'])),
                md.text('Ваш имя:,', (data['fname_date'])),
                md.text('Ваш фамилия:,', (data['lname_date'])),

                sep='\n',
            ),
            reply_markup=kb.markup_main,
            parse_mode=ParseMode.MARKDOWN, # рудимент убрать
        )
        # =====
        sql = "INSERT INTO `kaizen_registration` (`tel_fname`, `tel_lname`, `first_name`, `last_name`, `chat_id`, `lang`, `date_registration`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        val = (message.chat.first_name, message.chat.last_name, data['lang_date'], data['fname_date'], message.chat.id, data['lname_date'], message.date)
        cursor.execute(sql, val)
        db.commit()
        # ====
        await state.finish()
# -------------------------------
# если да сразу заканчиваем скрипт 
# убираем стейт
@dp.message_handler(lambda message: message.text in ["Да"], state=reg.lname)
async def name_stepqq2(message: types.Message, state: FSMContext):
        async with state.proxy() as data:    #вытаскиваем сообщение
            data['lname_date'] = message.chat.last_name #присваиваем переменой     

        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Ваш язык:,', (data['lang_date'])),
                md.text('Ваш имя:,', (data['fname_date'])),
                md.text('Ваш фамилия:,', (data['lname_date'])),

                sep='\n',
            ),
            reply_markup=kb.markup_main,
            parse_mode=ParseMode.MARKDOWN, # рудимент убрать
        )
        # =====
        sql = "INSERT INTO `kaizen_registration` (`tel_fname`, `tel_lname`, `first_name`, `last_name`, `chat_id`, `lang`, `date_registration`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        val = (message.chat.first_name, message.chat.last_name, data['lang_date'], data['fname_date'], message.chat.id, data['lname_date'], message.date)
        cursor.execute(sql, val)
        db.commit()
        # ====
        await state.finish()

# обробатываем ошибку
@dp.message_handler(lambda message: message.text not in ["Нет", "Да"], state=reg.lname)
async def lname_er(message: types.Message):
    await bot.send_message(message.from_user.id, MESSAGES['error_yes_and_no'], reply_markup=kb.markup_yes_no)    
# =================================================================== 
# Пользователь жмёт "Внести предложение"
# Пишем что ожидаем предложения от пользователя
@dp.message_handler(text=["Внести предложение","Указать на проблему"])
# @dp.message_handler(text=["Внести предложение","Указать на проблему"], commands=['info'])
async def process_suggestion(message: types.Message): 
    await bot.send_message(message.from_user.id,  MESSAGES['message_waiting_inquiry'].format(namber_mes=message.chat.first_name), 
                              reply_markup=types.ReplyKeyboardRemove())
    await reg.waiting_inquiry.set()                        
# Ждем ответ 
# Пишем что предложение принято
@dp.message_handler(content_types=["text"], state=reg.waiting_inquiry)
async def process_suggestion_wait_text(message: types.Message, state: FSMContext):
        if len(message.text)<=8:
                await bot.send_message(message.from_user.id, 'меньше 8', reply_markup=kb.markup_main)
        else:
                await bot.send_message(message.from_user.id,  MESSAGES['message_waiting_inquiry_thx'],
                                  reply_markup=kb.markup_main)  
        await state.finish()






@dp.message_handler(content_types=["photo"], state=reg.waiting_inquiry)
async def process_suggestion_wait_photo(message: types.Message, state: FSMContext):
                print(message.caption)
        # if len(message.caption)<=8:
        #         await bot.send_message(message.from_user.id, 'меньше 8', reply_markup=kb.markup_main)
        # else:
                path = F"/var/www/bot0.1.5/download/{message.chat.id}"
                try:
                    os.mkdir(path)
                except OSError:
                    pass
                else:
                    pass
                photo = message.photo.pop() 
                convert_date_telegram = (str(message.date).replace(' ', '_'))
                await photo.download (F'download/{message.chat.id}/{convert_date_telegram}-{message.message_id}.png')
                way_to_file = F'download/{message.chat.id}/{convert_date_telegram}-{message.message_id}.png'
                sql = "INSERT INTO kaizen_feedback (first_name, last_name, category, chat_id, suggestion, date_message, contacts, file_is_from, way_photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (message.chat.first_name, message.chat.last_name, '-', message.chat.id, way_to_file, message.date,'-','-','-')
                # ЗАМЕТКА у date_message стоит datetime (может выдовать ошибку если запрос не верный)
                cursor.execute(sql, val)
                db.commit()  

                global flag_group_id
                if flag_group_id == message.media_group_id:
                        print("net")
                else:
                    flag_group_id = message.media_group_id
                    if message.media_group_id != None:
                        print("taktak")
                        await bot.send_message(message.from_user.id, 'фото загружено', reply_markup=kb.markup_main)

                if message.media_group_id == None: 
                    print("taktak None") 
                    await bot.send_message(message.from_user.id, 'фото загружено', reply_markup=kb.markup_main)

                await state.finish()
                # print(message.message_id)
                # print(message.date)
                # print(message.caption)
                # 



#---------------------------
@dp.message_handler(text=["Изменить контактные данные 🖊"])
async def chenge_info(message: types.Message): 
    await bot.send_message(message.from_user.id, 'Выбор языка', reply_markup=kb.markup_lang)    
    await reg.lang.set() #Стейт    
# =================================================================== 




@dp.message_handler()
async def echo_message(message: types.Message):
    try:
        sql = "SELECT * FROM `kaizen_registration` WHERE `chat_id` = %s LIMIT 1"
        val = (message.chat.id, )
        cursor.execute(sql, val)

        id_tel = cursor.fetchall()
        for id_tel_end in id_tel:
            id_tel_sql = id_tel_end[3]

        db.commit()

        if id_tel_sql is not None:
            await bot.send_message(message.from_user.id, 'Не понимаю команду', reply_markup=kb.markup_main)

    except Exception as e:
            sql = "INSERT INTO `kaizen_registration` (`tel_fname`, `tel_lname`, `first_name`, `last_name`, `chat_id`, `lang`, `date_registration`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            val = (message.chat.first_name, message.chat.last_name, "", "", message.chat.id, "", message.date)
            cursor.execute(sql, val)
            db.commit()

            await bot.send_message(message.from_user.id, 'Вы не зарегистрированы!\nВыберите язык', reply_markup=kb.markup_lang)  
            await reg.lang.set()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)