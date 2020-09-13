import os
import logging
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import builtins

bot = commands.Bot(command_prefix = '.')
bot.remove_command('help')
builtins.bot = bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
logger.addHandler(handler)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

# Load all files in cogs folder (remove '.py' from filename when loading)
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def change_presence():
    await bot.change_presence(status = discord.Status.online, activity = discord.Game('with the discord API!'))

@bot.event
async def on_ready():
    # await bot.change_presence(status = discord.Status.online, activity = discord.Game('with the discord API!'))
    print(f'{bot.user.name} has joined the chat!')

bot.run(TOKEN)