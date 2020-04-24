import asyncio

import discord
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def on_member_join(self, member):
        print(f'{member} has joined the server.')

    async def on_member_remove(self, member):
        print(f'{member} has left the server.')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, context, amount=5):
        await context.channel.purge(limit=amount+1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await context.send(f"Kicked {member.mention}.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await context.send(f"Banned {member.mention}.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, context, *, member):
        banned_users = await context.guild.bans()
        name, discriminator = member.split('#')

        for banned_user in banned_users:
            user = banned_user.user
            if (user.name, user.discriminator) == (name, discriminator):
                await context.guild.unban(user)
                await context.send(f"Unbanned {user.mention}.")
                return

    @commands.command(aliases=['verify', 'approve', 'reject'])
    @commands.has_permissions(ban_members=True)
    async def judge(self, context, which):
        if which == 'fact':
            database = self.client.database
            fact = database.pending_fact

            if not fact:
                await context.send(
                    "No pending facts. Apparently I'm not very interesting."
                )
                return

            message = await context.send(
                f"Maybe you can help me. I'm not sure about this fact:\n\n"

                f"> {fact}\n\n"

                "React to this message with a 👍 to approve, a "
                "👎 to reject, or a 🤷‍♂️ to abstain."
            )
            await message.add_reaction('👍')
            await message.add_reaction('👎')
            await message.add_reaction('🤷‍♂️')

            author_name = context.author.name

            def check(reaction, user):
                correct_user = user == context.author
                valid_emoji = str(reaction.emoji) in ['👍', '👎', '🤷‍♂️']
                return correct_user and valid_emoji

            try:
                reaction, user = await self.client.wait_for(
                    'reaction_add',
                    timeout=10,
                    check=check,
                )
            except asyncio.TimeoutError:
                await context.send(f'Sorry {author_name}, you were too slow.')
            else:
                if reaction.emoji == '🤷‍♂️':
                    await context.send('Another time, then...')
                elif reaction.emoji == '👍':
                    await context.send(
                        f'Thanks for accepting the submission, {author_name}.'
                    )
                    database.judge_fact(fact, 'accepted')
                elif reaction.emoji == '👎':
                    await context.send(
                        f'The submission has been rejected.'
                    )
                    database.judge_fact(fact, 'rejected')


def setup(client):
    client.add_cog(Moderation(client))
