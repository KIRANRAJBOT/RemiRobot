import os
from pyrogram import Client, filters
from pyrogram.types import *

from RemiRobot.conf import get_str_key
from RemiRobot import pgram

REPO_TEXT = "**A Cute [BOT](https://telegra.ph/file/d2815963abcae6fa20dc8.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Owner ⇀ : 『 [Lovely](t.me/Horimaya) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @CrowdXStrike «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("💖 ʀᴇᴘᴏꜱɪᴛᴏʀʏ 💖", url=f"https://github.com/Hodacka/RemiRobot"),
        InlineKeyboardButton(" Network 💗", url=f"https://t.me/YuichiroNetwork"),
      ],[
        InlineKeyboardButton("ᴏᴡɴᴇʀ ❣️", url="https://t.me/Horimaya"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ 💞", url="https://t.me/RemiSupport"),
      ],[
        InlineKeyboardButton("❤️ ᴜᴘᴅᴀᴛᴇꜱ ❤️", url="https://t.me/CrowdXStrike"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ 💕", url="https://t.me/CrazyBoy_430"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pgram, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
