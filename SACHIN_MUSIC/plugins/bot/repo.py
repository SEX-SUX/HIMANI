from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SACHIN_MUSIC import app
from config import BOT_USERNAME
from SACHIN_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ sᴀᴄʜɪɴ ʀᴇᴘᴏs ⌾
 
◎ ʙʜᴀɢ ʙʜᴏsᴅɪᴋᴇ
 
◎ ʀᴇᴘᴏ ᴛᴏ ɴᴀ ᴅᴜɴɢᴀ
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴇʟᴘ •", url="https://t.me/Il_4ST_FIGHTER_lI"),
          InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/V_VIP_OWNER"),
          ],
               [
                InlineKeyboardButton("• sᴀɴᴀᴛᴀɴɪ ɴᴇᴛᴡᴏʀᴋ •", url=f"https://t.me/ALL_SANATANI_BOT"),
],
[
InlineKeyboardButton("• ᴏғғɪᴄɪᴀʟ ʙᴏᴛ •", url=f"https://t.me/HIMANSHI_MUSIC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/256b87e379dfd405b957d.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
