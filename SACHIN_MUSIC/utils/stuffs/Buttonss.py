from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [
    [
        InlineKeyboardButton("+", callback_data="splus HELP_ChatGPT"),
        InlineKeyboardButton("+", callback_data="splus HELP_Group"),
        InlineKeyboardButton("sᴛᴄᴋʀs", callback_data="mplus HELP_Sticker")
    ],
    [
        InlineKeyboardButton("+", callback_data="splus HELP_TagAll"),
        InlineKeyboardButton("+", callback_data="splus HELP_Info"),
        InlineKeyboardButton("+", callback_data="splus HELP_Extra")
    ],
    [
        InlineKeyboardButton("+", callback_data="splus HELP_Image"),
        InlineKeyboardButton("+", callback_data="splus HELP_Action"),
        InlineKeyboardButton("+", callback_data="splus HELP_Search")
    ],    
    [
        InlineKeyboardButton("+", callback_data="splus HELP_Font"),
        InlineKeyboardButton("+", callback_data="splus HELP_Game"),
        InlineKeyboardButton("+", callback_data="splus HELP_TG")
    ],
    [
        InlineKeyboardButton("+", callback_data="splus HELP_Imposter"),
        InlineKeyboardButton("+", callback_data="splus HELP_TD"),
        InlineKeyboardButton("+", callback_data="splus HELP_HT")
    ], 
    [
        InlineKeyboardButton("+", callback_data="splus HELP_TTS"),
        InlineKeyboardButton("+", callback_data="splus HELP_Fun"),
        InlineKeyboardButton("+", callback_data="splus HELP_Q")
    ],          
    [
        InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"settings_back_helper"), 
        InlineKeyboardButton("ɴᴇxᴛ", callback_data=f"managebot123 settings_back_helper"),
    ]
    ]
