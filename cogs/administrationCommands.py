import discord
from discord.ext import commands

class AdministrationCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Mute
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, member: discord.Member, reason = None):
        muted = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.add_roles(muted)
        await ctx.send(f'{member.mention} has been muted.')

    # Unmute
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, member: discord.Member):
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted"))
        await ctx.send(f'{member.mention} has been unmuted.')

    # Kick
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        """Kicks a member from the server.
        In order for this to work, the bot must have Kick Member permissions.
        To use this command you must have Kick Members permission.
        """

        if reason is None:
            reason = f'Action done by {ctx.author} (ID: {ctx.author.id})'

        try:
            await ctx.guild.kick(member, reason = reason)
            embed = discord.Embed(description = ":white_check_mark: **%s** has been kicked."%member, color=0x00ff00)
            # await ctx.send(f'Kicked {member}. {reason}.')
            return await ctx.send(embed=embed)
        except discord.Forbidden:
            return await ctx.send("Are you trying to ban someone higher than the bot?")

    # Ban
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        """Bans a member from the server.
        In order for this to work, the bot must have Ban Member permissions.
        To use this command you must have Ban Members permission.
        """

        if reason is None:
            reason = f'Action done by {ctx.author} (ID:{ctx.author.id})'

        if not member:
            return await ctx.send("You must specify a user.")
        
        try:
            await ctx.guild.ban(member, reason = reason)
            embed = discord.Embed(description = ":white_check_mark: **%s** has been banned."%member, color=0x00ff00)
            # await ctx.send(f'Banned {member}. {reason}.')
            return await ctx.send(embed=embed)
        except discord.Forbidden:
            return await ctx.send("Are you trying to ban someone higher than the bot?")

    #Multiban
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def multiban(self, ctx, members : commands.Greedy[discord.Member], *, reason = None):
        """Bans multiple members from the server.
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
        """Unbans a member from the server.
        This only works through banning via ID.
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

            embed = discord.Embed(description = ":white_check_mark: **%s** has been unbanned."%userID.name, color = 0x00ff00)

            return await ctx.send(embed = embed)

        except (NameError, discord.NotFound):
            embed = discord.Embed(description = ":x: Either this User ID is not valid or this user is not currently banned. Please input a valid user ID.", color = 0xff0000)
            return await ctx.send(embed = embed)

    # Clear messages
    @commands.command()
    @commands.has_guild_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 0):
        await ctx.channel.purge(limit = amount + 1)
        await ctx.send(f'Deleted {amount} messages.')

# Connect cog to bot
def setup(bot):
    bot.add_cog(AdministrationCommands(bot))