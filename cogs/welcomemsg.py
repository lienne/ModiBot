import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
LOGGING_CHANNEL = os.getenv('LOGGING_CHANNEL_ID')

class WelcomeMsg(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        new_user_msg = """
        Welcome to Knight Hacks 2020! We're excited that you're here!

To check in, please **reply to this DM** with the command `!checkin <email you used to register>` (Do not include the < >).

Sponsors, mentors, and judges, please message an organizer to be granted the appropriate permissions.

By entering the server, you agree that all of your interactions will abide by the MLH Code of Conduct.

Good luck, have fun, and we can't wait to see what you build!
        """

        channel = self.bot.get_channel(int(LOGGING_CHANNEL))

        await channel.send("User " + member.display_name + " joined the server.")

        try:
            await member.send(new_user_msg)
            await channel.send("Sent DM to " + member.display_name)
        except:
            await channel.send("Couldn't send welcome DM to " + member.display_name)

    @commands.command()
    async def sendwelcomemsg(self, ctx):
        is_owner = await self.bot.is_owner(ctx.author)
        
        if not is_owner:
            await ctx.author.send("You do not have permissions for this command.")
            return
            
        welcome_msg = """
        Welcome to Knight Hacks 2020! We're excited that you're here!

To check in, please **send a Direct Message to the bot** (that's me, Lancelot!) with the command `!checkin <email you used to register>`.

Sponsors, mentors, and judges, please message an organizer to be granted the appropriate permissions.

By entering the server, you agree that all of your interactions will abide by the MLH Code of Conduct. Please set your server nickname to be your real name to promote collaboration and make it easier for everyone to find each other.

Good luck, have fun, and we can't wait to see what you build!
        """

        await ctx.send(welcome_msg)

def setup(bot):
    bot.add_cog(WelcomeMsg(bot))