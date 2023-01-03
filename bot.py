import os
import logging
import random
import discord
import asyncio
import builtins

from dotenv import load_dotenv
from discord.ext import commands
from typing import Literal, Optional
from discord.ext.commands import Greedy, Context

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = '!', activity = discord.Game('with the discord API!'), intents=intents)
bot.remove_command('help')
builtins.bot = bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

discord.utils.setup_logging(level=logging.INFO, root=False)

logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has joined the chat!')

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(
    ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
        if not guilds:
            if spec == "~":
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "*":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "^":
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
                synced = []
            else:
                synced = await ctx.bot.tree.sync()

            await ctx.send(
                f"Synced {len(synced)} commands {'globally.' if spec is None else 'to the current guild.'}"
            )
            return

        ret = 0
        for guild in guilds:
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException:
                pass
            else:
                ret += 1

        await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

async def main():
    @bot.command()
    async def load(ctx, extension):
        await bot.load_extension(f'cogs.{extension}')

    @bot.command()
    async def unload(ctx, extension):
        await bot.unload_extension(f'cogs.{extension}')

    @bot.command()
    async def reload(ctx, extension):
        await bot.unload_extension(f'cogs.{extension}')
        await bot.load_extension(f'cogs.{extension}')

    async with bot:
        # Load all files in cogs folder (remove '.py' from filename when loading)
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')

        await bot.start(TOKEN)

asyncio.run(main())