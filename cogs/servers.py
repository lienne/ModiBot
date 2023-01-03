import discord
from discord.ext import commands

class Servers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Prints the names of all servers the bot is in
    @commands.command()
    async def serversinfo(self, ctx):
        is_owner = await self.bot.is_owner(ctx.author)

        if not is_owner:
            await ctx.author.send("You do not have permissions for this command.")
            return

        all_servers = []
        for guild in self.bot.guilds:
            all_servers.append(guild.name)
            # print(guild.name)

        title = "These are all the servers this bot is in:"
        embed = discord.Embed(title = title, color=0x7ce4f7,timestamp=ctx.message.created_at)
        embed.add_field(name="Servers:", value=all_servers)
        embed.set_footer(text=f"Requested by {ctx.author.name}")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Servers(bot))