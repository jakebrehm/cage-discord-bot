import discord
from discord.ext import commands


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['fact', 'fun-fact'])
    async def funfact(self, context):
        database = self.client.database
        await context.send(database.random_fact)


def setup(client):
    client.add_cog(Information(client))