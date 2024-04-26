import pymongo
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import ChatMember
from pyrogram import *
import asyncio
import psutil
import traceback
from pyrogram.types import *
import requests
import os, time
from datetime import datetime
import pytz
import random



import os
import openai
import uptime
import datetime
import pythonping
import psutil
import time 
import speedtest

# Bot API Token
API_TOKEN = ''
API_ID =''
API_HASH =''
# OpenAI API Key
openai.api_key = ""
#Only owner id
DEVIL = "1965898154"
# MongoDB setup
MONGODB_URI = ""  # Set your MongoDB connection string here
client = pymongo.MongoClient(MONGODB_URI)
db = client["wormgpt"]
collection = db["allowed_users"]
allowed_users = ["K_HACKER_ANONYMOUS", ""]
owners = ["K_HACKER_ANONYMOUS", ""]

for user in collection.find({}):
    allowed_users.append(user["telegram_username"])

# Define a function to check if a user is an owner
def is_owner(username):
    return username in owners

async def synchronize_time():
    await app.get_me()

    asyncio.run(synchronize_time())
# Create a Pyrogram Client
app = Client(
    "my_bot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = API_TOKEN
)

def get_total_cpu_usage():
    with open('/proc/stat') as file:
        line = file.readline()
        cpu_stats = line.split()
        total_cpu_time = sum(int(cpu) for cpu in cpu_stats[1:])
        idle_cpu_time = int(cpu_stats[4])
        return 100.0 * (1 - idle_cpu_time / total_cpu_time)
    
def get_total_cpu_usage():
    return psutil.cpu_percent(interval=1)

bot_start_time = datetime.datetime.now()


def get_server_uptime():
    uptime_seconds = psutil.boot_time()
    return time.time() - uptime_seconds
# Function to ping a server
def ping_server(host):
    return pythonping.ping(host, count=4) 
 # You can change the count as needed

def get_bot_cpu_usage():
    bot_process = psutil.Process(os.getpid())
    return bot_process.cpu_percent(interval=1)

def get_response(msg):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=msg,
        max_tokens=3500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return completion.choices[0].text

    
@app.on_message(filters.command(['code']))
def cod3(_,message):
    if message.from_user.username in allowed_users:
        question = message.text[len("/code"):]
        if len(question) == 0:
            message.reply( "❗𝚂𝚎𝚗𝚍 𝙻𝚒𝚔𝚎 𝚃𝚑𝚒𝚜: /code 𝚈𝚘𝚞𝚛 𝚀𝚞𝚎𝚜𝚝𝚒𝚘𝚗")
        else:
            answer = get_response(question+",use markdown to  identify the code ")
            message.reply( answer)
            cdd = answer.split('``')[1]
            with open('Your-Code.txt','w') as f:
                f.write(cdd)
            message.reply_document('Your-Code.txt',caption='**𝙀𝙭𝙘𝙚𝙧𝙘𝙞𝙨𝙚 𝙇𝙚𝙛𝙩 😈**\n1.Save This Code 💾 \n2.Run The Code 🛠 \n3.In Your Best IDE 💻 \n💠 ＷＯＲＭ ＧＰＴ')
        
   
    else:
        message.reply( "❌ 𝚂𝚘𝚛𝚛𝚢, 𝚢𝚘𝚞 𝚊𝚛𝚎 𝚗𝚘𝚝 𝚊𝚞𝚝𝚑𝚘𝚛𝚒𝚣𝚎𝚍 𝚝𝚘 𝚋𝚘𝚝 \n🌟 𝙱𝚞𝚢 𝙱𝚘𝚝 𝙵𝚛𝚘𝚖 @DARK_WORM_GPT_A")
        

