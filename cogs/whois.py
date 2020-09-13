import discord
from discord.ext import commands

class Whois(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whois(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        roles = [role for role in member.roles[1:]]

        embed = discord.Embed(color=0x7ce4f7, timestamp=ctx.message.created_at, title=f'User Info - {member}')

        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}')

        embed.add_field(name='ID: ', value=member.id, inline=False)
        embed.add_field(name='Display Name: ', value=member.display_name, inline=False)
        embed.add_field(name='Created Account On: ', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Whois(bot))