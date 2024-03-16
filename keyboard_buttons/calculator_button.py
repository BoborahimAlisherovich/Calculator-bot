from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

# 7 8 9 +
# 4 5 6 -
# 1 2 3 *
# , 0 / =

calculator_builder = InlineKeyboardBuilder()
for i in "789+456-123*,0/=DC":
    calculator_builder.add(InlineKeyboardButton(text=i, callback_data=i))
calculator_builder.add (InlineKeyboardButton(text="Bizning manzil",url="https://www.google.com/maps/@40.1028381,65.3730178,16z?entry=ttu"))
    
calculator_builder.add(InlineKeyboardButton(text="Admin bilan bog'lanish",url="https://t.me/Alisherov1ch_002"))
calculator_builder.adjust(4,4,4,4,2,2)


calculator_builder = calculator_builder.as_markup()
