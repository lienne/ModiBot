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
        embed.add_field(name='server / serverstats / stats / info', value='Displays server info.', inline=False)
        embed.add_field(name='vibe / vibecheck', value='Reads a user\'s vibe. If no user is tagged, reads the author\'s vibe.', inline=False)
        embed.add_field(name='whois', value='Displays the specified user\'s info. If no user is tagged, displays the author\'s info.')
        embed.add_field(name='pfp', value='Displays the specified user\'s profile picture.')
        embed.add_field(name='weather', value='Displays specified city\'s current weather.', inline=False)
        embed.add_field(name='wholesome', value='Displays a wholesome meme.', inline=False)
        embed.add_field(name='cat', value='Displays a random cat.')
        embed.add_field(name='dog', value='Displays a random dog.')
        embed.add_field(name='fact', value='Displays a random fact.', inline=False)
        embed.add_field(name='coinflip / flip', value='Flips a coin.')
        embed.add_field(name='diceroll / roll / dice', value='Rolls a die.')
        embed.add_field(name='eightball / 8ball', value='Gives you a prediction to a question.', inline=False)
        embed.add_field(name='who', value='who?')
        embed.add_field(name='github / gh', value='Modibot Source Code', inline=False)
        embed.add_field(name='tutorial', value='Video tutorial on how to write a discord bot in python. Outdated!', inline=False)

        await ctx.send(embed=embed)
        
    @commands.command()
    async def helpadmin(self, ctx):

        embed = discord.Embed(color=0x5eeba0)
        embed.set_author(name='Administration Commands')
        embed.add_field(name='kick @member', value='Kicks a member from the server.\
        In order for this to work, the bot must have Kick Member permissions.\
        To use this command you must have Kick Members permission.', inline=False)
        embed.add_field(name='ban @member', value='Bans a member from the server.\
        In order for this to work, the bot must have Ban Member permissions.\
        To use this command you must have Ban Members permission.', inline=False)
        embed.add_field(name='unban <id>', value='Unbans a member from the server.\
        This only works through unbanning via ID.\
        In order for this to work, the bot must have Ban Member permissions.\
        To use this command you must have Ban Members permissions.', inline=False)
        embed.add_field(name='mute @member', value='Mutes a member.\
        In order for this to work, the bot must have manage roles permissions.\
        To use this command you must have manage roles permission.', inline=False)
        embed.add_field(name='unmute @member', value='Unmutes a member.\
        In order for this to work, the bot must have manage roles permissions.\
        To use this command you must have manage roles permission.', inline=False)
        embed.add_field(name='clear <value>', value='Clears specified number of messages.\
        In order for this to work, the bot must have manage messages permissions.\
        To use this command you must have manage messages permissions.', inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))