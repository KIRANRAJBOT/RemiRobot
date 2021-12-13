import os
from pyrogram import Client, filters
from pyrogram.types import *

from RemiRobot.conf import get_str_key
from RemiRobot import pbot

REPO_TEXT = "[Remi Repository](https://telegra.ph/file/d2815963abcae6fa20dc8.jpg) \nRemi Open Sorce code! \nGive Star ⭐ and Fork 💖 \nAny errors Report in @RemiSupport"
  

  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("💕 Support 💕", url=f"https://t.me/RemiSupport"),
        InlineKeyboardButton("💖 Repository 💖", url=f"https://GitHub.com/Hodacka/RemiRobot"),
      ],[
        InlineKeyboardButton("💞 Owner 💞", url="https://t.me/Horimaya"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def scan(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,

        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
       )