@app.on_message(filters.command("start"))
def start_bot(client, message):
    # Create an InlineKeyboardMarkup with the "Start" button
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="❇ Support NetWork ❇", url=f"https://t.me/DARK_WORM_GPT_AI"),
            ],
            [
                InlineKeyboardButton(text="💠 Creator Of Bot 💠", url=f"https://t.me/K_HACKER_ANONYMOUS"),
            ],
            [
                InlineKeyboardButton(text="🔰 Buy WormGPT 🔰", callback_data="help"),
                InlineKeyboardButton(text="💻 About WormGPT 💻", callback_data="about"),
            ],
            [
             InlineKeyboardButton(text="💠 WormGPT Ai Dev 💠", callback_data="admin"),
             InlineKeyboardButton(text="🌟 User Commands 🌟", callback_data="auth"),
            ],
        ]
    )

    start_message = app.send_message(
        message.chat.id,
        """💕 𝙷𝚎𝚕𝚕𝚘 𝚂𝚒𝚛 ❗ 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝚃𝚘 𝚆𝚘𝚛𝚖 𝙶𝙿𝚃 𝙰𝚒 ! 𝙿𝚕𝚎𝚊𝚜𝚎 Click On The Bot User Commands Button 𝙵𝚘𝚛 𝚂𝚎𝚎 𝙵𝚎𝚊𝚝𝚞𝚛𝚎𝚜""",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("auth"))
