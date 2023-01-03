import discord
from discord.ext import commands

class Stats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['server', 'serverstats', 'info'])
    async def stats(self, ctx):
        guild = ctx.guild

        online = sum(member.status is discord.Status.online or member.status is discord.Status.do_not_disturb or member.status is discord.Status.idle for member in guild.members)

        embed = discord.Embed(color=0x7ce4f7, timestamp=ctx.message.created_at, title=f'Server Info - {guild.name}')
        
        embed.set_thumbnail(url=guild.icon)
        embed.set_footer(text=f'Requested by {ctx.author}')

        embed.add_field(name='Created on:', value=guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name='Owner:', value=guild.owner.name, inline=False)
        embed.add_field(name='Total Members:', value=guild.member_count, inline=False)
        embed.add_field(name='Currently Online:', value=str(online), inline=False)
        embed.add_field(name='Server Boosts:', value=str(guild.premium_subscription_count))

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Stats(bot))