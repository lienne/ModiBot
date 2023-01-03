import discord
from discord.ext import commands
import random

class KnightHacks(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gh'])
    async def github(self, ctx):
        # await ctx.send("closed source for now bb")
        await ctx.send("Catch! --> <https://github.com/lienne/ModiBot>")

    @commands.command()
    async def where(self, ctx):
        await ctx.send("right here :) \n**hopin:** <https://hopin.to/events/knight-hacks> "
                       "\n**day of:** <https://live.knighthacks.org/> "
                       "\n**hacker guide:** <https://www.knighthacks.org/guide> "
                       "\n**devpost:** <https://knight-hacks-2020-online.devpost.com/> ")

    @commands.command()
    async def how(self, ctx, *, text = None):
        if text is not None and text.lower() == 'is Modibot' or 'is Modibot?' or 'is ModiBot' or 'is ModiBot?':
            await ctx.send('awee thank you for asking!! <3')

        await ctx.send("<https://www.knighthacks.org/guide>")

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
            '...likes shorts? I like shorts!',
            '...is gonna win KnightHacks 2020?!'
        ]
        
        response = random.choice(responses)
        await ctx.send(response)

    @commands.command()
    async def tutorial(self, ctx):
        await ctx.send("<https://www.youtube.com/watch?v=1cuhODT6MGM>")

async def setup(bot):
    await bot.add_cog(KnightHacks(bot))