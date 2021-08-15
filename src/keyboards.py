from aiogram.types import ReplyKeyboardMarkup, \
                        KeyboardButton

button_kz = KeyboardButton("Қазақша 🇰🇿")
button_ru = KeyboardButton("Русский 🇷🇺")
button_en = KeyboardButton("English 🇬🇧")

# кнопки язык
markup_lang = ReplyKeyboardMarkup(resize_keyboard=True).row(button_kz, button_ru).add(button_en)

yes_kz = KeyboardButton("Иә")
no_kz = KeyboardButton("Емес")

yes_ru = KeyboardButton("Да")
no_ru = KeyboardButton("Нет")

yes_en = KeyboardButton("Yes")
no_en = KeyboardButton("No")

# кнопки ДА/НЕТ
markup_yes_no = ReplyKeyboardMarkup(resize_keyboard=True).row(yes_ru, no_ru)

# кнопки Запрос
button_main_one_ru = KeyboardButton("Внести предложение")
button_main_two_ru = KeyboardButton("Указать на проблему")
button_main_three_ru = KeyboardButton("Изменить контактные данные 🖊")
button_main_my_applications = KeyboardButton("Мои заявки 📝")

# кнопки язык
markup_main = ReplyKeyboardMarkup(resize_keyboard=True).add(button_main_one_ru).add(button_main_two_ru).add(button_main_three_ru).add(button_main_my_applications)

