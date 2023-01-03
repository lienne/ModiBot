import discord
from discord.ext import commands
import random

class Spongebob(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['mock', 'sponge'])
    async def spongebob(self, ctx, *input):
        
        output = ""

        for word in input:
            for c in word:
                if c.isalpha():
                    if random.random() > 0.5:
                        output += c.upper()
                    else:
                        output += c.lower()

                else:
                    output += c

            output += " "

        await ctx.channel.send(output, file=discord.File('cogs/img/mocking-spongebob.jpg'))

async def setup(bot):
    await bot.add_cog(Spongebob(bot))