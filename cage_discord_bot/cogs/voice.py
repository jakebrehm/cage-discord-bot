import discord
import youtube_dl
from discord.ext import commands


class Voice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
        pass_context=True,
        brief='Have Nic join the voice channel you are currently in',
    )
    async def join(self, context):
        if context.message.author.voice:
            channel = context.message.author.voice.channel
            await channel.connect()

    @commands.command(
        pass_context=True,
        brief='Have Nic join the voice channel you are currently in',
    )
    async def leave(self, context):
        if context.message.author.voice:
            voice_client = context.voice_client
            await voice_client.disconnect()


def setup(client):
    client.add_cog(Voice(client))
