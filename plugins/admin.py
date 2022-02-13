from pyrogram import Client, filters
import os
from plugins.helper.permissions import adminsOnly


@Client.on_message(filters.command("pin"))
@adminsOnly("can_pin_messages")
async def pin(_, message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()


@Client.on_message(filters.command("unpin"))
@adminsOnly("can_pin_messages")
async def unpin(_, message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
