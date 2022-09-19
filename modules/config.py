# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝐁𝐢𝐤𝐚𝐬𝐡𝐇𝐚𝐥𝐝𝐞𝐫 @𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝐁𝐢𝐤𝐚𝐬𝐡𝐇𝐚𝐥𝐝𝐞𝐫 @𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫
API_HASH = getenv("API_HASH", "XXXXX")
API_ID = int(getenv("API_ID", "XXXXX"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXXXX")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "XXXXX")
BOT_IMAGE = getenv("BOT_IMAGE", "https://te.legra.ph/file/99d0261f0aa5512ad6753.jpg")
BOT_NAME = getenv("BOT_NAME", "XXXXX")
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
MONGODB_URL = getenv("MONGODB_URL", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
OWNER_NAME = getenv("OWNER_NAME", "𝙸𝚗𝚞𝚖𝚊𝚔𝚒")
OWNER_USERNAME = getenv("OWNER_USERNAME", "deniMG")
SOURCE_CODE = getenv("SOURCE_CODE", "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.tiktok.com%2Fapi%2Fimg%2F%3FitemId%3D7131339418996100379%26location%3D0%26aid%3D1988&imgrefurl=https%3A%2F%2Fwww.tiktok.com%2F%40ceilygemoy%2Fvideo%2F7131339418996100379&tbnid=izoPB6B4gfWksM&vet=1&docid=Qg-sZUcK8fFZkM&w=576&h=1024&itg=1&source=sh%2Fx%2Fim")
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1004299209").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.tiktok.com%2Fapi%2Fimg%2F%3FitemId%3D7131339418996100379%26location%3D0%26aid%3D1988&imgrefurl=https%3A%2F%2Fwww.tiktok.com%2F%40ceilygemoy%2Fvideo%2F7131339418996100379&tbnid=izoPB6B4gfWksM&vet=1&docid=Qg-sZUcK8fFZkM&w=576&h=1024&itg=1&source=sh%2Fx%2Fim")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.tiktok.com%2Fapi%2Fimg%2F%3FitemId%3D7131339418996100379%26location%3D0%26aid%3D1988&imgrefurl=https%3A%2F%2Fwww.tiktok.com%2F%40ceilygemoy%2Fvideo%2F7131339418996100379&tbnid=izoPB6B4gfWksM&vet=1&docid=Qg-sZUcK8fFZkM&w=576&h=1024&itg=1&source=sh%2Fx%2Fim")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝐁𝐢𝐤𝐚𝐬𝐡 𝐇𝐚𝐥𝐝𝐞𝐫) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/BikashDP")
