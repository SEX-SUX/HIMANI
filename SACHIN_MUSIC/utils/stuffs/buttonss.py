from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [
    [
        InlineKeyboardButton("+", callback_data="mplus HELP_SACHIN"),
        InlineKeyboardButton("+", callback_data="mplus HELP_MUSIC"),
        InlineKeyboardButton("+", callback_data="mplus HELP_SANATANI")
    ],          
    [
        InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"settings_back_helper"), 
        InlineKeyboardButton("ɴᴇxᴛ", callback_data=f"splus"),
    ]
    ]
