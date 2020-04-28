import discord
import praw
from discord.ext import commands


class Web(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.reddit = praw.Reddit(
            client_id=self.client.config['reddit']['client id'],
            client_secret=self.client.config['reddit']['client secret'],
            user_agent=self.client.config['reddit']['user agent'],
        )

    @commands.command(
        aliases=['top', 'top-post', 'topreddit', 'top-reddit'],
        brief='Get a link to the current top /r/onetruegod post',
    )
    async def toppost(self, context):
        top_posts = self.reddit.subreddit('onetruegod').hot(limit=3)
        for post in top_posts:
            if not post.stickied:
                title = post.title
                subreddit = post.subreddit_name_prefixed
                score = post.ups + post.downs # post.score
                comments = post.num_comments
                link = f'https://www.reddit.com{post.permalink}'

                embed = discord.Embed(
                    title=f'{subreddit} - {title}',
                    author=post.author,
                    description=f'{score} points and {comments} comments so far on Reddit',
                    url=link,
                )
                embed.set_thumbnail(url=post.thumbnail)

                await context.send(content=None, embed=embed)
                return


def setup(client):
    client.add_cog(Web(client))