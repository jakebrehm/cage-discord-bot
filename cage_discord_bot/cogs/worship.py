import discord
from discord.ext import commands


class Worship(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Find out how many points you have')
    async def points(self, context):
        database = self.client.database
        user, mention = context.author, context.author.mention
        points = database.get_points(user)
        await context.send(database[17].format(points=points, name=mention))


def setup(client):
    client.add_cog(Worship(client))