#BHATAKTI_ATMA 

import os
import aiohttp
import asyncio
import json
import sys
import time
from youtubesearchpython import SearchVideos
from pyrogram import filters, Client
from yt_dlp import YoutubeDL
from yt_dlp.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)


@Client.on_message(filters.command("song") & ~filters.edited)
async def song(client, message):
    cap = "**๐ฅ ๐๐พ๐ฝ๐ถ๐ธ๐๐ฟ๐ป๐พ๐ฐ๐ณ๐ด๐ณ๐ฟ ๐ฑ๐โ\n๐ [๐ฑ๐ท๐ฐ๐๐ฐ๐บ๐๐ธ ๐ฎ๐ณ ๐ฐ๐๐ผ๐ฐ ๐ ๐ผ๐๐๐ธ๐ฒ](https://t.me/lovely_friends_2) ๐ท ...**"
    url = message.text.split(None, 1)[1]
    rkp = await message.reply("**๐ Sษษษคฦษฆษฉษณส ...**")
    if not url:
        await rkp.edit("**๐ฅ๐ฐ๐ฑ๐ฑ๐ด ๐ฑ๐ท๐ฐ๐ธ ๐๐ฐ ๐๐๐บ๐ธ ๐ฑ๐ท๐ด๐ฝ๐๐๐พ๐ฝ๐ถ๐๐บ๐ฐ๐ค\n๐ธ๐ฝ๐ฐ๐ฐ๐ผ๐ค๐ฑ๐๐ฐ๐ท ...**")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await rkp.edit("**โ ๐ฝ๐พ๐ธ ๐ฌ๐ผ๐ธ๐ป๐ฐ ๐๐ด ๐๐พ๐ฝ๐ถ ๐ผ๐๐น๐ท๐ด๐...**")
    type = "audio"
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        song = True
    try:
        await rkp.edit("**๐ ๐ฟ๐ป๐ด๐ฐ๐๐ด ๐๐ฐ๐ธ๐...**`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await rkp.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    time.time()
    if song:
        await rkp.edit("**๐ค ๐๐ฟ๐ป๐พ๐ฐ๐ณ๐ธ๐ฝ๐ถ ๐ท๐พ ๐๐ท๐ฐ ๐ท ...**"),
        lol = "./etc/tg_vc_bot.jpg"
        lel = await message.reply_audio(
                 f"{rip_data['id']}.mp3",
                 duration=int(rip_data["duration"]),
                 title=str(rip_data["title"]),
                 performer=str(rip_data["uploader"]),
                 thumb=lol,
                 caption=cap)
        await rkp.delete()
