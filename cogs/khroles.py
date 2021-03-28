import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
LANG_MSGID = os.getenv('823687567206776862')
OTHER_MSGID = os.getenv('823687567206776862')

class KHRoles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    lang_roles = {
        # 'emoji' : 'rolename'
        "python": "Python",
        "java": "Java",
        "javascript": "JavaScript",
        "htmlcss": "HTML/CSS",
        "clang": "C Language",
        "cplusplus": "C++",
        "csharp": "C#",
        "golang": "Golang",
        "rust": "Rust",
        "lua": "Lua"
    }

    skills = {
        "mobile_dev": "Mobile Development",
        "web_dev": "Web Development",
        "🌐": "Internet of Things",
        "📊": "Big Data",
        "🤖": "Artificial Intelligence",
        "galaxybrain": "Machine Learning",
        "☁️": "Cloud Computing",
        "⛓️": "Blockchain",
        "react": "React",
        "gcp": "GCP",
        "azure": "Azure",
        "aws": "AWS",
        "unity": "Unity"
    }

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.guild_id is None:
            return

        message_id = payload.message_id
        role = None

        if message_id == int(LANG_MSGID):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

            if payload.emoji.name in self.lang_roles:
                role = discord.utils.get(guild.roles, name = self.lang_roles[payload.emoji.name])
            else:
                role = discord.utils.get(guild.roles, name = payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print('Role assignment: Done.')
                else:
                    print('Role not found.')

        if message_id == int(OTHER_MSGID):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

            if payload.emoji.name in self.skills:
                role = discord.utils.get(guild.roles, name = self.skills[payload.emoji.name])
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

        if message_id == int(LANG_MSGID):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

            if payload.emoji.name in self.lang_roles:
                role = discord.utils.get(guild.roles, name = self.lang_roles[payload.emoji.name])
            else:
                role = discord.utils.get(guild.roles, name = payload.emoji.name)
            
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print('Role removal: Done.')
            else:
                print('Role not found.')

        if message_id == int(OTHER_MSGID):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

            if payload.emoji.name in self.skills:
                role = discord.utils.get(guild.roles, name = self.skills[payload.emoji.name])
            else:
                role = discord.utils.get(guild.roles, name = payload.emoji.name)
            
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print('Role removal: Done.')
            else:
                print('Role not found.')


def setup(bot):
    bot.add_cog(KHRoles(bot))