def auth_callback(client, callback_query):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⬅️", callback_data="back"),
            ],
        ]
    )

    app.send_message(
        callback_query.message.chat.id,
        """
✅ 𝚃𝚑𝚎𝚛𝚎 𝚊𝚛𝚎 𝚊𝚕𝚕 𝚌𝚖𝚍𝚜 𝚊𝚞𝚝𝚑 𝚞𝚜𝚎𝚛𝚜

✅ 𝙳𝚒𝚛𝚎𝚌𝚝𝚕𝚢 𝙰𝚜𝚔 𝚀𝚞𝚎𝚜𝚝𝚒𝚘𝚗𝚜 

✅ 𝙵𝚘𝚛 𝙲𝚘𝚍𝚎 𝙴𝚡𝚙𝚕𝚊𝚗𝚊𝚝𝚒𝚘𝚗 𝙰𝚗𝚍 𝙲𝚘𝚍𝚎 𝙵𝚒𝚕𝚎 𝚄𝚙𝚕𝚘𝚊𝚍 𝚄𝚜𝚎

✅ /code : 𝚀𝚞𝚎𝚜𝚝𝚒𝚘𝚗......

        """,
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("admin"))
def admin_callback(client, callback_query):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⬅️", callback_data="back"),
            ],
        ]
    )

    app.send_message(
        callback_query.message.chat.id,
        """
🌟 𝙳𝙰𝚁𝙺 𝚆𝙾𝚁𝙼 𝙶𝙿𝚃 𝙰𝙸 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 🌟 

💠 𝕄𝔸𝕀ℕ 𝔻𝔼𝕍 :- @K_HACKER_ANONYMOUS 


        """,
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("about"))
def about_callback(client, callback_query):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
         
            [
                InlineKeyboardButton(text="⬅️", callback_data="back"),
            ],
        ]
    )

    app.send_message(
        callback_query.message.chat.id,
        """
𝘼𝙣 𝙚𝙫𝙞𝙡 𝘾𝙝𝙖𝙩𝙂𝙋𝙏-𝙡𝙞𝙠𝙚 𝘼𝙄 𝙢𝙤𝙙𝙚𝙡 𝙞𝙨 𝙨𝙥𝙧𝙚𝙖𝙙𝙞𝙣𝙜 𝙖𝙘𝙧𝙤𝙨𝙨 𝙩𝙝𝙚 𝙙𝙖𝙧𝙠 𝙬𝙚𝙗 𝙖𝙣𝙙 𝙚𝙣𝙖𝙗𝙡𝙞𝙣𝙜 𝙝𝙖𝙘𝙠𝙚𝙧𝙨 𝙩𝙤 𝙥𝙚𝙧𝙛𝙤𝙧𝙢 𝙘𝙮𝙗𝙚𝙧𝙖𝙩𝙩𝙖𝙘𝙠𝙨 𝙤𝙣 𝙖 𝙣𝙚𝙫𝙚𝙧-𝙗𝙚𝙛𝙤𝙧𝙚-𝙨𝙚𝙚𝙣 𝙨𝙘𝙖𝙡𝙚


𝙏𝙚𝙭𝙩𝙎𝙤𝙛𝙞𝙖 𝙈𝙖𝙝𝙞𝙧𝙤𝙫𝙖 
𝙄𝙣 𝙢𝙤𝙧𝙚 𝘼𝙄-𝙧𝙚𝙡𝙖𝙩𝙚𝙙 𝙙𝙤𝙤𝙢𝙨𝙖𝙮𝙚𝙧 𝙣𝙚𝙬𝙨, 𝙖 𝘾𝙝𝙖𝙩𝙂𝙋𝙏-𝙨𝙩𝙮𝙡𝙚 𝘼𝙄 𝙩𝙤𝙤𝙡 𝙞𝙨 𝙩𝙖𝙠𝙞𝙣𝙜 𝙤𝙛𝙛 𝙖𝙘𝙧𝙤𝙨𝙨 𝙘𝙮𝙗𝙚𝙧𝙘𝙧𝙞𝙢𝙚 𝙛𝙤𝙧𝙪𝙢𝙨 𝙤𝙣 𝙩𝙝𝙚 𝙙𝙖𝙧𝙠 𝙬𝙚𝙗. 𝘾𝙖𝙡𝙡𝙚𝙙 𝙒𝙤𝙧𝙢𝙂𝙋𝙏, 𝙩𝙝𝙚 “𝙨𝙤𝙥𝙝𝙞𝙨𝙩𝙞𝙘𝙖𝙩𝙚𝙙 𝘼𝙄 𝙢𝙤𝙙𝙚𝙡” 𝙞𝙨 𝙙𝙚𝙨𝙞𝙜𝙣𝙚𝙙 𝙩𝙤 𝙥𝙧𝙤𝙙𝙪𝙘𝙚 𝙝𝙪𝙢𝙖𝙣-𝙡𝙞𝙠𝙚 𝙩𝙚𝙭𝙩 𝙩𝙝𝙖𝙩 𝙘𝙖𝙣 𝙗𝙚 𝙪𝙨𝙚𝙙 𝙞𝙣 𝙝𝙖𝙘𝙠𝙞𝙣𝙜 𝙘𝙖𝙢𝙥𝙖𝙞𝙜𝙣𝙨, 𝙚𝙣𝙖𝙗𝙡𝙞𝙣𝙜 𝙝𝙖𝙘𝙠𝙚𝙧𝙨 𝙩𝙤 𝙥𝙚𝙧𝙛𝙤𝙧𝙢 𝙖𝙩𝙩𝙖𝙘𝙠𝙨 𝙤𝙣 𝙖 𝙣𝙚𝙫𝙚𝙧-𝙗𝙚𝙛𝙤𝙧𝙚-𝙨𝙚𝙚𝙣 𝙨𝙘𝙖𝙡𝙚.

“𝙏𝙝𝙞𝙨 𝙩𝙤𝙤𝙡 𝙥𝙧𝙚𝙨𝙚𝙣𝙩𝙨 𝙞𝙩𝙨𝙚𝙡𝙛 𝙖𝙨 𝙖 𝙗𝙡𝙖𝙘𝙠𝙝𝙖𝙩 𝙖𝙡𝙩𝙚𝙧𝙣𝙖𝙩𝙞𝙫𝙚 𝙩𝙤 𝙂𝙋𝙏 𝙢𝙤𝙙𝙚𝙡𝙨, 𝙙𝙚𝙨𝙞𝙜𝙣𝙚𝙙 𝙨𝙥𝙚𝙘𝙞𝙛𝙞𝙘𝙖𝙡𝙡𝙮 𝙛𝙤𝙧 𝙢𝙖𝙡𝙞𝙘𝙞𝙤𝙪𝙨 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙞𝙚𝙨,” 𝙨𝙚𝙘𝙪𝙧𝙞𝙩𝙮 𝙧𝙚𝙨𝙚𝙖𝙧𝙘𝙝𝙚𝙧 𝘿𝙖𝙣𝙞𝙚𝙡 𝙆𝙚𝙡𝙡𝙚𝙮 𝙨𝙖𝙞𝙙 𝙬𝙧𝙤𝙩𝙚 𝙤𝙣 𝘾𝙮𝙗𝙚𝙧𝙨𝙚𝙘𝙪𝙧𝙞𝙩𝙮 𝙨𝙞𝙩𝙚, 𝙎𝙡𝙖𝙨𝙝𝙣𝙚𝙭𝙩. “𝙒𝙤𝙧𝙢𝙂𝙋𝙏 𝙬𝙖𝙨 𝙖𝙡𝙡𝙚𝙜𝙚𝙙𝙡𝙮 𝙩𝙧𝙖𝙞𝙣𝙚𝙙 𝙤𝙣 𝙖 𝙙𝙞𝙫𝙚𝙧𝙨𝙚 𝙖𝙧𝙧𝙖𝙮 𝙤𝙛 𝙙𝙖𝙩𝙖 𝙨𝙤𝙪𝙧𝙘𝙚𝙨, 𝙥𝙖𝙧𝙩𝙞𝙘𝙪𝙡𝙖𝙧𝙡𝙮 𝙘𝙤𝙣𝙘𝙚𝙣𝙩𝙧𝙖𝙩𝙞𝙣𝙜 𝙤𝙣 𝙢𝙖𝙡𝙬𝙖𝙧𝙚-𝙧𝙚𝙡𝙖𝙩𝙚𝙙 𝙙𝙖𝙩𝙖.”

𝙒𝙝𝙖𝙩 𝙙𝙤𝙚𝙨 𝙩𝙝𝙞𝙨 𝙢𝙚𝙖𝙣 𝙛𝙤𝙧 𝙩𝙝𝙚 𝙧𝙚𝙨𝙩 𝙤𝙛 𝙪𝙨? 𝙀𝙨𝙨𝙚𝙣𝙩𝙞𝙖𝙡𝙡𝙮 𝙞𝙩 𝙗𝙤𝙞𝙡𝙨 𝙙𝙤𝙬𝙣 𝙩𝙤 𝙩𝙝𝙚 𝙨𝙥𝙚𝙚𝙙 𝙖𝙣𝙙 𝙣𝙪𝙢𝙗𝙚𝙧 𝙤𝙛 𝙨𝙘𝙖𝙢𝙨 𝙖 𝙡𝙖𝙣𝙜𝙪𝙖𝙜𝙚 𝙢𝙤𝙙𝙚𝙡 𝙘𝙖𝙣 𝙜𝙚𝙣𝙚𝙧𝙖𝙩𝙚 𝙖𝙩 𝙤𝙣𝙘𝙚, 𝙬𝙝𝙞𝙘𝙝 𝙞𝙨 𝙤𝙗𝙫𝙞𝙤𝙪𝙨𝙡𝙮 𝙬𝙤𝙧𝙧𝙮𝙞𝙣𝙜 𝙬𝙝𝙚𝙣 𝙮𝙤𝙪 𝙘𝙤𝙣𝙨𝙞𝙙𝙚𝙧 𝙝𝙤𝙬 𝙛𝙖𝙨𝙩 𝙡𝙖𝙣𝙜𝙪𝙖𝙜𝙚 𝙢𝙤𝙙𝙚𝙡𝙨 𝙘𝙖𝙣 𝙜𝙚𝙣𝙚𝙧𝙖𝙩𝙚 𝙩𝙚𝙭𝙩. 𝙏𝙝𝙞𝙨 𝙢𝙖𝙠𝙚𝙨 𝙘𝙮𝙗𝙚𝙧𝙖𝙩𝙩𝙖𝙘𝙠𝙨 𝙨𝙪𝙘𝙝 𝙖𝙨 𝙥𝙝𝙞𝙨𝙝𝙞𝙣𝙜 𝙚𝙢𝙖𝙞𝙡𝙨 𝙥𝙖𝙧𝙩𝙞𝙘𝙪𝙡𝙖𝙧𝙡𝙮 𝙚𝙖𝙨𝙮 𝙩𝙤 𝙧𝙚𝙥𝙡𝙞𝙘𝙖𝙩𝙚 𝙬𝙝𝙚𝙣 𝙥𝙪𝙩 𝙞𝙣 𝙩𝙝𝙚 𝙝𝙖𝙣𝙙𝙨 𝙤𝙛 𝙚𝙫𝙚𝙣 𝙖 𝙣𝙤𝙫𝙞𝙘𝙚 𝙘𝙮𝙗𝙚𝙧𝙘𝙧𝙞𝙢𝙞𝙣𝙖𝙡.

💠 𝕄𝔸𝕀ℕ 𝔻𝔼𝕍 :- @K_HACKER_ANONYMOUS

        """,
        reply_markup=keyboard)



