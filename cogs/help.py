import discord
from discord.ext import commands
import os

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(color=0x7ce4f7)
        embed.set_author(name='Available Commands')
        embed.set_thumbnail(url='https://github.com/lienne/ModiBot/blob/master/cogs/img/headphonesdog.png?raw=true')
        # embed.add_field(name='', value='', inline=False)
        embed.add_field(name='ping', value='Pong! With latency.', inline=False)
        # embed.add_field(name='when', value='Time until KnightHacks starts / ends.')
        # embed.add_field(name='where', value='Important hackathon links.')
        # embed.add_field(name='how', value='Hacker guide.')
        # embed.add_field(name='schedule', value='Knight Hacks schedule', inline=False)
        embed.add_field(name='coinflip / flip', value='Flips a coin.')
        embed.add_field(name='diceroll / roll / dice', value='Rolls a die.')
        embed.add_field(name='eightball / 8ball', value='Gives you a prediction to a question.', inline=False)
        embed.add_field(name='vibe', value='Reads a user\'s vibe. If no user is tagged, reads the author\'s vibe.', inline=False)
        embed.add_field(name='whois', value='Displays the specified user\'s info. If no user is tagged, displays the author\'s info.')
        embed.add_field(name='pfp', value='Displays the specified user\'s profile picture.')
        embed.add_field(name='server / serverstats / stats / info', value='Displays server info.', inline=False)
        embed.add_field(name='weather', value='Displays specified city\'s current weather.', inline=False)
        embed.add_field(name='cat', value='Displays a random cat.')
        embed.add_field(name='dog', value='Displays a random dog.')
        embed.add_field(name='fact', value='Displays a random fact.', inline=False)
        embed.add_field(name='why', value='<:yeehaw:762850304781189161>')
        embed.add_field(name='who', value='who?')
        embed.add_field(name='reee', value='reee')
        embed.add_field(name='REEE', value='Ultra reee')
        embed.add_field(name='github / gh', value='Modibot Source Code', inline=False)
        embed.add_field(name='tutorial', value='Video tutorial on how to write a discord bot in python.', inline=False)

        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Help(bot))