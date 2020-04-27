import discord
from discord.ext import commands


class Contribute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    async def submit(self, context):
        if context.invoked_subcommand is None:
            database = self.client.database
            mention = context.author.mention
            await context.send(database[16].format(name=mention))

    @submit.command(name='fact')
    async def submit_fact(self, context, *, submission):
        guild_id = context.guild.id
        mention = context.author.mention
        author_id = context.author.id
        database = self.client.database
        database.submit_fact(guild_id, author_id, 'pending', submission)
        await context.send(database[15].format(name=mention))


def setup(client):
    client.add_cog(Contribute(client))