@app.on_callback_query(filters.regex("help"))
def help_callback(client, callback_query):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💠 𝙱𝚞𝚢 𝙱𝚘𝚝 𝙰𝚞𝚝𝚑 𝙵𝚛𝚘𝚖 𝙾𝚠𝚗𝚎𝚛 💠", url="https://t.me/K_HACKER_ANONYMOUS"),
            ],
            [
                InlineKeyboardButton(text="⬅️", callback_data="back"),
            ],
        ]
    )

    app.send_message(
        callback_query.message.chat.id,
        """
🌟 𝙸𝚏 𝚈𝚘𝚞 𝙽𝚎𝚎𝚍 𝙱𝚘𝚝 𝙰𝚞𝚝𝚑 🌟
        """,
        reply_markup=keyboard
    )
@app.on_callback_query(filters.regex("back"))
def back_to_start_callback(client, callback_query):
    # Return to the "/start" command
    start_bot(client, callback_query.message)
    
@app.on_message(filters.command("admin"))
def admin(client, message):
    if message.from_user.username in owners:
        app.send_message(message.chat.id, """\
💠 𝙰𝙳𝙼𝙸𝙽 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 💠

/addauth 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 (𝙵𝚘𝚛 𝙰𝚍𝚍 𝚄𝚜𝚎𝚛𝚜) ❇
/rmauth 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 (𝙵𝚘𝚛 𝚁𝚎𝚖𝚘𝚟𝚎 𝚄𝚜𝚎𝚛𝚜) ❇

𝙿𝚄𝚃 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 @ 

/broadcast (𝙵𝚘𝚛 𝙱𝚛𝚘𝚊𝚍𝚌𝚊𝚜𝚝 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝚃𝚘 𝙰𝚕𝚕 𝚄𝚜𝚎𝚛𝚜) ❇

/authlist (𝙵𝚘𝚛 𝚂𝚎𝚎 𝙰𝚕𝚕 𝙰𝚞𝚝𝚑𝚘𝚛𝚒𝚣𝚎𝚍 𝚄𝚜𝚎𝚛𝚜) ❇
""")


