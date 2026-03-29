import os
import dotenv
import requests
import discord
from discord.ext import commands
# from cog.reactionrole import ReactionRole

dotenv.load_dotenv()


bot = commands.AutoShardedBot(
    command_prefix=".",
    intents = discord.Intents.all()
)

@bot.event
async def setup():
    pass
    # await ReactionRole.setup(bot) #type: ignore

@bot.event
async def on_ready():
    print(f"bot : {bot.user}")


@bot.command("sticky")
async def sticky(ctx : commands.Context, channel: discord.TextChannel, *, messge):
    _response = requests.post(
        "http://localhost:8000/sticky",
        json={
            "channel_id" : channel.id,
            "message" : messge
        }
    )

    print(
        _response.text
    )

    if _response.status_code == 200:
        await ctx.send(
        "sticky message created !!"
        )

    
    await ctx.send(
            str(_response.json())
        )







token= str(os.environ.get("TOKEN"))
bot.run(token) #type: ignore