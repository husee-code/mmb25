from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ap_start_kb = InlineKeyboardMarkup(row_width=1).add(*[
    InlineKeyboardButton("Настройка мастеров", callback_data="masters"),
    InlineKeyboardButton("Настройка досуга", callback_data="dosug"),
    InlineKeyboardButton("Настройка мест", callback_data="places"),
    InlineKeyboardButton("Посмотреть статистику за месяц", callback_data="check_stats"),
    InlineKeyboardButton("Коэффициенты таблицы", callback_data="table_coef")
])

ap_settings_kb = InlineKeyboardMarkup(row_width=1).add(*[
    InlineKeyboardButton("Добавить новую вкладку", callback_data="add_tab"),
    InlineKeyboardButton("Добавить новое поле во вкладку", callback_data="add_field"),
    InlineKeyboardButton("Изменить инфу о поле", callback_data="edit_field"),
    InlineKeyboardButton("Удалить поле", callback_data="remove_field"),
    InlineKeyboardButton("Изменить название вкладки", callback_data="edit_tab"),
    InlineKeyboardButton("Удалить вкладку", callback_data="remove_tab"),
])

table_coef_kb = InlineKeyboardMarkup(row_width=1).add(*[
    InlineKeyboardButton("R21", callback_data="R21"),
    InlineKeyboardButton("R22", callback_data="R22"),
    InlineKeyboardButton("R23", callback_data="R23"),
    InlineKeyboardButton("R24", callback_data="R24"),
    InlineKeyboardButton("Черногория", callback_data="xe"),

])

sphere_options_kb = InlineKeyboardMarkup(row_width=1).add(*[
    InlineKeyboardButton('Открыть эту вкладку', callback_data="open_tab"),
    InlineKeyboardButton('Изменить название', callback_data="edit_name"),
    InlineKeyboardButton('Добавить мастера', callback_data="add_master"),
    InlineKeyboardButton('Удалить вкладку', callback_data="remove_tab"),
])
