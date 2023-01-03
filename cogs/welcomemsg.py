import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
LOGGING_CHANNEL = os.getenv('LOGGING_CHANNEL_ID')

class WelcomeMsg(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#     @commands.Cog.listener()
#     async def on_member_join(self, member):
#         new_user_msg = """
#         Welcome to Knight Hacks 2020! We're excited that you're here!

# To check in, please **reply to this DM** with the command `!checkin youremail@email.com` to be assigned the Hacker role. Checking in will only work if you have RSVP'd, so make sure to do that before trying to check in!

# Sponsors, mentors, and judges, please message an organizer to be granted the appropriate permissions.

# By entering the server, you agree that all of your interactions will abide by the MLH Code of Conduct.

# Good luck, have fun, and we can't wait to see what you build!
#         """

#         channel = self.bot.get_channel(int(LOGGING_CHANNEL))

#         embed = discord.Embed(description = "User " + member.mention + " joined the server.", color=0x00ff00)
#         await channel.send(embed = embed)

#         try:
#             embed = discord.Embed(description = "Sent DM to " + member.mention, color=0x00ff00)
#             # await member.send(new_user_msg)
#             # await channel.send(embed = embed)
#         except:
#             embed = discord.Embed(description = "Couldn't send welcome DM to " + member.mention, color=0xff0000)
#             # await channel.send(embed = embed)

#     @commands.command()
#     async def sendwelcomemsg(self, ctx):
#         is_owner = await self.bot.is_owner(ctx.author)
        
#         if not is_owner:
#             await ctx.author.send("You do not have permissions for this command.")
#             return
            
#         welcome_msg = """
#         Welcome to Knight Hacks 2020! We're excited that you're here!

# The Club server is currently closed for the hackathon, so only Knight Hacks participants are allowed in for the weekend. Don't worry, the server will be re-opened afterwards!

# To check in for the event, please **send a Direct Message to the bot** (that's me, Lancelot!) with the command `!checkin youremail@email.com` to be assigned the Hacker role. Checking in will only work if you have RSVP'd, so make sure to do that before trying to check in!

# Sponsors, mentors, and judges, please message an organizer to be granted the appropriate permissions.

# By entering the server, you agree that all of your interactions will abide by the MLH Code of Conduct. Please set your server nickname to be your real name to promote collaboration and make it easier for everyone to find each other.

# Good luck, have fun, and we can't wait to see what you build!
#         """

#         await ctx.send(welcome_msg)

async def setup(bot):
    await bot.add_cog(WelcomeMsg(bot))