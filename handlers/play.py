#BHATAKTI ATMA // @ZINDA_H_TU_MERE_LIYE_HEART_HACK

import os
from os import path
from asyncio.queues import QueueEmpty
from typing import Callable
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from modules.cache.admins import set
from modules.callsmusic import callsmusic, queues
from modules.callsmusic.callsmusic import client as USER
from modules.helpers.admins import get_administrators
import requests
import aiohttp
import yt_dlp
from youtube_search import YoutubeSearch
from modules import converter
from modules.downloaders import youtube
from modules.config import DURATION_LIMIT, que, SUDO_USERS
from modules.cache.admins import admins as a
from modules.helpers.filters import command, other_filters
from modules.helpers.command import commandpro
from modules.helpers.decorators import errors, authorized_users_only
from modules.helpers.errors import DurationLimitError
from modules.helpers.gets import get_url, get_file_name
from modules.helpers.channelmusic import get_chat_id
import aiofiles
import ffmpeg
from PIL import Image, ImageFont, ImageDraw
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream

# plus
chat_id = None
useer = "NaN"



def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(filename)


# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    return image.resize((newWidth, newHeight))


async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open("etc/foreground.jpg")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/font.otf", 32)
    draw.text((190, 550), f"Title: {title[:70]} ...", (255, 255, 255), font=font)
    draw.text((190, 590), f"Duration: {duration}", (255, 255, 255), font=font)
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text(
        (190, 670),
        f"Powered By: 👑ᵛ͢ᵎᵖ𝄟🍻⃝🇧ͥ𝐇ͫA̶T̶A̶K̶𝐓𝐈⃟💋👻⃝🇦𝐓𝐌𝐀⃝🖤 (@ZINDA_H_TU_MERE_LIYE_HEART_HACK)",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")


@Client.on_message(
    commandpro(["/play", "/ytp", "!Play"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer

    lel = await message.reply("**🔄 𝗣𝗥𝗢𝗦𝗘𝗦𝗦𝗜𝗡G...**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "BHATAKTI_MUSIC"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
     
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace("https://t.me/+","https://t.me/lovely_friends_2/")
                except:
                    await lel.edit(
                        "<b>🤖𝗔𝗕𝗕𝗘 𝗔𝗗𝗠𝗜𝗡 𝗧𝗢 𝗕𝗡𝗔 𝗣𝗛𝗔𝗟𝗬😬\n😘𝗠𝗨𝗝𝗛𝗘🌷...</b>",
                    )
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id,
                        "**💐𝗕𝗛𝗔𝗧𝗔𝗞𝗧𝗜_𝗠𝗨𝗦𝗜𝗖 ♻️ 𝗔𝗦𝗦𝗜𝗦𝗧𝗔𝗡𝗧 🤞 𝗡𝗢𝗪 🌹 𝗥𝗘𝗔𝗗𝗬 👻\n😘 𝗧𝗢 ✌️ 𝗣𝗟𝗔𝗬 💞 𝗠𝗨𝗦𝗜𝗖 🌷...**",
                    )

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"<b>💥𝗦𝗥𝗬 𝗔𝗦𝗦𝗜𝗦𝗧𝗔𝗡𝗧 😔 𝗙𝗔𝗜𝗟𝗗 ⚠️ 𝗧𝗢 📵\n🥺 𝗝𝗢𝗜𝗡 ✌️ 𝗝𝗢𝗜𝗡 💞 𝗖𝗛𝗔𝗧 🌷..."
                    )
    try:
        await USER.get_chat(chid)
        # lmoa = await client.get_chat_member(chid,wew)
    except:
        await lel.edit(
            f"**💥 𝗦𝗥𝗬 𝗔𝗦𝗦𝗜𝗦𝗧𝗔𝗡𝗧 😔 𝗙𝗔𝗜𝗟𝗗 ⚠️ 𝗧𝗢 📵\n🥺 𝗝𝗢𝗜𝗡 ✌️ 𝗝𝗢𝗜𝗡 💞 𝗖𝗛𝗔𝗧 🌷...**"
        )
        return

    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"**💥 𝗣𝗟𝗔𝗬 🔊 𝗠𝗨𝗦𝗜𝗖 ✨ 𝗪𝗔𝗜𝗧 ⚡️\n🤟 𝗧𝗛𝗢𝗗𝗜 😒 𝗗𝗘𝗥 ⚡️ {DURATION_LIMIT} 💞...**"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/ab23ee0880dd24f21affe.png"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            text="╰𝗟𝗘𝗧,𝗦 𝗝𝗢𝗜𝗡 𝗠𝗬 𝗚𝗥𝗢𝗨𝗣╯",
                            url=f"https://t.me/SUBHI_WORLD")

                ]
            ]
        )

        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            keyboard = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            text="𒋲〚⚜️𝐉𝐎𝐈𝐍⚜️』𒋲",
                            url=f"https://t.me/SUBHI_WORLD")

                ]
            ]
        )

        except Exception as e:
            title = "NaN"
            thumb_name = "https://telegra.ph/file/ab23ee0880dd24f21affe.png"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            text="╰𒋲〚⚜️𝐉𝐎𝐈𝐍⚜️』𒋲╯",
                            url=f"https://t.me/SUBHI_WORLD")

                ]
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**💥 𝗣𝗟𝗔𝗬 🔊 𝗠𝗨𝗦𝗜𝗖 💿 𝗟𝗘𝗦𝗦  ⚡️\n🤟 𝗧𝗛𝗘𝗡 ⚡️ {DURATION_LIMIT} 💞 𝗙𝗘𝗪 𝗠𝗜𝗡𝗨𝗧𝗘𝗦 ...**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit(
                "**🤖 𝗕𝗛𝗔𝗜 ⚜️ 𝗬𝗔 𝗨𝗦𝗞𝗜 𝗕𝗛𝗘𝗡 ⚠️ 🥱 𝗡𝗔𝗔𝗠 😬 𝗕𝗧𝗔𝗢 𝗠𝗨𝗦𝗜𝗖 ⚜️ 𝗞𝗔 😍\n💞 𝗬𝗔 𝗣𝗔𝗚𝗔𝗟 𝗛𝗢 🌷...**"
            )
        await lel.edit("**🔎 𝗦𝗘𝗔𝗥𝗖𝗛𝗜𝗡𝗚 ...**")
        query = message.text.split(None, 1)[1]
        # print(query)
        await lel.edit("**🔄 𝗣𝗟𝗘𝗔𝗦𝗘 𝗪𝗔𝗜𝗧 ...**")
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**🔊 𝗠𝗨𝗝𝗛𝗘 😃 𝗬𝗘 ♻️ 𝗠𝗨𝗦𝗜𝗖 🤧 𝗡𝗢𝗜 💔 𝗠𝗜𝗟𝗔 ❗️\n💞 𝗔𝗚𝗔𝗜𝗡 𝗧𝗥𝗬 ✨ 𝗞𝗥 🌷...**"
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            text="╰𒋲〚⚜️𝐉𝐎𝐈𝐍⚜️』𒋲╯",
                            url=f"https://t.me/SUBHI_WORLD")

                ]
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**💥 𝗪𝗔𝗜𝗧 𝗞𝗥 🔊 𝗠𝗨𝗦𝗜𝗖  💿 𝗕𝗔𝗝𝗡𝗬  𝗩𝗔𝗟𝗔 ⚡️\n🤟 𝗛 ⚡️ {DURATION_LIMIT} 💞 𝗪𝗔𝗜𝗧 𝗙𝗘𝗪 𝗠𝗜𝗡𝗨𝗧𝗘,𝗦 ...**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(message.chat.id) in ACTV_CALLS:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
            photo="final.png",
            caption="**💥 𝗕𝗛𝗔𝗧𝗔𝗞𝗧𝗜_𝗔𝗧𝗠𝗔 🤞\n💿 𝗔𝗗𝗗𝗜𝗡𝗚 𝗔 𝗦𝗢𝗡𝗚 ❗️\n🔊 𝗔𝗧  💞  » `{}` 🌷 ...**".format(position),
            reply_markup=keyboard,
        )
    else:
        await callsmusic.pytgcalls.join_group_call(
                message.chat.id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            ) 
        await message.reply_photo(
            photo="final.png",
            reply_markup=keyboard,
            caption="**💥 𝗕𝗛𝗔𝗧𝗔𝗞𝗧𝗜 𝗔𝗧𝗠𝗔 🤞 𝗠𝗨𝗦𝗜𝗖 💞\n🎸 𝗡𝗢𝗪  🔊 𝗣𝗟𝗔𝗬𝗜𝗡𝗚 😍 𝗢𝗣 🥀 𝗦𝗢𝗨𝗡𝗗  ...**".format(),
        )

    os.remove("final.png")
    return await lel.delete()
    
    
    
