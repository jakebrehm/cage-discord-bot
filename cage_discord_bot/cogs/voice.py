# import asyncio

import discord
# import youtube_dl
from discord.ext import commands

# youtube_dl.utils.bug_reports_message = lambda: ''

# ytdl_format_options = {
#     'format': 'bestaudio/best',
#     'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
#     'restrictfilenames': True,
#     'noplaylist': True,
#     'nocheckcertificate': True,
#     'ignoreerrors': False,
#     'logtostderr': False,
#     'quiet': True,
#     'no_warnings': True,
#     'default_search': 'auto',
#     'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
# }

# ffmpeg_options = {
#     'options': '-vn'
# }

# ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


# class YTDLSource(discord.PCMVolumeTransformer):
#     def __init__(self, source, *, data, volume=0.5):
#         super().__init__(source, volume)

#         self.data = data

#         self.title = data.get('title')
#         self.url = data.get('url')

#     @classmethod
#     async def from_url(cls, url, *, loop=None, stream=False):
#         loop = loop or asyncio.get_event_loop()
#         data = await loop.run_in_executor(
#             None,
#             lambda: ytdl.extract_info(url, download=not stream),
#         )

#         if 'entries' in data:
#             # take first item from a playlist
#             data = data['entries'][0]

#         filename = data['url'] if stream else ytdl.prepare_filename(data)
#         return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Voice(commands.Cog):

    def __init__(self, client):
        self.client = client
        # discord.opus.load_opus('opus')

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
        brief='Have Nic leave the voice channel he is currently in',
    )
    async def leave(self, context):
        if context.message.author.voice:
            voice_client = context.voice_client
            await voice_client.disconnect()

    # @commands.command(
    #     pass_context=True,
    #     brief='Have Nic stream audio to the voice channel he is currently in',
    # )
    # async def play(self, context, url):
    #     voice_client = context.voice_client

    #     async with context.typing():
    #         player = await YTDLSource.from_url(url)
    #         voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    #     await context.send('Now playing: {}'.format(player.title))


def setup(client):
    client.add_cog(Voice(client))
