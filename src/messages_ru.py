from utils import TestStates

message_fname_ru = 'Salem, \n\nВас приветствует система сбора предложений компании CHI! \n\nНеобходимо пройти регистрацию, чтобы мы могли определить, кому высылать награды за ваши идеи и предложения! \n\nВаше имя {name_in_mes}?'

message_lname_ru = 'Приятно познакомиться, {name_in_mes}!\n\nВаша {lname_in_mes}?'

message_waiting_inquiry_ru = 'Пожалуйста, напишите свое предложение в одном сообщении:'

message_waiting_inquiry_thx_ru = 'Спасибо за ваше предложение, Владимир!\n\nВаше предложение №{namber_mes} принято на рассмотрение рабочей группой!\n\nВ течении 7 рабочих дней вам придет сообщение от нашего бота.\n\nВы можете выбрать категорию и сделать новое предложение:'
# Напиши своё имя
send_name_ru = 'Напиши своё имя'
# Ошибка напиши ответ должен быть Да/Нет
error_yes_and_no_ru = 'Ошибка напиши ответ должен быть Да/Нет'


# # Выбор языка







MESSAGES = {
    'greeting_fname': message_fname_ru,
    'greeting_lname': message_lname_ru,
    'message_waiting_inquiry':message_waiting_inquiry_ru,
    'message_waiting_inquiry_thx':message_waiting_inquiry_thx_ru,
    'error_yes_and_no':error_yes_and_no_ru,
    'send_name':send_name_ru,    
}
