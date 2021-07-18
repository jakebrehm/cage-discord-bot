import discord
from discord.ext import commands


class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Have Nic write the role selector message')
    @commands.has_permissions(administrator=True)
    async def roles(self, context):
        not_pinned = lambda message: not message.pinned
        await context.channel.purge(limit=1, check=not_pinned)
        database = self.client.database
        selector = await context.send(database[27])
        for emoji in ['🎮']:
            await selector.add_reaction(emoji)


def setup(client):
    client.add_cog(Roles(client))
