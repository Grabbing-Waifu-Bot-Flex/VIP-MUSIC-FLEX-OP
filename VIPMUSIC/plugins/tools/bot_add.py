import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import delete_served_chat
from VIPMUSIC.utils.database import get_assistant


photo = [
    "https://telegra.ph/file/d3489f64d0aceb81fd48a.jpg",
    "https://telegra.ph/file/ba2be6b1ffd937418f1be.jp",
    "https://telegra.ph/file/05f797444814774a07883.jpg",
    "https://telegra.ph/file/aca31398bf04ab0e0a02f.jpg",
    "https://telegra.ph/file/f5bf75d105391d4fdf249.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                )
                msg = (
                    f"**𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    f"**𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n"
                    f"**𝐂ʜᴀᴛ 𝐈ᴅ:** {message.chat.id}\n"
                    f"**𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @{username}\n"
                    f"**𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs:** {count}\n"
                    f"**𝐀ᴅᴅᴇᴅ 𝐁ʏ:** {message.from_user.mention}"
                )
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"𝐀ᴅᴅᴇᴅ 𝐁ʏ",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                )
                            ]
                        ]
                    ),
                )
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Error: {e}")
