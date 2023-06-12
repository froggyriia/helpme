from aiogram.types import \
    KeyboardButton, \
    ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, \
    InlineKeyboardMarkup, \
    InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData

show_schedule = InlineKeyboardButton('Посмотреть расписание🙊🗓', callback_data='show_schedule')
show_homework = InlineKeyboardButton('Посмотреть домашнее задние 📖📚', callback_data='show_homework')
edit_schedule = InlineKeyboardButton('Редактировать расписание ✏️🗓', callback_data='edit_schedule')
edit_homework = InlineKeyboardButton('Редактировать домашнее задние ✏️📖', callback_data='edit_homework')
show_a_cat_kb = InlineKeyboardButton('Получить дозу мотивации🌷🐱🌷', callback_data='show_a_cat')

inlineShowCat = InlineKeyboardMarkup().add(show_a_cat_kb)

inlineKeyboardGreeting = InlineKeyboardMarkup().add(show_schedule).add(show_homework).add(edit_homework).add(
    edit_schedule).add(show_a_cat_kb)


weekday_cd = CallbackData("w_w", "weekday")
monday = InlineKeyboardButton('Понедельник', callback_data=weekday_cd.new(weekday='monday'))
tuesday = InlineKeyboardButton('Вторник', callback_data=weekday_cd.new(weekday='tuesday'))
wednesday = InlineKeyboardButton('Среда', callback_data=weekday_cd.new(weekday='wednesday'))
thursday = InlineKeyboardButton('Четверг', callback_data=weekday_cd.new(weekday='thursday'))
friday = InlineKeyboardButton('Пятница', callback_data=weekday_cd.new(weekday='friday'))
saturday = InlineKeyboardButton('Суббота', callback_data=weekday_cd.new(weekday='saturday'))
sunday = InlineKeyboardButton('Воскресенье', callback_data=weekday_cd.new(weekday='sunday'))
week_schedule = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

inlineKeyboardWeekSchedule = InlineKeyboardMarkup()
for day in week_schedule:
    inlineKeyboardWeekSchedule.add(day)
