import discord
from discord.ext import commands


class Worship(commands.Cog):

    def __init__(self, client):
        self.client = client

    # @commands.command(brief='Find out how many points you have')
    # async def points(self, context):
    #     database = self.client.database
    #     user, mention = context.author, context.author.mention
    #     points = database.get_points(user)
    #     await context.send(database[17].format(points=points, name=mention))

    @commands.group(
        brief='Find out how many points you have or another user has'
    )
    async def points(self, context, user : discord.Member = None):
        if context.invoked_subcommand is None:
            database = self.client.database
            if user is None:
                user = context.author
            mention = user.mention
            points = database.get_points(user)
            await context.send(database[17].format(points=points, name=mention))
        
    @points.command(name='give')
    async def points_give(self, context, user : discord.Member, amount=0):
        database = self.client.database
        database.add_points(user, amount)
        mention = user.mention
        await context.send(database[18].format(points=amount, name=mention))


def setup(client):
    client.add_cog(Worship(client))