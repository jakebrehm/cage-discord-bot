import asyncio

import discord
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Clear messages from the chat')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, context, amount=None):
        not_pinned = lambda message: not message.pinned
        if amount is None:
            await context.channel.purge(limit=None, check=not_pinned)
        else:
            await context.channel.purge(limit=int(amount)+1, check=not_pinned)

    @commands.command(brief='Kick a user')
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member : discord.Member, *, reason=None):
        mention = member.mention
        await member.kick(reason=reason)
        await context.send(self.client.database[6].format(name=mention))

    @commands.command(brief='Ban a user')
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member : discord.Member, *, reason=None):
        mention = member.mention
        await member.ban(reason=reason)
        await context.send(self.client.database[7].format(name=mention))

    @commands.command(brief='Unban a user')
    @commands.has_permissions(ban_members=True)
    async def unban(self, context, *, member):
        banned_users = await context.guild.bans()
        name, discriminator = member.split('#')

        async for banned_user in banned_users:
            user = banned_user.user
            mention = user.mention
            if (user.name, user.discriminator) == (name, discriminator):
                await context.guild.unban(user)
                await context.send(self.client.database[8].format(name=mention))
                return

    @commands.group(brief='Accept or reject user submissions')
    @commands.has_permissions(administrator=True)
    async def judge(self, context):
        if context.invoked_subcommand is None:
            database = self.client.database
            mention = context.author.mention
            await context.send(database[18].format(name=mention))

    @judge.command(name='fact')
    async def judge_fact(self, context):
        database = self.client.database
        fact = database.pending_fact

        if not fact:
            await context.send(database[9])
            return

        message = await context.send(
            database[10] +

            f"\n\n> {fact}\n\n"

            "React to this message with a 👍 to approve, a "
            "👎 to reject, or a 🤷‍♂️ to abstain."
        )
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('🤷‍♂️')

        mention = context.author.mention

        def check(reaction, user):
            correct_user = (user == context.author)
            valid_emoji = str(reaction.emoji) in ['👍', '👎', '🤷‍♂️']
            return correct_user and valid_emoji

        try:
            reaction, user = await self.client.wait_for(
                'reaction_add',
                timeout=60,
                check=check,
            )
        except asyncio.TimeoutError:
            await context.send(database[11].format(name=mention))
        else:
            if reaction.emoji == '🤷‍♂️':
                await context.send(database[12].format(name=mention))
            elif reaction.emoji == '👍':
                await context.send(database[13].format(name=mention))
                database.judge_fact(fact, 'accepted')
            elif reaction.emoji == '👎':
                await context.send(database[14].format(name=mention))
                database.judge_fact(fact, 'rejected')


def setup(client):
    client.add_cog(Moderation(client))
