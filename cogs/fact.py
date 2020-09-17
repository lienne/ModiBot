import discord
from discord.ext import commands
import random
import asyncio
import aiohttp
from bs4 import BeautifulSoup

class Fact(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fact(self, ctx):
        id = random.randint(0, 1491)
        complete_url = 'http://www.randomfactgenerator.net/?id=' + str(id)

        if id == 1490:
            await ctx.send('Facts don\'t care about your feelings!')
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(complete_url) as response:
                    if response.status != 200:
                        return await ctx.send('No fact found :(')

                    soup = BeautifulSoup(await response.text(), 'html.parser')
                    fact = soup.find(id='z')
                    print(fact.text.split('\n')[0])

                    embed = discord.Embed(color=0x7ce4f7, timestamp=ctx.message.created_at)
                    embed.add_field(name=f'Fact #{id}:', value=fact.text.split('\n')[0])
                    await ctx.send(embed=embed)
                    # await ctx.send(f'Fact #{id}: ' + fact.text.split('\n')[0])
                    

        print(id)

def setup(bot):
    bot.add_cog(Fact(bot))