import discord
from discord.ext import commands


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases=['funfact', 'fun-fact'],
        brief='Get a fun fact about our lord and savior',
    )
    async def fact(self, context):
        database = self.client.database
        await context.send(database.random_fact)


def setup(client):
    client.add_cog(Information(client))