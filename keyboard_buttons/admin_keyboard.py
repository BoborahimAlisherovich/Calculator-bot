from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni"),
            KeyboardButton(text="Reklama yuborish"),
        ],
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

manzil = InlineKeyboardMarkup(
    inline_keyboard= [
      [
    InlineKeyboardButton(text="calkulyator",callback_data="kalkulyator"),
     InlineKeyboardButton(text="Bizning manzil",url="https://www.google.com/maps/@40.1028381,65.3730178,16z?entry=ttu")],
    

    [InlineKeyboardButton(text="Admin bilan bog'lanish",url="https://t.me/Alisherov1ch_002")],
    #  [InlineKeyboardButton(text="bot haqida",)],
    ]
)