@app.on_message(filters.command("addauth"))
def add_authorized_user(client, message):
    if message.from_user.username in owners:
        user_to_add = message.text[len("/addauth "):].strip()
        if len(user_to_add) == 0:
            app.send_message(message.chat.id, "⚠️ 𝚂𝚎𝚗𝚍 𝙻𝚒𝚔𝚎 𝚃𝚑𝚒𝚜: /addauth NewUserUsername")
        else:
            if user_to_add not in allowed_users:
                allowed_users.append(user_to_add)
                if collection.find_one({"telegram_username": user_to_add}) is None:
                    # Add the user to MongoDB collection
                    collection.insert_one({"telegram_username": user_to_add})
                app.send_message(message.chat.id, f"🌟 𝚄𝚜𝚎𝚛 {user_to_add} 𝚑𝚊𝚜 𝚋𝚎𝚎𝚗 𝚊𝚞𝚝𝚑𝚘𝚛𝚒𝚣𝚎𝚍 𝚝𝚘 𝚞𝚜𝚎 𝚝𝚑𝚒𝚜 𝚋𝚘𝚝.")
            else:
                app.send_message(message.chat.id, f"🔁 𝚄𝚜𝚎𝚛 {user_to_add} 𝚒𝚜 𝚊𝚕𝚛𝚎𝚊𝚍𝚢 𝚊𝚞𝚝𝚑𝚘𝚛𝚒𝚣𝚎𝚍.")
    else:
        app.send_message(message.chat.id, "❌ 𝚂𝚘𝚛𝚛𝚢, 𝚢𝚘𝚞 𝚊𝚛𝚎 𝚗𝚘𝚝 𝚊𝚗 𝚘𝚠𝚗𝚎𝚛 𝚝𝚘 𝚞𝚜𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 /alive use alive check")

@app.on_message(filters.command("rmauth"))
def remove_authorized_user(client, message):
    if message.from_user.username in owners:
        user_to_remove = message.text[len("/rmauth "):].strip()
        if len(user_to_remove) == 0:
            app.send_message(message.chat.id, "⚠ 𝚂𝚎𝚗𝚍 𝙻𝚒𝚔𝚎 𝚃𝚑𝚒𝚜: /rmauth UserToRemoveUsername")
        else:
            if user_to_remove in allowed_users:
                allowed_users.remove(user_to_remove)
                # Remove the user from the MongoDB collection if it exists
                collection.delete_one({"telegram_username": user_to_remove})
                app.send_message(message.chat.id, f"🚫 𝚄𝚜𝚎𝚛 {user_to_remove} 𝚑𝚊𝚜 𝚋𝚎𝚎𝚗 𝚛𝚎𝚖𝚘𝚟𝚎𝚍 𝚏𝚛𝚘𝚖 𝚊𝚞𝚝𝚑𝚘𝚛𝚒𝚣𝚎𝚍 𝚞𝚜𝚎𝚛𝚜.")
            else:
                app.send_message(message.chat.id, f"⚠️ 𝚄𝚜𝚎𝚛 {user_to_remove} 𝚒𝚜 𝚗𝚘𝚝 𝚒𝚗 𝚝𝚑𝚎 𝚕𝚒𝚜𝚝 𝚘𝚏 𝚊𝚞𝚝𝚑𝚘𝚛𝚒𝚣𝚎𝚍 𝚞𝚜𝚎𝚛𝚜.")