@Client.on_message(commandpro(["/pause", "Pause"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/ab23ee0880dd24f21affe.png", 
                             caption="**💥 𝗠𝗔𝗜 𝗧𝗢 𝗖𝗛𝗨𝗣 🤞 𝗛𝗢 𝗚𝗬𝗔 𝗔𝗕𝗕 𝗞𝗥𝗢 🥶\n💞 𝗕𝗔𝗞𝗖𝗛𝗢𝗗𝗜 🥀 ▶️ 𝗣𝗔𝗨𝗦𝗘𝗗 𝗕𝗛𝗔𝗧𝗔𝗞𝗧𝗜_𝗠𝗨𝗦𝗜𝗖🌷 ...**"
    )


@Client.on_message(commandpro(["/resume", "Resume"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/ab23ee0880dd24f21affe.png", 
                             caption="**💥 𝗛𝗢 𝗚𝗬𝗜 𝗞𝗛𝗔𝗧𝗔𝗠 ♻️ 𝗕𝗔𝗞𝗖𝗛𝗢𝗗𝗜 𝗔𝗣𝗞𝗜 👅 𝗠𝗨𝗦𝗜𝗖 𝗦𝗧𝗔𝗥𝗧 🤞 𝗔𝗚𝗔𝗜𝗡\n𝗡𝗢𝗪🥀 ⏸ 𝗣𝗟𝗔𝗬𝗜𝗡𝗚 𝗧𝗢 𝗕𝗛𝗔𝗧𝗔𝗞𝗧𝗜 𝗠𝗨𝗦𝗜𝗖🌷 ...**"
    )



@Client.on_message(commandpro(["/skip", "/next", "Skip", "Next"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = message.chat.id
    ACTV_CALL = []
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALL.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALL:
        await message.reply_text("**💥 𝗬𝗥𝗥 𝗠 ♻️ 𝗫𝗛𝗨𝗧𝗜𝗬𝗔 😑 𝗛𝗨 𝗞𝗬𝗔 💞\n𝗞𝗨𝗖𝗛 🔇 𝗖𝗛𝗔𝗟𝗔𝗬𝗔 𝗛𝗨𝗔 𝗕𝗛𝗜 𝗛 𝗧𝗨𝗠𝗡𝗬 🌷 ...**")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
            
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                    InputStream(
                        InputAudioStream(
                            callsmusic.queues.get(chat_id)["file"],
                        ),
                    ),
                )

    await message.reply_photo(
                             photo="https://telegra.ph/file/ab23ee0880dd24f21affe.png", 
                             caption=f'**💥 𝗟𝗢 𝗕𝗔𝗗𝗔𝗟 𝗚𝗬𝗔 𝗦𝗢𝗡𝗚 🔈𝗞𝗥𝗢  🤞\nNøω 🥀 𝗠𝗝𝗘  ⏩ 𝗦𝗞𝗜𝗣𝗣𝗘𝗗 🌷 ...**'
   ) 


@Client.on_message(commandpro(["/end", "End", "/stop", "Stop"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        callsmusic.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await callsmusic.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/ab23ee0880dd24f21affe.png", 
                             caption="**💥 𝗞𝗛𝗨𝗝𝗟𝗜 😑 𝗛 𝗞𝗬𝗔 𝗕𝗘 🔈 𝗦𝗧𝗢𝗣 \n🤞 𝗞𝗬𝗨 🥀 ❌ 𝗞𝗜𝗬𝗔 😵𝗦𝗧𝗢𝗣𝗘𝗗 🌷 ...**"
    )


@Client.on_message(commandpro(["reload", "refresh"]))
@errors
@authorized_users_only
async def admincache(client, message: Message):
    set(
        message.chat.id,
        (
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ),
    )

    await message.reply_photo(
                              photo="https://telegra.ph/file/ab23ee0880dd24f21affe.png",
                              caption="**💥 𝗕𝗛𝗔𝗧𝗔𝗞𝗧𝗜_𝗠𝗨𝗦𝗜𝗖🔈🤞\n🥀 𝗡𝗢𝗪 🔥 𝗣𝗘𝗟𝗢𝗔𝗗𝗘𝗗 𝗗𝗢𝗡𝗘 ⚜️ ...**"
    )
