import discord
import youtube_dl
from discord.ext import commands


class Voice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @client.command(
        pass_context=True,
        brief='Have Nic join the voice channel you are currently in',
    )
    async def join(context):
        if context.message.author.voice:
            channel = context.message.author.voice.channel
            await channel.connect()

    @client.command(
        pass_context=True,
        brief='Have Nic join the voice channel you are currently in',
    )
    async def leave(context):
        if context.message.author.voice:
            channel = context.message.author.voice.channel
            await channel.disconnect()


def setup(client):
    client.add_cog(Voice(client))
