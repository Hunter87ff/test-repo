import os
import dotenv
import discord
from discord.ext import commands
from cog.reactionrole import ReactionRole

dotenv.load_dotenv()


bot = commands.AutoShardedBot(
    command_prefix=".",
    intents = discord.Intents.all()
)

@bot.event
async def setup():
    await ReactionRole.setup(bot) #type: ignore

@bot.event
async def on_ready():
    print(f"bot : {bot.user}")





token= str(os.environ.get("TOKEN"))
bot.run(token) #type: ignore