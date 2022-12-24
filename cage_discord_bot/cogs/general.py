import discord
from discord.ext import commands


class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Check in on Nic')
    async def ping(self, context):
        message = self.client.database[1].format(name=context.author.mention)
        await context.send(message)

    @commands.command(brief='Have Nic repeat what you say')
    async def say(self, context, *, text):
        await context.message.delete()
        await context.send(text)


async def setup(client):
    await client.add_cog(General(client))
