import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ab23ee0880dd24f21affe.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝗛𝗘𝗟𝗟𝗢, 𝗜 𝗔𝗠 𝗦𝗨𝗣𝗘𝗥 𝗙𝗔𝗦𝗧 𝗠𝗨𝗦𝗜𝗖 𝗣𝗟𝗔𝗬𝗘𝗥
𝗕𝗢𝗧 𝗙𝗢𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗚𝗥𝗢𝗨𝗣...
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝗖𝗥𝗘𝗔𝗧𝗘𝗥 : [𝗕𝗛𝗔𝗧𝗔𝗞𝗧𝗜_𝗔𝗧𝗠𝗔](https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK)
┣★ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 : [𝗦𝗨𝗣𝗣𝗢𝗥𝗧](https://t.me/SUBHI_WORLD)
┣★ 𝗦𝗢𝗨𝗥𝗖𝗘 : [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲](https://t.me/A_BUT)
┗━━━━━━━━━━━━━━━━━┛

━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕❰𝗞𝗜𝗗𝗡𝗔𝗣 𝗠𝗘❱➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "legend"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ab23ee0880dd24f21affe.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙅𝙤𝙞𝙣 𝙃𝙚𝙧𝙚 𝘼𝙣𝙙 𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url=f"https://t.me/SUBHI_WORLD")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ab23ee0880dd24f21affe.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😆𝗥𝗘𝗣𝗢 𝗟𝗔𝗡𝗜 𝗛 😆", url=f"https://t.me/SUBHI_WORLD")
                ]
            ]
        ),
    )
