from .. import Bot
from telethon import events, Button

@Bot.on(events.NewMessage(incoming=True, pattern="/startbot"))
async def startbot(event):
    await event.reply("Telethon Working Fine ✅")

@Bot.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("Thanks For Using Bot")
