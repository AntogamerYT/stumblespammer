# Not very good at python so i might be typing shitcode rn
import discord
from discord.ext import commands
from dotenv import load_dotenv
from io import BytesIO
import requests
import asyncio
import os
import time
import colorama
from colorama import Fore
from PIL import Image

load_dotenv()


TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

print(Fore.RED+"I, ANTOGAMER, AM NOT RESPONSIBLE FOR ANY OF YOUR ACCOUNT BANS MADE FROM THIS USERBOT, PROCEED AT YOUR RISK, YOU CAN QUIT BY USING CTRL+C!!!")
time.sleep(0.5)
print(Fore.WHITE+"Proceeding in 5 seconds...")
time.sleep(5)
text = input("Input the text that you would like to send to the channel (this will cover all the inputs asked from the bot):")

while text == "":
	text = input("Please input some text to continue:")

print(" ")
image = input("Please input the image that you would like to send on the report, just press enter to skip:")

def checkifimage(link):
	try:
	 req = requests.get(link)
	 if req.headers["content-type"] == "image/png" or req.headers["content-type"] == "image/jpeg" or req.headers["content-type"] == "image/jpg" or req.headers["content-type"] == "image/gif" or req.headers["content-type"] == "image/webp" or req.headers["content-type"] == "image/bmp":
	  return True
	 else:
	  return False
	except:
		return False

while checkifimage(image) == False and image != "":
	image = input("Please input a valid image link:")
@client.event
async def on_ready():
		print(f'Logged in as {client.user} (ID: {client.user.id})')
		bugbot = await client.fetch_user("874342935909531678")
		counter = 0
		while True:
		 await bugbot.send("/report")
		 await asyncio.sleep(0.2)
		 await bugbot.send("YES")
		 await asyncio.sleep(0.3)
		 await bugbot.send(text)
		 await asyncio.sleep(0.3)
		 await bugbot.send(text)
		 await asyncio.sleep(0.3)
		 await bugbot.send(text)
		 await asyncio.sleep(0.3)
		 await bugbot.send(text)
		 await asyncio.sleep(0.3)
		 if image != "":
			 await bugbot.send(image)
		 else:
			 await bugbot.send("no")
		 counter = counter+1
		 print(f"Completed {counter} bug report(s), going to the next one in 3 seconds!")
		 await asyncio.sleep(3)
	

client.run(TOKEN)
