from pyrogram import Client as app, filters
from filters import Text
from random import randint as rn
from utils.emojis import emojis
from utils.errors import custom_command_error

@app.on_message(Text(startswith=".rn", contains="-") & filters.me)
async def Alone228YT_Test_random_number(app, msg):
	try:
		text = msg.text[4:].strip()
		x = text.split(" - ")
		if len(x) == 1:
			return await custom_command_error(msg, ".rn number1 - number2")

		n = [int(x[0].split()[-1]), int(x[1].split()[0])]
		n.sort()
	except:
		return await custom_command_error(msg, ".rn number1 - number2")
	emoji = emojis["👀"]

	await msg.edit(f"{emoji} <b>Random number:</b> {rn(n[0], n[1])}")