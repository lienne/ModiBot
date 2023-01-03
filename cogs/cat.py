import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import aiohttp

class Cat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['catto', 'hamb'])
    async def cat(self, ctx):
        complete_url = 'https://api.thecatapi.com/v1/images/search'

        async with aiohttp.ClientSession() as session:
            async with session.get(complete_url) as response:
                if response.status != 200:
                    return await ctx.send('No cat found :(')

                x = await response.json()

                embed = discord.Embed(title='Random Cat', color=0x7ce4f7, timestamp=ctx.message.created_at)
                embed.set_image(url=x[0]['url'])

                await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Cat(bot))