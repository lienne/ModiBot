import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import aiohttp

"""
Check-in feature for KnightHacks 2020.
"""

load_dotenv()
SERVER_ID = os.getenv('KH_SERVER_ID')
HACKER_ROLE_ID = os.getenv('KH_HACKER_ROLE')
LOGGING_CHANNEL = os.getenv('LOGGING_CHANNEL_ID')

class CheckIn(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def checkin(self, ctx, email: str = ''):
        url = 'http://kh-functions-app.azurewebsites.net/api/sign_in_hacker_email'
        channel = self.bot.get_channel(int(LOGGING_CHANNEL))

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json = {'email' : email}) as response:
                try:
                    if response.status == 200:
                        # Assign Hacker role to member checked-in
                        guild = self.bot.get_guild(int(SERVER_ID))
                        role = guild.get_role(int(HACKER_ROLE_ID))
                        member = guild.get_member(ctx.author.id)

                        await member.add_roles(role)
                        # embed = discord.Embed(description = ctx.author.mention + " checked in with email " + email + ". Added Hacker role to " + ctx.author.display_name + ".", color=0x00ff00)
                        # await channel.send(embed = embed)
                        await channel.send(ctx.author.display_name + " checked in with email " + email + ". Added Hacker role to " + ctx.author.display_name + ".")
                        await ctx.author.send("Congratulations, Hacker! You are checked in.")

                    elif response.status == 409:
                        await channel.send(ctx.author.display_name + " tried checking in again with email " + email)
                        await ctx.author.send("You are already checked in.")

                    else:
                        await channel.send(ctx.author.display_name + " failed to check in with email " + email)
                        await ctx.author.send("Invalid email. Please check your spelling. If you are still experiencing problems checking in, please contact an organizer.")
                
                except Exception as e:
                    print(e)
                    await channel.send(ctx.author.display_name + " failed to check in with email " + email)
                    await ctx.author.send("Invalid email. Please check your spelling. If you are still experiencing problems checking in, please contact an organizer.")

    @commands.command()
    async def clearcheckin(self, ctx, email: str = ''):
        is_owner = await self.bot.is_owner(ctx.author)
        
        if not is_owner:
            await ctx.author.send("You do not have permissions for this command.")
            return

        url = 'http://kh-functions-app.azurewebsites.net/api/sign_in_hacker_email'
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json = {'email' : email, 'status' : False}) as response:
                try:
                    if response.status == 200:
                        await ctx.author.send("User un-checked in successfully.")
                    elif response.status == 409:
                        await ctx.author.send("This user is not checked in.")
                    else:
                        await ctx.author.send("Invalid email.")
                
                except Exception as e:
                    print(e)
                    await ctx.author.send("Invalid email.")


def setup(bot):
    bot.add_cog(CheckIn(bot))