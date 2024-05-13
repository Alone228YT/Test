from utils.emojis import emojis

_emoji = emojis["ℹ️"]
__info__ = f"""{_emoji} Test module"""
__version__ = """1.10"""
__author__ = """Alone"""
__releaseDate__ = """12.05.2024"""
__lastUpdate__ = """13.05.2024"""
__commands__ = """
<code>.test</code> - checks the operation of the module
<code>!text!</code> - makes text uppercase
<code>.rn number1 - number2</code> - selects a random number
"""

__fullInfo__ = f"""
{__info__} <i>(by {__author__})</i>
<b>Version</b> <code>{__version__}</code>
<b>Release date:</b> <code>{__releaseDate__}</code>
<b>Last update:</b> <code>{__lastUpdate__}</code>
<b>Commands:</b>
{__commands__}
"""