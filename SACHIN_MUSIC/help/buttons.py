from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [
    [
        InlineKeyboardButton("ᴀᴄᴛɪᴏɴ", callback_data="mplus HELP_H1"),
        InlineKeyboardButton("ɢʀᴘs", callback_data="mplus HELP_H2"),
        InlineKeyboardButton("ᴀɪ", callback_data="mplus HELP_H3"),
    ],
    [
        InlineKeyboardButton("ɪɴꜰᴏ", callback_data="mplus HELP_H4"),
        InlineKeyboardButton("ᴛʀᴘʜ", callback_data="mplus HELP_H5")
        InlineKeyboardButton("ᴇxᴛʀᴀ", callback_data="mplus HELP_H6")
    ],
    [
        InlineKeyboardButton("ᴛᴀɢᴀʟʟ", callback_data="mplus HELP_H7"),
        InlineKeyboardButton("ʜsᴛᴀɢ", callback_data="mplus HELP_H8")
        InlineKeyboardButton("ғᴏɴᴛ", callback_data="mplus HELP_H9"),
    ],
    [
        InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data="mplus HELP_H10"),
        InlineKeyboardButton("sᴛᴄᴋʀs", callback_data="mplus HELP_H11")
        InlineKeyboardButton("ɪᴍᴘsᴛʀ", callback_data="mplus HELP_H12"),
    ],    
    [
        InlineKeyboardButton("ғᴜɴs", callback_data="mplus HELP_H13"),
        InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_H14")
    ],          
    [
        InlineKeyboardButton("⌯ ʙᴀᴄᴋ ⌯", callback_data=f"settingsback_helper",),
    ]
    ]
