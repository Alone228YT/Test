from pyrogram import Client as app, filters
from filters import Text

@app.on_message(Text(startswith="!", endswith="!") & filters.me)
async def Alone228YT_Test_caps_text(app, msg):
	text = msg.text
	new_text = text.upper()
	await msg.edit(new_text[1:-1])