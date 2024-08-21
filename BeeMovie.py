from decouple import config
import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

logging_handler = logging.FileHandler(
    filename='BeeMovie.log', encoding='utf-8', mode='w')

dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(
    '[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
logging_handler.setFormatter(formatter)
logger.addHandler(logging_handler)

intents = discord.Intents.all()  # All intents
client = discord.Client(intents=intents)

SECRET_KEY = config("BEE_MOVIE_SCRIPT_SECRET_KEY")

TEXT_CHAN_NAME_DICT = {}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    # Text Channel Name Dictionary
    for text_chan in client.guilds[0].text_channels:
        TEXT_CHAN_NAME_DICT[text_chan.name] = text_chan.id

    print("TEXT CHANNEL NAME DICTIONARY IS READY!")


@client.event
async def on_message(message):
    if not isinstance(message.channel, discord.channel.TextChannel):
        return
    if not message.channel.name == "general":
        return

    if message.author.bot:
        return

    queue_file = 'Script-Queue.txt'
    tracking_file = 'Script-Sent.txt'

    # Step 1: Read the queue file and remove the first line
    with open(queue_file, 'r') as queue:
        lines = queue.readlines()

    if not lines:
        print("Queue file is empty, nothing to dequeue.")
        return

    first_line = lines.pop(0)  # Remove the first line
    print(first_line)

    await message.guild.get_channel(TEXT_CHAN_NAME_DICT["general"]).send(first_line)

    # Step 2: Append the first line to the tracking file
    with open(tracking_file, 'a') as dest:
        dest.write(first_line)

    # Step 3: Rewrite the queue file without the removed first line
    with open(queue_file, 'w') as queue:
        queue.writelines(lines)

try:
    client.run(SECRET_KEY, log_handler=logging_handler)

except discord.errors.HTTPException as e:
    print("\n----- DISCORD ERROR HTTP EXCEPTION -----\n")
    print("e: ", e, "\n+++++++++++++++++++++++++")
    print("e.response.response: ", e.response._headers)
    print("Retry-After: ",
          e.response._headers['Retry-After'], "Seconds \n+++++++++++++++++++++++++")
