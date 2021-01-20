import discord
from discord.ext import commands
import random

class Diceroll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['roll', 'dice'])
    async def diceroll(self, ctx):
        if ctx.author == bot.user:
            return

        roll = random.randint(1,6)

        await ctx.send(f'{ctx.author.display_name}, you rolled a {roll}.')

def setup(bot):
    bot.add_cog(Diceroll(bot))