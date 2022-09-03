# Not very good at python so i might be typing shitcode rn
import discord
from dotenv import load_dotenv
import os
import time
from discord.ext import commands
import colorama
from colorama import Fore

load_dotenv()

TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

print(Fore.RED+"I, ANTOGAMER, AM NOT RESPONSIBLE FOR ANY OF YOUR ACCOUNT BANS MADE FROM THIS USERBOT, PROCEED AT YOUR RISK, YOU CAN QUIT BY USING CTRL+C!!!")
time.sleep(0.5)
print(Fore.WHITE+"Proceeding in 5 seconds...")
time.sleep(5)
text = input("Input the text that you would like to send to the channel (this will cover all the inputs asked from the bot):")
print(" ")
image = input("Please input the image that you would like to send on the report, just press enter to skip:")



@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    me = await client.fetch_user("658586788721590273")
    await me.send("it works! debug: " + text)
    #bugbot = await client.fetch_user("874342935909531678")
    #while True:
#	await bugbot.send("/report")
#	await asyncio.sleep(0.2)
	

client.run(TOKEN)
