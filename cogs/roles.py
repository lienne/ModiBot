import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
MSGID = os.getenv('823687567206776862')

class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    roles_map = {
        # Format:
        # 'emoji' : 'rolename'
        "👔": "OPS",
        "python": "Python",
        "java": "Java",
        "clang": "CLang",
        "cplusplus": "C++",
        "csharp": "C#",
        "javascript": "JavaScript",
        "htmlcss": "HTML/CSS",
        "rust": "Rust",
        "lua": "Lua",
        "linux": "Linux",
        "windows": "Windows",
        "macos": "MacOS",
        "math": "Math",
        "👩‍🔬": "Physics",
        "knighthacks": "knighthacks"
    }

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.guild_id is None:
            return
        
        message_id = payload.message_id
        role = None
        if message_id == int(MSGID):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

            if payload.emoji.name in self.roles_map:
                role = discord.utils.get(guild.roles, name = self.roles_map[payload.emoji.name])
            else:
                role = discord.utils.get(guild.roles, name = payload.emoji.name)
            
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print('Role assignment: Done.')
            else:
                print('Role not found.')


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.guild_id is None:
            return

        message_id = payload.message_id
        role = None

        if message_id == int(MSGID):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

            if payload.emoji.name in self.roles_map:
                role = discord.utils.get(guild.roles, name = self.roles_map[payload.emoji.name])
            else:
                role = discord.utils.get(guild.roles, name = payload.emoji.name)
            
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print('Role removal: Done.')
            else:
                print('Role not found.')

# Connect cog to bot
def setup(bot):
    bot.add_cog(Roles(bot))