import discord
from discord.ext import commands


class Worship(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(
        brief='Find out how many points you have or another user has',
        invoke_without_command=True,
    )
    async def points(self, context, user : discord.Member = None):
        if context.invoked_subcommand is None:
            database = self.client.database
            m = 17 if user is None else 19
            user = context.author if user is None else user
            mention = user.mention
            points = database.get_points(user)
            await context.send(database[m].format(points=points, name=mention))
        
    @points.command(name='give')
    @commands.has_permissions(administrator=True)
    async def points_give(self, context, user : discord.Member, amount=0):
        database = self.client.database
        database.add_points(user, amount)
        mention = user.mention
        await context.send(database[20].format(points=amount, name=mention))
        await self.client.assign_role(user)


async def setup(client):
    await client.add_cog(Worship(client))