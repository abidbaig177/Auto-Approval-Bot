from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

bot=Client(
    "Auto Approval Bot",
    bot_token = environ["BOT_TOKEN"],
    api_id = int(environ["API_ID"]),
    api_hash = environ["API_HASH"]
)
ccaption = """\n\n<b><i>⚜️ To Join Click here
⭐️ @honeybeemovies
⭐️ @AmazonPrime_Orginal ✅
⭐️ @honeybeemoviesgroup1 
⭐️ @MalluFlix 🧲
    🅷🅾️🅽🅴🆈 🅱️🅴🅴 🅼🅾️🆅🅸🅴🆂 </b></i>"""

ccaption2 = """\n<b><i>⚜️ Join    @h4hbm</b></i>"""
CHAT_ID = [int(bot) for bot in environ.get("CHAT_ID", None).split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYou are Approved")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

@bot.on_message(filters.private & filters.command(["start"]))
async def start(client: bot, message: Message):
    await client.send_message(chat_id=message.chat.id, text=f"**__Im an auto approval bot for telegram__**",reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Repository", url="https://github.com/akhilbaiju/Auto-Approval-Bot" )]]
        ))
    
    
@bot.on_chat_join_request(filters.group | filters.channel)
async def approve(client, message: ChatJoinRequest):
    chat=message.chat 
    user=message.from_user
    try:
        await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    except Exception as e:
        await client.send_message(chat_id=chat.id,text={e})
        
@bot.on_message(filters.group, group=1)
async def caption2(client, message):
    grp=message.chat.id
    if grp==-1001574333947:
        ogcap=message.caption
        if ogcap==None:
            newcap=ccaption
        else:
            newcap="<b><i>"+str(ogcap)+"</b></i>"+ccaption
        await message.copy(message.chat.id, caption=newcap)
    else:
        ogcap=message.caption
        if ogcap==None:
            newcap="."+ccaption2
        else:
            newcap="<b><i>"+str(ogcap)+"\n</b></i>"+ccaption2
        await message.copy(message.chat.id, caption=newcap)
bot.run()
