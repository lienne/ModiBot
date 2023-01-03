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
                        embed = discord.Embed(description = ctx.author.mention + " checked in with email " + email + ". Added Hacker role to " + ctx.author.mention + ".", color=0x00ff00)
                        await channel.send(embed = embed)
                        await ctx.author.send("Congratulations, Hacker! You are checked in.")

                    elif response.status == 409:
                        embed = discord.Embed(description = ctx.author.mention + " tried checking in again with email " + email, color=0xff0000)
                        await channel.send(embed = embed)
                        await ctx.author.send("You are already checked in.")

                    elif response.status == 403:
                        embed = discord.Embed(description = ctx.author.mention + " tried checking in without RSVP, with email " + email)
                        await channel.send(embed = embed)
                        await ctx.author.send("It looks like you haven't RSVPed. Please confirm your attendance through your acceptance or reminder email and then try checking in again.")

                    else:
                        embed = discord.Embed(description = ctx.author.mention + " failed to check in with email " + email, color=0xff0000)
                        await channel.send(embed = embed)
                        await ctx.author.send("Invalid email. Please check if this is the email you registered with or check your spelling. If you are still experiencing problems checking in, please contact an organizer.")
                
                except Exception as e:
                    print(e)
                    embed = discord.Embed(description = ctx.author.mention + " failed to check in with email " + email, color=0xff0000)
                    await channel.send(embed = embed)
                    await ctx.author.send("Invalid email. Please check if this is the email you registered with or check your spelling. If you are still experiencing problems checking in, please contact an organizer.")

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
                        print(response.status)
                        await ctx.author.send("Invalid email.")
                
                except Exception as e:
                    print(e)
                    await ctx.author.send("Invalid email.")


async def setup(bot):
    await bot.add_cog(CheckIn(bot))