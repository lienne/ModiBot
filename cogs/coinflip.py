import discord
from discord.ext import commands
import random

class Coinflip(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['flip'])
    async def coinflip(self, ctx):
        if ctx.author == bot.user:
            return

        flip = random.randint(0, 1)

        if flip == 0:
            await ctx.send(f'{ctx.author.display_name}, you got Heads.')
        else:
            await ctx.send(f'{ctx.author.display_name}, you got Tails.')



def setup(bot):
    bot.add_cog(Coinflip(bot))