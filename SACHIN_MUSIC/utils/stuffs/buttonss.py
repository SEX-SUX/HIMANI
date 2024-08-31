from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONSS(object):
    MBUTTON = [
    [
        InlineKeyboardButton("+", callback_data="splus HELP_SACHIN"),
        InlineKeyboardButton("+", callback_data="splus HELP_MUSIC"),
        InlineKeyboardButton("+", callback_data="splus HELP_SANATANI")
    ],          
    [
        InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"settings_back_helper"), 
        InlineKeyboardButton("ɴᴇxᴛ", callback_data=f"managebot123 settings_back_helper"),
    ]
    ]
