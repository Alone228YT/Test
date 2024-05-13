from pyrogram import Client as app, filters
from utils.emojis import emojis

@app.on_message(filters.command("test", prefixes=".") & filters.me)
async def Alone228YT_Test_test(app, msg):
	emoji = emojis["✔️"]
	await msg.edit(f"{emoji} It works!")