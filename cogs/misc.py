import discord
from discord.ext import commands
import random

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command(aliases=['gh'])
    async def github(self, ctx):
        # await ctx.send("closed source for now bb")
        await ctx.send("Catch! --> <https://github.com/lienne/ModiBot>")

    @commands.command()
    async def why(self, ctx):
        await ctx.send("Everyone always asks why is Modibot, no one ever asks how is Modibot :pensive:")

    @commands.command()
    async def what(self, ctx):
        await ctx.send("bro idk")

    @commands.command()
    async def who(self, ctx):
        responses = [
            '...let the dogs out! WHO WHO WHO WHO WHO!',
            '...stole the cookie from my cookie jar?',
            '...ate my ramen?!',
            '...likes shorts? I like shorts!'
        ]
        
        response = random.choice(responses)
        await ctx.send(response)

    @commands.command()
    async def tutorial(self, ctx):
        await ctx.send("<https://www.youtube.com/watch?v=1cuhODT6MGM>")

async def setup(bot):
    await bot.add_cog(Misc(bot))