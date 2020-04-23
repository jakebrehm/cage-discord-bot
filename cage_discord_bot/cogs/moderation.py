import discord
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def on_member_join(self, member):
        print(f'{member} has joined the server.')

    async def on_member_remove(self, member):
        print(f'{member} has left the server.')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, context, amount=5):
        await context.channel.purge(limit=amount+1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await context.send(f"Kicked {member.mention}.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await context.send(f"Banned {member.mention}.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, context, *, member):
        banned_users = await context.guild.bans()
        name, discriminator = member.split('#')

        for banned_user in banned_users:
            user = banned_user.user
            if (user.name, user.discriminator) == (name, discriminator):
                await context.guild.unban(user)
                await context.send(f"Unbanned {user.mention}.")
                return

    @commands.command(aliases=['approve'])
    @commands.has_permissions(ban_members=True)
    async def verify(self, context, which):
        if which == 'fact':
            database = self.client.database
            fact = database.pending_fact
            await context.send("I'm not sure about this fact:")
            await context.send(fact)


def setup(client):
    client.add_cog(Moderation(client))