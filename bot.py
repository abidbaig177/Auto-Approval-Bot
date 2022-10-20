from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

bot=Client(
    "Auto Approval Bot",
    bot_token = environ["BOT_TOKEN"],
    api_id = int(environ["API_ID"]),
    api_hash = environ["API_HASH"]
)

CHAT_ID = [int(bot) for bot in environ.get("CHAT_ID", None).split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYou are Approved")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

@bot.on_message(filters.private & filters.command(["start"]))
async def start(client: bot, message: Message):
    await client.send_message(chat_id=message.chat.id, text=f"**__Ok da 🙄__**")

@bot.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def approve(client: bot, message: ChatJoinRequest):
    chat=message.chat
    user=message.from_user
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))

bot.run()
