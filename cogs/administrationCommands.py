import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import asyncio

class AdministrationCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    """
        TO DO:
        Log these events to logging channel.
        Find a better way to delete bot "deleted x msgs" confirmation msg.
    """

    # Mute
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, member: discord.Member, reason = None):
        """
        Mutes a member.
        In order for this to work, the bot must have manage roles permissions.
        To use this command you must have manage roles permission.
        """

        muted = discord.utils.get(ctx.guild.roles, name="Muted")

        if muted is None:
            return await ctx.send(f'This server does not have a Muted role.')

        if member is ctx.author:
            return await ctx.send("Why are you trying to mute yourself?")

        await member.add_roles(muted)
        embed = discord.Embed(description = f'{member.mention} has been muted.', color=0xb9b9b9)
        await ctx.send(embed=embed)

    # Lacking Perms for Mute
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(description = ":no_entry_sign: You don't have permission to use that command.", color=0xff0000)
            await ctx.send(embed=embed)

    # Unmute
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, member: discord.Member):
        """
        Unmutes a member.
        In order for this to work, the bot must have manage roles permissions.
        To use this command you must have manage roles permission.
        """

        muted = discord.utils.get(ctx.guild.roles, name="Muted")

        if muted is None:
            return await ctx.send(f'This server does not have a Muted role.')

        if muted not in member.roles:
            return await ctx.send(f'{member.mention} is not muted.')

        await member.remove_roles(muted)
        embed = discord.Embed(description = f'{member.mention} has been unmuted.', color=0xb9b9b9)
        await ctx.send(embed=embed)

    # Lacking Perms for Unmute
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(description = ":no_entry_sign: You don't have permission to use that command.", color=0xff0000)
            await ctx.send(embed=embed)

    # Kick
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        """
        Kicks a member from the server.
        In order for this to work, the bot must have Kick Member permissions.
        To use this command you must have Kick Members permission.
        """

        if not member:
            return await ctx.send("You must specify a user.")

        if member is ctx.author:
            return await ctx.send("Why are you trying to kick yourself?")

        try:
            """
            This currently sends the user a DM even if the kicking fails.
            The reason is that the bot cannot message a user directly if they don't share a server. So the message must be sent before kicking is attempted (and thus, before
            the exception is caught).
            This is true for banning as well.
            """
            if reason is None:
                await member.send(f'You have been kicked from {ctx.guild}.')
            else:
                await member.send(f'You have been kicked from {ctx.guild}. Reason given: {reason}')

            await ctx.guild.kick(member, reason = reason)
            embed = discord.Embed(description = f':white_check_mark: {member.mention} has been kicked.', color=0x00ff00)

            return await ctx.send(embed=embed)

        except discord.Forbidden:
            await member.send(f'Kicking failed.')
            return await ctx.send("Are you trying to kick someone higher than the bot?")

    # Lacking Perms for Kick
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(description = ":no_entry_sign: You don't have permission to use that command.", color=0xff0000)
            await ctx.send(embed=embed)

    # Ban
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        """
        Bans a member from the server.
        In order for this to work, the bot must have Ban Member permissions.
        To use this command you must have Ban Members permission.
        """

        # if reason is None:
        #     reason = f'Action done by {ctx.author} (ID:{ctx.author.id})'

        if not member:
            return await ctx.send("You must specify a user.")

        if member is ctx.author:
            return await ctx.send("Why are you trying to ban yourself?")
        
        try:
            """
            This currently sends the user a DM even if the ban fails.
            The reason is that the bot cannot message a user directly if they don't share a server. So the message must be sent before banning is attempted (and thus, before
            the exception is caught).
            This is true for kicking as well.
            """
            if reason is None:
                await member.send(f'You have been banned from {ctx.guild}.')
            else:
                await member.send(f'You have been banned from {ctx.guild}. Reason given: {reason}')

            await ctx.guild.ban(member, delete_message_days = 0, reason = reason)
            embed = discord.Embed(description = f':white_check_mark: {member.mention} has been banned.', color=0x00ff00)

            return await ctx.send(embed=embed)

        except discord.Forbidden:
            await member.send(f'Banning failed.')
            return await ctx.send("Are you trying to ban someone higher than the bot?")

    # Lacking Perms for Ban
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(description = ':no_entry_sign: You don\'t have permission to use that command.', color=0xff0000)
            await ctx.send(embed=embed)


    #Multiban
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def multiban(self, ctx, members : commands.Greedy[discord.Member], *, reason = None):
        """
        Currently not working.
        Bans multiple members from the server.
        This only works through banning via ID.
        In order for this to work, the bot must have Ban Member permissions.
        To use this command you must have Ban Members permission.
        """

        if reason is None:
            reason = f'Action done by {ctx.author} (ID:{ctx.author.id})'
        
        total_members = len(members)
        if total_members == 0:
            return await ctx.send('Missing members to ban.')
        
        confirm = await ctx.prompt(f'This will ban **{total_members:member}** members. Are you sure?', reacquire = False)
        if not confirm:
            return await ctx.send('Aborting.')

        failed = 0
        for member in members:
            try:
                await ctx.guild.ban(member, reason = reason)
            except discord.HTTPException:
                failed += 1
        
        await ctx.send(f'Banned {total_members - failed}/{total_members} members. {reason}')

    # Unban
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userID, reason = None):
        """
        Currently confirmation message isn't being sent.
        Unbans a member from the server.
        This only works through unbanning via ID.
        In order for this to work, the bot must have Ban Member permissions.
        To use this command you must have Ban Members permissions.
        """

        if not userID.isdigit():
            embed = discord.Embed(description = ":x: Input a Valid User ID.", color = 0xff0000)
            return await ctx.send(embed = embed)

        if reason is None:
            reason = f'Action done by {ctx.author} (ID:{ctx.author.id})'

        try:
            user = discord.Object(id = userID)
            await ctx.guild.unban(user, reason = reason)

            embed = discord.Embed(description = f':white_check_mark: {user} has been unbanned.', color = 0x00ff00)
            # embed.add_field(name='Reason:', value=f'{reason}', inline=False)

            return await ctx.send(embed=embed)

        except (NameError, discord.NotFound):
            embed = discord.Embed(description = ":x: Either this User ID is not valid or this user is not currently banned. Please input a valid user ID.", color = 0xff0000)
            return await ctx.send(embed = embed)

    # Lacking Perms for Unban
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(description = ":no_entry_sign: You don't have permission to use that command.", color=0xff0000)
            await ctx.send(embed=embed)

    # Clear messages
    @commands.command()
    @commands.has_guild_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 0):
        """
        Clears specified number of messages.
        In order for this to work, the bot must have manage messages permissions.
        To use this command you must have manage messages permissions.
        """
        await ctx.channel.purge(limit = amount + 1)
        await ctx.send(f'Deleted {amount} messages.')
        await asyncio.sleep(5)
        await ctx.channel.purge(limit = 1)

    # Lacking Perms for Clear
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(description = ":no_entry_sign: You don't have permission to use that command.", color=0xff0000)
            await ctx.send(embed=embed)

# Connect cog to bot
def setup(bot):
    bot.add_cog(AdministrationCommands(bot))