# All auth lists users -----
@app.on_message(filters.command("authlist") & filters.user(owners))
def list_authorized_users(client, message):
    if message.from_user.username in owners:
        user_list = "\n💠 Verified @".join(allowed_users)
        app.send_message(message.chat.id, f"💠 𝙻𝚒𝚜𝚝 𝙾𝚏 𝙰𝚕𝚕 𝙰𝚞𝚝𝚑𝚘𝚛𝚒𝚣𝚎𝚍 𝚄𝚜𝚎𝚛𝚜 💠 :\n❄ All Active Users ❄ \n✅ Verified List ✅ \n💠 Verified @{user_list}")



# Broadcast message to all users
def broadcast_message(message_text):
    for user in allowed_users:
        try:
            app.send_message(user, message_text)
        except Exception as e:
            print(f"❌ 𝙵𝚊𝚒𝚕𝚎𝚍 𝚝𝚘 𝚜𝚎𝚗𝚍 𝚝𝚑𝚎 𝚋𝚛𝚘𝚊𝚍𝚌𝚊𝚜𝚝 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝?? {user}. Error: {str(e)}")

# Handle '/broadcast' command (for owners)
@app.on_message(filters.command("broadcast") & filters.user(owners))
def broadcast_message_command(client, message):
    # Check if the message has a text following the command
    if len(message.command) < 2:
        app.send_message(
            message.chat.id,
            "📤 𝚂𝚎𝚗𝚍 𝚊 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝𝚘 𝚋𝚎 𝚋𝚛𝚘𝚊𝚍𝚌𝚊𝚜𝚝𝚎𝚍 𝚊𝚜 𝚊 𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚝𝚑𝚎 /broadcast 𝚌𝚘𝚖𝚖𝚊𝚗𝚍.",
        )
    else:
        # Extract the message to be broadcasted
        broadcast_text = message.text.split(" ", 1)[1]

        broadcast_message(broadcast_text)

# Update 'allowed_users' list from the MongoDB collection
for user in collection.find({}):
    allowed_users.append(user['telegram_username'])

@app.on_message(filters.command("alive"))
def get_uptime(client, message):
    uptime_seconds = get_server_uptime()
    uptime_str = str(datetime.timedelta(seconds=uptime_seconds))
    total_cpu = get_total_cpu_usage()
    current_cpu = get_bot_cpu_usage()
    bot_alive_time = str(datetime.datetime.now() - bot_start_time)  # Calculate bot's uptime using bot_start_time

    alive_message = (
        f"✅ Server Uptime: {uptime_str}\n"
        f"✅ Total CPU Usage: {total_cpu:.2f}%\n"
        f"✅ Current Bot CPU Usage: {current_cpu:.2f}%\n"
        f"✅ Bot Alive Time: {bot_alive_time}"
    )

    app.send_message(message.chat.id, alive_message)
@app.on_message(filters.text)
def send_answer(client, message):
    if message.from_user.username in allowed_users:
        app.send_message(message.chat.id, get_response(message.text))
    else:
        app.send_message(message.chat.id, "❌ 𝚂𝚘𝚛𝚛𝚢, 𝚢𝚘𝚞 𝚊𝚛𝚎 𝚗𝚘𝚝 𝚊𝚞𝚝𝚑𝚘𝚛𝚒𝚣𝚎𝚍 𝚝𝚘 𝚋𝚘𝚝 \n🌟 𝙱𝚞𝚢 𝙱𝚘𝚝 𝙵𝚛𝚘𝚖 @DARK_WORM_GPT_AI")

@app.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==DEVIL:
        fwded_mesg = await message.forward(chat_id=DEVIL, disable_notification=True)
        
print(f"Dark Worm Gpt Bot Is Active Now ✅")      
app.run()
