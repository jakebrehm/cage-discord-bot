import discord
import json
import os
import random
from discord.ext import commands


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.FUN_FACTS = os.path.join('..', 'data', 'facts.json')

    @commands.command(aliases=['fact', 'fun-fact'])
    async def funfact(self, context):
        with open(self.FUN_FACTS, 'r') as json_file:
            facts = json.load(json_file)
        await context.send(random.choice(facts))


def setup(client):
    client.add_cog(Information(client))