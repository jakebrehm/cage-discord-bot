import discord
from discord.ext import commands


class Contribute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['remind'])
    async def submit(self, context, which, *, submission):
        if which in ['fact', 'fun-fact']:
            await context.send(
                f"Thanks for reminding me, {context.author.name}. "
                f"I can't believe I forgot."
            )
        else:
            await context.send(
                f"What are you trying to remind me of, {context.author.name}? "
                f"I don't understand."
            )


def setup(client):
    client.add_cog(Contribute(client))