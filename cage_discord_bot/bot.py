import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready.')

if __name__ == '__main__':

    # Use pathlib to get the path of the project folder
    import pathlib
    PROJECT_DIRECTORY = pathlib.Path(__file__).parent.parent
    DATA_FOLDER = os.path.join(PROJECT_DIRECTORY, 'data')

    # Read the configuration file
    config = configparser.ConfigParser()
    CONFIG_PATH = os.path.join(DATA_FOLDER, 'config.ini')
    config.read(CONFIG_PATH)

    # Read the login information for the first toon
    token = config['authorization']['token']

    client.run(token)